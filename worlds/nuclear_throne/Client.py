import asyncio

import Utils
from copy import deepcopy
from typing import List, Any, Optional
from NetUtils import NetworkItem
from CommonClient import CommonContext, gui_enabled, ClientCommandProcessor, logger, get_base_parser, ClientStatus


class NuclearThroneCommandProcessor(ClientCommandProcessor):
    def _cmd_run_proxy(self):
        """Turn On Nuclear Throne Proxy HTTP Server"""
        logger.info("Starting Nuclear Throne proxy server")

        self.ctx.http_task = asyncio.create_task(
            run_http_server(self.ctx, self.ctx.http_port),
            name="Nuclear Throne Proxy"
        )

    def _cmd_end_proxy(self):
        """Turn Off Nuclear Throne Proxy HTTP Server"""
        if self.ctx.http_server is not None:
            logger.info("Stopping Nuclear Throne proxy server")
            asyncio.create_task(self.ctx.http_server.cleanup())
            self.ctx.http_server = None
        else:
            logger.info("Error: Server Not Found")

    async def _cmd_deathlink(self):
        """Toggles deathlink"""
        if isinstance(self.ctx, NuclearThroneContext):
            if "DeathLink" in self.ctx.tags:
                self.ctx.tags.remove("DeathLink")
                self.output(f"Deathlink disabled. {self.ctx.tags}")
            else:
                self.ctx.tags.add("DeathLink")
                self.output(f"Deathlink enabled. {self.ctx.tags}")
            await self.ctx.disconnect(True)


class NuclearThroneContext(CommonContext):
    command_processor = NuclearThroneCommandProcessor
    game = "Nuclear Throne"

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.http_port = 9916
        self.http_server = None
        self.http_task = None
        self.items_handling = 0b111
        self.room_info = None
        self.full_inventory: List[Any] = []
        self.awaiting_items: List[Any] = []
        self.deathlink_occurrence = False
        self.slot_data = None
        self.goal_number = 1
        self.goal_complete = 0
        self.finished_game = False

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(NuclearThroneContext, self).server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    async def connect(self, address: Optional[str] = None):
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        if self.http_server is not None:
            logger.info("Stopping proxy server")
            await self.http_server.cleanup()
            self.http_server = None

        await super().disconnect(allow_autoreconnect)

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            try:
                self.slot_data = args["slot_data"]
                self.goal_number = self.slot_data["goal_number"]
                logger.info("Connected and slot_data initialized")
                self.http_task = asyncio.create_task(
                    run_http_server(self, self.http_port),
                    name="Nuclear Throne Proxy"
                    )
            except Exception as e:
                logger.info(f"Error starting proxy server: {e}")

        elif cmd == "ReceivedItems":
            if args["index"] == 0:
                self.awaiting_items.clear()
                self.full_inventory.clear()

            for item in args["items"]:
                item_obj = NetworkItem(*item).item
                self.awaiting_items.append(item_obj)
                self.full_inventory.append(item_obj)
                if item_obj >= 5000:
                    self.goal_complete += 1

        elif cmd == "Bounced":
            data = args.get("data", {})
            if "x" in data and "room" in data:
                if data["player"] != self.slot and data["player"] is not None:
                    self.deathlink_occurrence = True

    def run_gui(self):
        from kvui import GameManager

        class NTManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Nuclear Throne"

        self.ui = NTManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


def launch(*launch_args: str):
    async def main():
        parser = get_base_parser()
        args = parser.parse_args(launch_args)

        ctx = NuclearThroneContext(args.connect, args.password)

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()

    Utils.init_logging("NuclearThroneClient")

    import colorama
    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()


from aiohttp import web


def create_http_app(ctx: NuclearThroneContext):
    app = web.Application()

    async def root(request):
        return web.json_response({"status": "running"})

    async def initialize(request):
        if ctx.slot_data is None:
            return web.json_response({"error": "slot_data not initialized"}, status=503)

        ctx.slot_data["death_link"] = 1 if "DeathLink" in ctx.tags else 0
        return web.json_response(ctx.slot_data)

    async def allitems(request):
        if ctx.goal_complete >= ctx.goal_number and not ctx.finished_game:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True

        ctx.awaiting_items.clear()
        return web.json_response(ctx.full_inventory)

    async def getitems(request):
        if ctx.goal_complete >= ctx.goal_number and not ctx.finished_game:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True

        sending_items = deepcopy(ctx.awaiting_items)
        ctx.awaiting_items.clear()
        return web.json_response(sending_items)

    async def deathlink_get(request):
        trigger = ctx.deathlink_occurrence
        ctx.deathlink_occurrence = False
        return web.json_response(trigger)

    async def location(request):
        try:
            # Try JSON first
            try:
                data = await request.json()
                location_id = data.get("location_id")
            except:
                # Fallback: raw body
                body = (await request.text()).strip()
                location_id = int(body)

            if location_id is None:
                raise ValueError("Missing location_id")

            await ctx.check_locations([location_id])
            return web.json_response({"received": location_id})

        except Exception as e:
            logger.warning(f"/location error: {e}")
            return web.json_response({"error": "invalid request"}, status=400)
    
    async def deathlink_post(request):
        try:
            # Try JSON first
            try:
                data = await request.json()
                cause = data.get("cause")
            except:
                # Fallback: raw body
                cause = (await request.text()).strip()

            if not cause:
                raise ValueError("Missing cause")

            await ctx.send_death(f"{ctx.player_names[ctx.slot]} {cause}")
            return web.json_response({"received": cause})

        except Exception as e:
            logger.warning(f"/deathlink error: {e}")
            return web.json_response({"error": "invalid request"}, status=400)

    app.router.add_get("/", root)
    app.router.add_get("/initialize", initialize)
    app.router.add_get("/allitems", allitems)
    app.router.add_get("/getitems", getitems)
    app.router.add_get("/deathlink", deathlink_get)
    app.router.add_post("/location", location)
    app.router.add_post("/deathlink", deathlink_post)

    return app


async def run_http_server(ctx: NuclearThroneContext, local_port: int):
    app = create_http_app(ctx)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "localhost", local_port)
    await site.start()

    ctx.http_server = runner

    logger.info(f"Proxy server running")

    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        await runner.cleanup()