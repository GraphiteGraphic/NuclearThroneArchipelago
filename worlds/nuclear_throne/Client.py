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

    def _cmd_goal(self):
        """Displays the current goal number and completion status"""
        if isinstance(self.ctx, NuclearThroneContext):
            goal_lookup = { 99901: "FISH", 99902: "CRYSTAL", 99903: "EYES", 99904: "MELTING", 99905: "PLANT",
                            99906: "Y.V.", 99907: "STEROIDS", 99908: "ROBOT", 99909: "CHICKEN", 99910: "REBEL",
                            99911: "HORROR", 99912: "ROGUE", 99916: "CUZ" }
            self.output(f"Goals completed: {self.ctx.goal_complete}/{self.ctx.goal_number}")
            for check in self.ctx.checked_locations:
                   if check > 99900:
                        self.output(goal_lookup.get(check, f"Unknown goal {check}"))
    
    def _cmd_release_character(self, character: str):
        """Releases a character after completing their goal"""
        if isinstance(self.ctx, NuclearThroneContext):
            character_id_lookup = { "FISH": 1, "CRYSTAL": 2, "EYES": 3, "MELTING": 4, "PLANT": 5,
                                    "Y.V.": 6, "STEROIDS": 7, "ROBOT": 8, "CHICKEN": 9, "REBEL": 10,
                                    "HORROR": 11, "ROGUE": 12, "CUZ": 16 }
            character_lookup = { "FISH": {11001, 12001, 13001, 11002, 11003, 12003, 13003, 11004, 
                                          11005, 12005, 13005, 11006, 11007, 12007, 13007, 11000, 
                                          11100, 11101, 11102, 11103, 11104, 11105, 11106, 12106,
                                          13106, 7701, 7801, 
                                          102, 103, 104, 105, 106, 107, 
                                          108, 109, 110, 111, 112, 113},
                                "CRYSTAL": {21001, 22001, 23001, 21002, 21003, 22003, 23003, 21004, 
                                            21005, 22005, 23005, 21006, 21007, 22007, 23007, 21000, 
                                            21100, 21101, 21102, 21103, 21104, 21105, 21106, 22106, 
                                            23106, 7702, 7802, 
                                            202, 203, 204, 205, 206, 207, 
                                            208, 209, 210, 211, 212, 213},
                                "EYES": {31001, 32001, 33001, 31002, 31003, 32003, 33003, 31004, 
                                         31005, 32005, 33005, 31006, 31007, 32007, 33007, 31000, 
                                         31100, 31101, 31102, 31103, 31104, 31105, 31106, 32106,
                                         33106, 7703, 7803, 
                                         302, 303, 304, 305, 306, 307, 
                                         308, 309, 310, 311, 312, 313}, 
                                "MELTING": {41001, 42001, 43001, 41002, 41003, 42003, 43003, 41004, 
                                            41005, 42005, 43005, 41006, 41007, 42007, 43007, 41000, 
                                            41100, 41101, 41102, 41103, 41104, 41105, 41106, 42106, 
                                            43106, 7704, 7804, 
                                            402, 403, 404, 405, 406, 407, 
                                            408, 409, 410, 411, 412, 413}, 
                                "PLANT": {51001, 52001, 53001, 51002, 51003, 52003, 53003, 51004, 
                                          51005, 52005, 53005, 51006, 51007, 52007, 53007, 51000, 
                                          51100, 51101, 51102, 51103, 51104, 51105, 51106, 52106, 
                                          53106, 7705, 7805, 
                                          502, 503, 504, 505, 506, 507, 
                                          508, 509, 510, 511, 512, 513},
                                "Y.V.": {61001, 62001, 63001, 61002, 61003, 62003, 63003, 61004, 
                                         61005, 62005, 63005, 61006, 61007, 62007, 63007, 61000, 
                                         61100, 61101, 61102, 61103, 61104, 61105, 61106, 62106, 
                                         63106, 7706, 7806, 
                                         602, 603, 604, 605, 606, 607, 
                                         608, 609, 610, 611, 612, 613}, 
                                "STEROIDS": {71001, 72001, 73001, 71002, 71003, 72003, 73003, 71004, 
                                             71005, 72005, 73005, 71006, 71007, 72007, 73007, 71000, 
                                             71100, 71101, 71102, 71103, 71104, 71105, 71106, 72106, 
                                             73106, 7707, 7807, 
                                             702, 703, 704, 705, 706, 707, 
                                             708, 709, 710, 711, 712, 713},
                                "ROBOT": {81001, 82001, 83001, 81002, 81003, 82003, 83003, 81004, 
                                          81005, 82005, 83005, 81006, 81007, 82007, 83007, 81000, 
                                          81100, 81101, 81102, 81103, 81104, 81105, 81106, 82106, 
                                          83106, 7708, 7808, 
                                          802, 803, 804, 805, 806, 807, 
                                          808, 809, 810, 811, 812, 813},
                                "CHICKEN": {91001, 92001, 93001, 91002, 91003, 92003, 93003, 91004, 
                                            91005, 92005, 93005, 91006, 91007, 92007, 93007, 91000, 
                                            91100, 91101, 91102, 91103, 91104, 91105, 91106, 92106, 
                                            93106, 7709, 7809, 
                                            902, 903, 904, 905, 906, 907, 
                                            908, 909, 910, 911, 912, 913},
                                "REBEL": {101001, 102001, 103001, 101002, 101003, 102003, 103003, 101004, 
                                          101005, 102005, 103005, 101006, 101007, 102007, 103007, 101000, 
                                          101100, 101101, 101102, 101103, 101104, 101105, 101106, 102106, 
                                          103106, 7710, 7810, 
                                          1002, 1003, 1004, 1005, 1006, 1007, 
                                          1008, 1009, 1010, 1011, 1012, 1013},
                                "HORROR": {111001, 112001, 113001, 111002, 111003, 112003, 113003, 111004, 
                                           111005, 112005, 113005, 111006, 111007, 112007, 113007, 111000, 
                                           111100, 111101, 111102, 111103, 111104, 111105, 111106, 112106, 
                                           113106, 7711, 7811, 
                                           1102, 1103, 1104, 1105, 1106, 1107, 
                                           1108, 1109, 1110, 1111, 1112, 1113},
                                "ROGUE": {121001, 122001, 123001, 121002, 121003, 122003, 123003, 121004, 
                                          121005, 122005, 123005, 121006, 121007, 122007, 123007, 121000, 
                                          121100, 121101, 121102, 121103, 121104, 121105, 121106, 122106, 
                                          123106, 7712, 7812, 
                                          1202, 1203, 1204, 1205, 1206, 1207, 
                                          1208, 1209, 1210, 1211, 1212, 1213},
                                "CUZ": {161001, 162001, 163001, 161002,161003, 162003, 163003, 161004, 
                                        161005, 162005, 163005, 161006, 161007, 162007, 163007, 161000, 
                                        161100, 161101, 161102, 161103, 161104, 161105, 161106, 162106, 
                                        163106, 7716, 7816, 
                                        1602, 1603, 1604, 1605, 1606, 1607, 
                                        1608, 1609, 1610, 1611, 1612, 1613}
                                }
            character_id = character_id_lookup.get(character.upper())
            locations = character_lookup.get(character.upper()) if character_id is not None else None
            if locations is not None:
                if (99900 + character_id) in self.ctx.checked_locations:
                    self.output(f"Attempting to release {character}...")
                    asyncio.create_task(self.ctx.check_locations(list(locations)))
                else:
                    self.output(f"Cannot release {character} yet. Goal not completed.")
            else:
                self.output(f"Unknown character: {character}")

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