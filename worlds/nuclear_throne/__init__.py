import logging
from worlds.AutoWorld import World
from BaseClasses import ItemClassification

from . import items, locations, rules, web_world, names
from .locations import NuclearThroneLocation
from .regions import NuclearThroneRegion, nuclearthrone_runs, crown_runs, skin_runs
from . import options as nuclearthrone_options
from typing import Dict, Any
import math
from worlds.LauncherComponents import Component, components, icon_paths, launch as launch_component, Type


def launch_client(*args: str):
    from .Client import launch
    launch_component(launch, name="NuclearThroneClient", args=args)


components.append(Component("Nuclear Throne Client", "NuclearThroneClient", func=launch_client,
                            component_type=Type.CLIENT, icon='nticon'))

icon_paths['nticon'] = f"ap:{__name__}/nticon.png"


logger = logging.getLogger("Nuclear Throne")

class NuclearThroneWorld(World):
    """
    Nuclear Throne is a post-apocalyptic roguelike-like top-down shooter.
    Not 'the final hope of humanity' post-apocalyptic, but 'humanity is extinct and mutants 
    and monsters now roam the world' post-apocalyptic. Can you reach the Nuclear Throne?
    """

    game = "Nuclear Throne"
    web = web_world.NuclearThroneWebWorld()
    
    options_dataclass = nuclearthrone_options.NuclearThroneOptions
    options: nuclearthrone_options.NuclearThroneOptions
    
    item_name_to_id = items.lookup_item_to_id
    location_name_to_id = locations.lookup_location_to_id
    item_name_groups = items.item_names
    location_name_groups = {
        "FISH": locations.fish_locations.keys()
                | locations.crown_locations_fish.keys()
                | locations.skin_locations_fish.keys(),
        "CRYSTAL": locations.crystal_locations.keys()
                | locations.crown_locations_crystal.keys()
                | locations.skin_locations_crystal.keys(),
        "EYES": locations.eyes_locations.keys()
                | locations.crown_locations_eyes.keys()
                | locations.skin_locations_eyes.keys(),
        "MELTING": locations.melting_locations.keys()
                | locations.crown_locations_melting.keys()
                | locations.skin_locations_melting.keys(),
        "PLANT": locations.plant_locations.keys()
                | locations.crown_locations_plant.keys()
                | locations.skin_locations_plant.keys(),
        "Y.V.": locations.yv_locations.keys()
                | locations.crown_locations_yv.keys()
                | locations.skin_locations_yv.keys(),
        "STEROIDS": locations.steroids_locations.keys()
                | locations.crown_locations_steroids.keys()
                | locations.skin_locations_steroids.keys(),
        "ROBOT": locations.robot_locations.keys()
                | locations.crown_locations_robot.keys()
                | locations.skin_locations_robot.keys(),
        "CHICKEN": locations.chicken_locations.keys()
                | locations.crown_locations_chicken.keys()
                | locations.skin_locations_chicken.keys(),
        "REBEL": locations.rebel_locations.keys()
                | locations.crown_locations_rebel.keys()
                | locations.skin_locations_rebel.keys(),
        "HORROR": locations.horror_locations.keys()
                | locations.crown_locations_horror.keys()
                | locations.skin_locations_horror.keys(),
        "ROGUE": locations.rogue_locations.keys()
                | locations.crown_locations_rogue.keys()
                | locations.skin_locations_rogue.keys(),
        "CUZ": locations.cuz_locations.keys()
                | locations.crown_locations_cuz.keys()
                | locations.skin_locations_cuz.keys(),
        "DESERT": locations.desert_01_locations.keys()
                | locations.desert_02_locations.keys() 
                | locations.desert_03_locations.keys(),
        "SEWERS": locations.sewers_locations.keys(),
        "SCRAPYARD": locations.scrapyard_01_locations.keys() 
                | locations.scrapyard_02_locations.keys() 
                | locations.scrapyard_03_locations.keys(),
        "CAVES": locations.caves_locations.keys(),
        "FROZEN CITY": locations.frozencity_01_locations.keys() 
                | locations.frozencity_02_locations.keys() 
                | locations.frozencity_03_locations.keys(),
        "LABS": locations.labs_locations.keys(),
        "PALACE": locations.palace_01_locations.keys() 
                | locations.palace_02_locations.keys() 
                | locations.palace_03_locations.keys(),
        "CAMPFIRE": locations.campfire_locations.keys(),
        "HQ": locations.hq_01_locations.keys() 
                | locations.hq_02_locations.keys() 
                | locations.hq_03_locations.keys(),
        "OASIS": locations.oasis_locations.keys(),
        "PIZZA SEWERS": locations.pizzasewers_locations.keys(),
        "Y.V. MANSION": locations.mansion_locations.keys(),
        "CURSED CAVES": locations.cursedcaves_locations.keys(),
        "JUNGLE": locations.jungle_locations.keys(),
        "CROWN VAULT": locations.vault_locations.keys(),
        "CROWNS": locations.crown_location_table.keys(),
        "CROWNS - FISH": locations.crown_locations_fish.keys(),
        "CROWNS - CRYSTAL": locations.crown_locations_crystal.keys(),
        "CROWNS - EYES": locations.crown_locations_eyes.keys(),
        "CROWNS - MELTING": locations.crown_locations_melting.keys(),
        "CROWNS - PLANT": locations.crown_locations_plant.keys(),
        "CROWNS - Y.V.": locations.crown_locations_yv.keys(),
        "CROWNS - STEROIDS": locations.crown_locations_steroids.keys(),
        "CROWNS - ROBOT": locations.crown_locations_robot.keys(),
        "CROWNS - CHICKEN": locations.crown_locations_chicken.keys(),
        "CROWNS - REBEL": locations.crown_locations_rebel.keys(),
        "CROWNS - HORROR": locations.crown_locations_horror.keys(),
        "CROWNS - ROGUE": locations.crown_locations_rogue.keys(),
        "CROWNS - CUZ": locations.crown_locations_cuz.keys(),
        "CROWNS - PRELOOP": {f"CROWN OF LIFE - {names.char_fish}",
                            f"CROWN OF LIFE - {names.char_crystal}",
                            f"CROWN OF LIFE - {names.char_eyes}",
                            f"CROWN OF LIFE - {names.char_melting}",
                            f"CROWN OF LIFE - {names.char_plant}",
                            f"CROWN OF LIFE - {names.char_yv}",
                            f"CROWN OF LIFE - {names.char_steroids}",
                            f"CROWN OF LIFE - {names.char_robot}",
                            f"CROWN OF LIFE - {names.char_chicken}",
                            f"CROWN OF LIFE - {names.char_rebel}",
                            f"CROWN OF LIFE - {names.char_horror}",
                            f"CROWN OF LIFE - {names.char_rogue}",
                            f"CROWN OF LIFE - {names.char_cuz}",
                            f"CROWN OF GUNS - {names.char_fish}",
                            f"CROWN OF GUNS - {names.char_crystal}",
                            f"CROWN OF GUNS - {names.char_eyes}",
                            f"CROWN OF GUNS - {names.char_melting}",
                            f"CROWN OF GUNS - {names.char_plant}",
                            f"CROWN OF GUNS - {names.char_yv}",
                            f"CROWN OF GUNS - {names.char_steroids}",
                            f"CROWN OF GUNS - {names.char_robot}",
                            f"CROWN OF GUNS - {names.char_chicken}",
                            f"CROWN OF GUNS - {names.char_rebel}",
                            f"CROWN OF GUNS - {names.char_horror}",
                            f"CROWN OF GUNS - {names.char_rogue}",
                            f"CROWN OF GUNS - {names.char_cuz}",
                            f"CROWN OF HASTE - {names.char_fish}",
                            f"CROWN OF HASTE - {names.char_crystal}",
                            f"CROWN OF HASTE - {names.char_eyes}",
                            f"CROWN OF HASTE - {names.char_melting}",
                            f"CROWN OF HASTE - {names.char_plant}",
                            f"CROWN OF HASTE - {names.char_yv}",
                            f"CROWN OF HASTE - {names.char_steroids}",
                            f"CROWN OF HASTE - {names.char_robot}",
                            f"CROWN OF HASTE - {names.char_chicken}",
                            f"CROWN OF HASTE - {names.char_rebel}",
                            f"CROWN OF HASTE - {names.char_horror}",
                            f"CROWN OF HASTE - {names.char_rogue}",
                            f"CROWN OF HASTE - {names.char_cuz}",
                            f"CROWN OF DESTINY - {names.char_fish}",
                            f"CROWN OF DESTINY - {names.char_crystal}",
                            f"CROWN OF DESTINY - {names.char_eyes}",
                            f"CROWN OF DESTINY - {names.char_melting}",
                            f"CROWN OF DESTINY - {names.char_plant}",
                            f"CROWN OF DESTINY - {names.char_yv}",
                            f"CROWN OF DESTINY - {names.char_steroids}",
                            f"CROWN OF DESTINY - {names.char_robot}",
                            f"CROWN OF DESTINY - {names.char_chicken}",
                            f"CROWN OF DESTINY - {names.char_rebel}",
                            f"CROWN OF DESTINY - {names.char_horror}",
                            f"CROWN OF DESTINY - {names.char_rogue}",
                            f"CROWN OF DESTINY - {names.char_cuz}",
                            f"CROWN OF CURSES - {names.char_fish}",
                            f"CROWN OF CURSES - {names.char_crystal}",
                            f"CROWN OF CURSES - {names.char_eyes}",
                            f"CROWN OF CURSES - {names.char_melting}",
                            f"CROWN OF CURSES - {names.char_plant}",
                            f"CROWN OF CURSES - {names.char_yv}",
                            f"CROWN OF CURSES - {names.char_steroids}",
                            f"CROWN OF CURSES - {names.char_robot}",
                            f"CROWN OF CURSES - {names.char_chicken}",
                            f"CROWN OF CURSES - {names.char_rebel}",
                            f"CROWN OF CURSES - {names.char_horror}",
                            f"CROWN OF CURSES - {names.char_rogue}",
                            f"CROWN OF CURSES - {names.char_cuz}",
                            f"CROWN OF RISK - {names.char_fish}",
                            f"CROWN OF RISK - {names.char_crystal}",
                            f"CROWN OF RISK - {names.char_eyes}",
                            f"CROWN OF RISK - {names.char_melting}",
                            f"CROWN OF RISK - {names.char_plant}",
                            f"CROWN OF RISK - {names.char_yv}",
                            f"CROWN OF RISK - {names.char_steroids}",
                            f"CROWN OF RISK - {names.char_robot}",
                            f"CROWN OF RISK - {names.char_chicken}",
                            f"CROWN OF RISK - {names.char_rebel}",
                            f"CROWN OF RISK - {names.char_horror}",
                            f"CROWN OF RISK - {names.char_rogue}",
                            f"CROWN OF RISK - {names.char_cuz}"},
        "CROWNS - POSTLOOP": {f"CROWN OF DEATH - {names.char_fish}",
                            f"CROWN OF DEATH - {names.char_crystal}",
                            f"CROWN OF DEATH - {names.char_eyes}",
                            f"CROWN OF DEATH - {names.char_melting}",
                            f"CROWN OF DEATH - {names.char_plant}",
                            f"CROWN OF DEATH - {names.char_yv}",
                            f"CROWN OF DEATH - {names.char_steroids}",
                            f"CROWN OF DEATH - {names.char_robot}",
                            f"CROWN OF DEATH - {names.char_chicken}",
                            f"CROWN OF DEATH - {names.char_rebel}",
                            f"CROWN OF DEATH - {names.char_horror}",
                            f"CROWN OF DEATH - {names.char_rogue}",
                            f"CROWN OF DEATH - {names.char_cuz}",
                            f"CROWN OF BLOOD - {names.char_fish}",
                            f"CROWN OF BLOOD - {names.char_crystal}",
                            f"CROWN OF BLOOD - {names.char_eyes}",
                            f"CROWN OF BLOOD - {names.char_melting}",
                            f"CROWN OF BLOOD - {names.char_plant}",
                            f"CROWN OF BLOOD - {names.char_yv}",
                            f"CROWN OF BLOOD - {names.char_steroids}",
                            f"CROWN OF BLOOD - {names.char_robot}",
                            f"CROWN OF BLOOD - {names.char_chicken}",
                            f"CROWN OF BLOOD - {names.char_rebel}",
                            f"CROWN OF BLOOD - {names.char_horror}",
                            f"CROWN OF BLOOD - {names.char_rogue}",
                            f"CROWN OF BLOOD - {names.char_cuz}",
                            f"CROWN OF HATRED - {names.char_fish}",
                            f"CROWN OF HATRED - {names.char_crystal}",
                            f"CROWN OF HATRED - {names.char_eyes}",
                            f"CROWN OF HATRED - {names.char_melting}",
                            f"CROWN OF HATRED - {names.char_plant}",
                            f"CROWN OF HATRED - {names.char_yv}",
                            f"CROWN OF HATRED - {names.char_steroids}",
                            f"CROWN OF HATRED - {names.char_robot}",
                            f"CROWN OF HATRED - {names.char_chicken}",
                            f"CROWN OF HATRED - {names.char_rebel}",
                            f"CROWN OF HATRED - {names.char_horror}",
                            f"CROWN OF HATRED - {names.char_rogue}",
                            f"CROWN OF HATRED - {names.char_cuz}",
                            f"CROWN OF LOVE - {names.char_fish}",
                            f"CROWN OF LOVE - {names.char_crystal}",
                            f"CROWN OF LOVE - {names.char_eyes}",
                            f"CROWN OF LOVE - {names.char_melting}",
                            f"CROWN OF LOVE - {names.char_plant}",
                            f"CROWN OF LOVE - {names.char_yv}",
                            f"CROWN OF LOVE - {names.char_steroids}",
                            f"CROWN OF LOVE - {names.char_robot}",
                            f"CROWN OF LOVE - {names.char_chicken}",
                            f"CROWN OF LOVE - {names.char_rebel}",
                            f"CROWN OF LOVE - {names.char_horror}",
                            f"CROWN OF LOVE - {names.char_rogue}",
                            f"CROWN OF LOVE - {names.char_cuz}",
                            f"CROWN OF LUCK - {names.char_fish}",
                            f"CROWN OF LUCK - {names.char_crystal}",
                            f"CROWN OF LUCK - {names.char_eyes}",
                            f"CROWN OF LUCK - {names.char_melting}",
                            f"CROWN OF LUCK - {names.char_plant}",
                            f"CROWN OF LUCK - {names.char_yv}",
                            f"CROWN OF LUCK - {names.char_steroids}",
                            f"CROWN OF LUCK - {names.char_robot}",
                            f"CROWN OF LUCK - {names.char_chicken}",
                            f"CROWN OF LUCK - {names.char_rebel}",
                            f"CROWN OF LUCK - {names.char_horror}",
                            f"CROWN OF LUCK - {names.char_rogue}",
                            f"CROWN OF LUCK - {names.char_cuz}",
                            f"CROWN OF PROTECTION - {names.char_fish}",
                            f"CROWN OF PROTECTION - {names.char_crystal}",
                            f"CROWN OF PROTECTION - {names.char_eyes}",
                            f"CROWN OF PROTECTION - {names.char_melting}",
                            f"CROWN OF PROTECTION - {names.char_plant}",
                            f"CROWN OF PROTECTION - {names.char_yv}",
                            f"CROWN OF PROTECTION - {names.char_steroids}",
                            f"CROWN OF PROTECTION - {names.char_robot}",
                            f"CROWN OF PROTECTION - {names.char_chicken}",
                            f"CROWN OF PROTECTION - {names.char_rebel}",
                            f"CROWN OF PROTECTION - {names.char_horror}",
                            f"CROWN OF PROTECTION - {names.char_rogue}",
                            f"CROWN OF PROTECTION - {names.char_cuz}"},
        "SKINS": locations.skin_location_table.keys(),
        "B SKINS": {f"B SKIN - {names.char_fish}",
                    f"B SKIN - {names.char_crystal}",
                    f"B SKIN - {names.char_eyes}",
                    f"B SKIN - {names.char_melting}",
                    f"B SKIN - {names.char_plant}",
                    f"B SKIN - {names.char_yv}",
                    f"B SKIN - {names.char_steroids}",
                    f"B SKIN - {names.char_robot}",
                    f"B SKIN - {names.char_chicken}",
                    f"B SKIN - {names.char_rebel}",
                    f"B SKIN - {names.char_horror}",
                    f"B SKIN - {names.char_rogue}",
                    f"B SKIN - {names.char_cuz}"},
        "C SKINS": {f"C SKIN - {names.char_fish}",
                    f"C SKIN - {names.char_crystal}",
                    f"C SKIN - {names.char_eyes}",
                    f"C SKIN - {names.char_melting}",
                    f"C SKIN - {names.char_plant}",
                    f"C SKIN - {names.char_yv}",
                    f"C SKIN - {names.char_steroids}",
                    f"C SKIN - {names.char_robot}",
                    f"C SKIN - {names.char_chicken}",
                    f"C SKIN - {names.char_rebel}",
                    f"C SKIN - {names.char_horror}",
                    f"C SKIN - {names.char_rogue}",
                    f"C SKIN - {names.char_cuz}"},
    }

    def create_regions(self) -> None:
        menu = NuclearThroneRegion("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)                

        if self.options.goal.value == 5:
            self.options.crownsanity.value = True
        if self.options.skinsanity.value:
            self.options.starting_weapon.value = 0
            self.options.starting_secondary.value = 0

        for char_run in nuclearthrone_runs:
            required_items = nuclearthrone_runs[char_run][0]
            run_locations = nuclearthrone_runs[char_run][1]
            for level in run_locations:
                region = NuclearThroneRegion(level, self.player, self.multiworld)
                if level in locations.desert_01_locations:
                    lvl_fmt = {level : locations.desert_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    menu.connect(region, f"To {level}",
                        lambda state, items=required_items: state.has_all(items, self.player))
                elif level in locations.desert_02_locations:
                    lvl_fmt = {level : locations.desert_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.desert_01} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.desert_03_locations:
                    lvl_fmt = {level : locations.desert_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.desert_02} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.sewers_locations:
                    lvl_fmt = {level : locations.sewers_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.desert_03} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 1))
                elif level in locations.scrapyard_01_locations:
                    lvl_fmt = {level : locations.scrapyard_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.sewers} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.weapons_tier_1: state.has_from_list(items, self.player, 7))
                elif level in locations.scrapyard_02_locations:
                    lvl_fmt = {level : locations.scrapyard_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.scrapyard_01} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.scrapyard_03_locations:
                    lvl_fmt = {level : locations.scrapyard_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.scrapyard_02} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.caves_locations:
                    lvl_fmt = {level : locations.caves_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.scrapyard_03} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 2))
                elif level in locations.frozencity_01_locations:
                    lvl_fmt = {level : locations.frozencity_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.caves} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.weapons_tier_2: state.has_from_list(items, self.player, 7))
                elif level in locations.frozencity_02_locations:
                    lvl_fmt = {level : locations.frozencity_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.frozencity_01} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.frozencity_03_locations:
                    lvl_fmt = {level : locations.frozencity_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.frozencity_02} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.labs_locations:
                    lvl_fmt = {level : locations.labs_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.frozencity_03} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 4))
                elif level in locations.palace_01_locations:
                    lvl_fmt = {level : locations.palace_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.labs} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.weapons_tier_3: state.has_from_list(items, self.player, 7))
                elif level in locations.palace_02_locations:
                    lvl_fmt = {level : locations.palace_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.palace_01} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.palace_03_locations:
                    lvl_fmt = {level : locations.palace_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.palace_02} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.weapons_tier_4: state.has_from_list(items, self.player, 7))
                    if self.options.goal.value == 0 or self.options.goal.value == 3:
                        goal_id = items.character_item_table[required_items[0]].index + 99900
                        goal_name = f"GOAL - {required_items[0]}"
                        region.add_locations({goal_name : goal_id}, NuclearThroneLocation)
                    if self.options.crownsanity.value:
                        region.add_locations(crown_runs[required_items[0]], NuclearThroneLocation)
                elif level in locations.campfire_locations:
                    lvl_fmt = {level : locations.campfire_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.palace_03} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 7))
                    if self.options.goal.value == 4 or self.options.goal.value == 5:
                        goal_id = items.character_item_table[required_items[0]].index + 99900
                        goal_name = f"GOAL - {required_items[0]}"
                        region.add_locations({goal_name : goal_id}, NuclearThroneLocation)
                    if self.options.skinsanity.value:
                        region.add_locations(skin_runs[required_items[0]], NuclearThroneLocation)
                elif level in locations.hq_01_locations:
                    lvl_fmt = {level : locations.hq_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.campfire} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 7))
                elif level in locations.hq_02_locations:
                    lvl_fmt = {level : locations.hq_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.hq_01} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.hq_03_locations:
                    lvl_fmt = {level : locations.hq_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.hq_02} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                    if self.options.goal.value == 1 or self.options.goal.value == 2:
                        goal_id = items.character_item_table[required_items[0]].index + 99900
                        goal_name = f"GOAL - {required_items[0]}"
                        region.add_locations({goal_name : goal_id}, NuclearThroneLocation)
                elif level in locations.oasis_locations:
                    lvl_fmt = {level : locations.oasis_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.desert_01} - {required_items[0]}", self.player).connect(region,
                                    f"Oasis Skip - {required_items[0]}",
                        lambda state, items=items.weapons_tier_1: state.has_from_list(items, self.player, 7))
                elif level in locations.pizzasewers_locations:
                    lvl_fmt = {level : locations.pizzasewers_locations[level]}
                    required_wep = [names.wep_grenade_launcher, names.wep_bazooka, names.wep_toxic_launcher]
                    anarchy_wep = [names.wep_hyper_launcher, names.wep_heavy_grenade_launcher,
                                   names.wep_grenade_rifle, names.wep_grenade_shotgun,
                                   names.wep_auto_grenade_shotgun, names.wep_cluster_launcher,
                                   names.wep_gatling_bazooka, names.wep_super_bazooka,
                                   names.wep_nuke_launcher, names.wep_sticky_launcher]
                    if self.options.anarchy_mode.value:
                        required_wep.extend(anarchy_wep)
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.sewers} - {required_items[0]}", 
                                    self.player).connect(region, f"Pizza Sewers Enter - {required_items[0]}",
                                        lambda state, items=required_wep: state.has_any(items, self.player))
                elif level in locations.mansion_locations:
                    lvl_fmt = {level : locations.mansion_locations[level]}
                    required_wep = [names.wep_screwdriver]
                    anarchy_wep = [names.wep_golden_screwdriver, names.wep_energy_screwdriver]
                    if self.options.anarchy_mode.value:
                        required_wep.extend(anarchy_wep)
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.scrapyard_01} - {required_items[0]}", 
                                    self.player).connect(region, f"Mansion Enter - {required_items[0]}", 
                                        lambda state, items=required_wep: state.has_any(items, self.player))
                elif level in locations.cursedcaves_locations:
                    lvl_fmt = {level : locations.cursedcaves_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.scrapyard_03} - {required_items[0]}", 
                                    self.player).connect(region, f"Cursed Cave Enter - {required_items[0]}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 2))
                elif level in locations.jungle_locations:
                    lvl_fmt = {level : locations.jungle_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.frozencity_01} - {required_items[0]}",
                                    self.player).connect(region, f"Jungle Enter - {required_items[0]}")
                elif level in locations.vault_locations:
                    lvl_fmt = {level : locations.vault_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.scrapyard_02} - {required_items[0]}", 
                                    self.player).connect(region,  f"ScrapVault Enter - {required_items[0]}")
                    self.multiworld.get_region(f"{names.frozencity_02} - {required_items[0]}", 
                                    self.player).connect(region,   f"CityVault Enter - {required_items[0]}")
                self.multiworld.regions.append(region)         

    def set_rules(self) -> None:
        rules.set_rules(self)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("VICTORY", self.player,
                                                                                     self.options.goal_number.value)

    def create_items(self) -> None:
        itempool = []

        # set starting character        
        if self.options.starting_character.value == 0: # default: fish and crystal
                self.multiworld.push_precollected(self.create_item(self.item_id_to_name[1]))
                self.multiworld.push_precollected(self.create_item(self.item_id_to_name[2]))
                itempool.extend([self.create_item(name) for name in items.character_item_table
                                 if name != names.char_fish and name != names.char_crystal])
        else:
            start_char = self.item_id_to_name[self.options.starting_character.value]
            self.multiworld.push_precollected(self.create_item(start_char))
            itempool.extend([self.create_item(name) for name in items.character_item_table if name != start_char])
        
        itempool.extend([self.create_item(name) for name in items.mutations_item_table])
        itempool.extend([self.create_item(name) for name in items.weapon_item_table])

        filler_items = len(locations.location_table) - len(itempool)
        if self.options.crownsanity:
            filler_items += len(locations.crown_location_table)
        if self.options.skinsanity:
            filler_items += len(locations.skin_location_table)
        trap_amount = math.floor(filler_items * (self.options.trap_percentage / 100.0))

        filler_items -= trap_amount
        itempool.extend([self.create_item(self.get_filler_item_name())
                         for _ in range(filler_items)])
        itempool.extend([self.create_item(self.get_trap_item_name())
                         for _ in range(trap_amount)])
        self.multiworld.itempool += itempool

    def create_item(self, name: str) -> items.NuclearThroneItem:
        item = items.item_table[name]
        classification = ItemClassification.filler
        if item.progression:
            classification = ItemClassification.progression_skip_balancing \
                if item.skip_balancing else ItemClassification.progression
        if item.useful:
            classification |= ItemClassification.useful
        if self.options.anarchy_mode.value:
            anarchy_wep = [names.wep_hyper_launcher, names.wep_heavy_grenade_launcher,
                           names.wep_grenade_rifle, names.wep_grenade_shotgun,
                           names.wep_auto_grenade_shotgun, names.wep_cluster_launcher,
                           names.wep_gatling_bazooka, names.wep_super_bazooka,
                           names.wep_nuke_launcher, names.wep_sticky_launcher,
                           names.wep_golden_screwdriver, names.wep_energy_screwdriver]
            if name in anarchy_wep:
                classification = ItemClassification.progression_skip_balancing \
                    if item.skip_balancing else ItemClassification.progression
        if self.options.skinsanity.value:
            req_items = [names.wep_black_sword,names.mut_second_stomach
                        ,names.mut_bloodlust,names.mut_gamma_guts
                        ,names.mut_long_arms,names.mut_laser_brain
                        ,names.mut_recycle_gland,names.mut_shotgun_shoulders
                        ,names.mut_impact_wrists,names.mut_bolt_marrow]
            if name in req_items:
                classification = ItemClassification.progression_skip_balancing \
                    if item.skip_balancing else ItemClassification.progression

        if item.trap:
            classification = ItemClassification.trap

        return items.NuclearThroneItem(name, classification, item.index, self.player)
    
    def get_filler_item_name(self) -> str:
        return self.random.choices(list(items.filler_item_weights.keys()),
                                   weights=list(items.filler_item_weights.values()))[0]
    
    def get_trap_item_name(self) -> str:
        return self.random.choices(list(items.trap_item_table.keys()),
                                   weights=[self.options.bigdog_trap_weight.value,
                                            self.options.curse_trap_weight.value,
                                            self.options.drop_trap_weight.value,
                                            self.options.frog_trap_weight.value,
                                            self.options.horror_trap_weight.value,
                                            self.options.maggot_trap_weight.value,
                                            self.options.popo_trap_weight.value,
                                            self.options.skeleton_trap_weight.value,
                                            self.options.tmnt_trap_weight.value,
                                            self.options.eat_trap_weight.value,
                                            self.options.slow_trap_weight.value,
                                            self.options.speed_trap_weight.value,
                                            self.options.rusty_trap_weight.value,
                                            self.options.accuracy_trap_weight.value,
                                            self.options.low_hp_trap_weight.value,
                                            self.options.crown_trap_weight.value,
                                            self.options.empty_clip_trap_weight.value,
                                            self.options.nuke_trap_weight.value,
                                            self.options.car_trap_weight.value,
                                            self.options.dark_trap_weight.value])[0]
    
    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict("starting_character", "starting_weapon", "starting_secondary", "skinsanity",
                                    "goal", "goal_number", "endurance_number", "anarchy_mode", "crownsanity")
    