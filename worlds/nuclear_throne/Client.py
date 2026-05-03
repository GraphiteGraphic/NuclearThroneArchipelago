import asyncio

import Utils
from copy import deepcopy
from typing import List, Any, Optional
from NetUtils import NetworkItem
from CommonClient import CommonContext, gui_enabled, ClientCommandProcessor, logger, get_base_parser, ClientStatus


class NuclearThroneCommandProcessor(ClientCommandProcessor):
    def _cmd_run_proxy(self):
        """Turn On Nuclear Throne Proxy HTTP Server"""
        try:
            logger.info("Starting Nuclear Throne proxy server")
            self.ctx.http_task = asyncio.create_task(
                run_http_server(self.ctx, self.ctx.http_port),
                name="Nuclear Throne Proxy"
            )
        except Exception as e:
            logger.info(f"Error starting proxy server: {e}")

    def _cmd_end_proxy(self):
        """Turn Off Nuclear Throne Proxy HTTP Server"""
        try:
            logger.info("Stopping Nuclear Throne proxy server")
            asyncio.create_task(self.ctx.http_server.cleanup())
            self.ctx.http_server = None
        except Exception as e:
            logger.info(f"Error stopping proxy server; {e}")

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
        self.full_inventory: List[Any] = []
        self.awaiting_items: List[Any] = []
        self.deathlink_occurrence = None
        self.slot_data = None
        self.goal_number = 1
        self.goal_complete = 0

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(NuclearThroneContext, self).server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    async def connect(self, address: Optional[str] = None):
        self.full_inventory.clear()
        self.awaiting_items.clear()
        self.deathlink_occurrence = None
        self.slot_data = None
        self.goal_number = 1
        self.goal_complete = 0
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        try:
            if self.http_server is not None:
                logger.info("Stopping proxy server")
                await self.http_server.cleanup()
                self.http_server = None
        except Exception as e:
            logger.info(f"Error stopping proxy server: {e}")

        self.full_inventory.clear()
        self.awaiting_items.clear()
        self.deathlink_occurrence = None
        self.slot_data = None
        self.goal_number = 1
        self.goal_complete = 0
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
            data = args.get("data", None)
            if data is not None and data["source"] != self.player_names[self.slot]:
                self.deathlink_occurrence = data["source"]

    async def vault_raider_check(self):
        fish_crowns = set([102,103,104,105,106,107,108,109,110,111,112,113])
        if fish_crowns.issubset(self.checked_locations):
            await self.check_locations([99901])
        
        crystal_crowns = set([202,203,204,205,206,207,208,209,210,211,212,213])
        if crystal_crowns.issubset(self.checked_locations):
            await self.check_locations([99902])
        
        eyes_crowns = set([302,303,304,305,306,307,308,309,310,311,312,313])
        if eyes_crowns.issubset(self.checked_locations):
            await self.check_locations([99903])
        
        melting_crowns = set([402,403,404,405,406,407,408,409,410,411,412,413])
        if melting_crowns.issubset(self.checked_locations):
            await self.check_locations([99904])
        
        plant_crowns = set([502,503,504,505,506,507,508,509,510,511,512,513])
        if plant_crowns.issubset(self.checked_locations):
            await self.check_locations([99905])
        
        yv_crowns = set([602,603,604,605,606,607,608,609,610,611,612,613])
        if yv_crowns.issubset(self.checked_locations):
            await self.check_locations([99906])
        
        steroids_crowns = set([702,703,704,705,706,707,708,709,710,711,712,713])
        if steroids_crowns.issubset(self.checked_locations):
            await self.check_locations([99907])
        
        robot_crowns = set([802,803,804,805,806,807,808,809,810,811,812,813])
        if robot_crowns.issubset(self.checked_locations):
            await self.check_locations([99908])
        
        chicken_crowns = set([902,903,904,905,906,907,908,909,910,911,912,913])
        if chicken_crowns.issubset(self.checked_locations):
            await self.check_locations([99909])
        
        rebel_crowns = set([1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013])
        if rebel_crowns.issubset(self.checked_locations):
            await self.check_locations([99910])
        
        horror_crowns = set([1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113])
        if horror_crowns.issubset(self.checked_locations):
            await self.check_locations([99911])
        
        rogue_crowns = set([1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213])
        if rogue_crowns.issubset(self.checked_locations):
            await self.check_locations([99912])
        
        cuz_crowns = set([1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613])
        if cuz_crowns.issubset(self.checked_locations):
            await self.check_locations([99916])

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
        ctx.deathlink_occurrence = None
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
                location_id = body

            if location_id is None:
                raise ValueError("Missing location_id")

            await ctx.check_locations([int(location_id)])
            if ctx.slot_data["goal"] == 5:
                await ctx.vault_raider_check()

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