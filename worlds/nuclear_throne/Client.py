import asyncio

import Utils
from copy import deepcopy
from typing import List, Any, Optional
from NetUtils import NetworkItem
from CommonClient import CommonContext, gui_enabled, ClientCommandProcessor, logger, get_base_parser, ClientStatus

DEBUG = False

class NuclearThroneCommandProcessor(ClientCommandProcessor):
    def _cmd_run_proxy(self):
        """Turn On Nuclear Throne Proxy HTTP Server"""
        logger.info("Starting Nuclear Throne proxy server")
        
        self.ctx.http_task = asyncio.create_task(run_http_server(self.ctx, self.ctx.http_port),
                                                name="Nuclear Throne Proxy")

    def _cmd_end_proxy(self):
        """Turn Off Nuclear Throne Proxy HTTP Server"""
        if self.ctx.http_server != None:
            logger.info("Stopping Nuclear Throne proxy server")
            self.ctx.http_server.should_exit = True
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

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(NuclearThroneContext, self).server_auth(password_requested)

        await self.get_username()
        await self.send_connect()
    
    async def connect(self, address: Optional[str] = None):
        await super().connect(address)

    async def disconnect(self, allow_autoreconnect: bool = False):
        if self.http_server != None:
            logger.info("Stopping Nuclear Throne proxy server")
            self.http_server.should_exit = True
            self.http_server = None
        
        await super().disconnect(allow_autoreconnect)

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            try:
                self.slot_data = args["slot_data"]
                self.goal_number = self.slot_data["goal_number"]
                logger.info("Starting Nuclear Throne proxy server")
                self.http_task = asyncio.create_task(run_http_server(self, self.http_port),
                                                    name="Nuclear Throne Proxy")
            except:
                logger.info("Error has occurred starting the proxy server")
        elif cmd == "ReceivedItems":
            if args["index"] == 0:
                self.awaiting_items.clear()
                self.full_inventory.clear()

            for item in args["items"]:
                self.awaiting_items.append(NetworkItem(*item).item)
                self.full_inventory.append(NetworkItem(*item).item)
                if NetworkItem(*item).item >= 5000:
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

        if ctx.http_server != None:
            ctx.http_server.should_exit = True
        
        if ctx.http_task:
            await ctx.http_task


    Utils.init_logging("NuclearThroneClient")

    import colorama
    colorama.just_fix_windows_console()
    asyncio.run(main())
    colorama.deinit()


from fastapi import FastAPI
import uvicorn

def create_http_app(ctx: NuclearThroneContext):
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"status": "running"}
    
    @app.get("/initialize")
    async def getSetting():
        if "DeathLink" in ctx.tags:
            ctx.slot_data["death_link"] = 1
        else:
            ctx.slot_data["death_link"] = 0
        return ctx.slot_data

    @app.get("/allitems")
    async def getAllItems():
        if ctx.goal_complete >= ctx.goal_number and not ctx.finished_game:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True

        ctx.awaiting_items.clear()
        return ctx.full_inventory
    
    @app.get("/getitems")
    async def getItems():
        if ctx.goal_complete >= ctx.goal_number and not ctx.finished_game:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
    
        sending_items = deepcopy(ctx.awaiting_items)
        ctx.awaiting_items.clear()
        return sending_items

    @app.get("/deathlink")
    async def getLastDeathLink():
        trigger_death = ctx.deathlink_occurrence
        ctx.deathlink_occurrence = False
        return trigger_death

    @app.post("/location")
    async def sendLocationCheck(location_id: int):
        await ctx.check_locations([location_id])

        return {"received": location_id}

    @app.post("/deathlink")
    async def sendDeathLink(cause: str):
        await ctx.send_death(f"{ctx.player_names[ctx.slot]} {cause}")

        return {"received": cause}

    return app


async def run_http_server(ctx: NuclearThroneContext, local_port: int):
    app = create_http_app(ctx)

    config = uvicorn.Config(
        app,
        host="localhost",
        port=local_port,
        log_level="info",
        loop="asyncio"
    )
    server = uvicorn.Server(config)

    ctx.http_server = server

    await server.serve()