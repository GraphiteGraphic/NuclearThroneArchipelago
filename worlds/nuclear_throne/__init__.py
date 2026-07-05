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
        "CROWNS - PRELOOP": {f"{names.char_fish} - CROWN OF LIFE",
                            f"{names.char_crystal} - CROWN OF LIFE",
                            f"{names.char_eyes} - CROWN OF LIFE",
                            f"{names.char_melting} - CROWN OF LIFE",
                            f"{names.char_plant} - CROWN OF LIFE",
                            f"{names.char_yv} - CROWN OF LIFE",
                            f"{names.char_steroids} - CROWN OF LIFE",
                            f"{names.char_robot} - CROWN OF LIFE",
                            f"{names.char_chicken} - CROWN OF LIFE",
                            f"{names.char_rebel} - CROWN OF LIFE",
                            f"{names.char_horror} - CROWN OF LIFE",
                            f"{names.char_rogue} - CROWN OF LIFE",
                            f"{names.char_cuz} - CROWN OF LIFE",
                            f"{names.char_fish} - CROWN OF GUNS",
                            f"{names.char_crystal} - CROWN OF GUNS",
                            f"{names.char_eyes} - CROWN OF GUNS",
                            f"{names.char_melting} - CROWN OF GUNS",
                            f"{names.char_plant} - CROWN OF GUNS",
                            f"{names.char_yv} - CROWN OF GUNS",
                            f"{names.char_steroids} - CROWN OF GUNS",
                            f"{names.char_robot} - CROWN OF GUNS",
                            f"{names.char_chicken} - CROWN OF GUNS",
                            f"{names.char_rebel} - CROWN OF GUNS",
                            f"{names.char_horror} - CROWN OF GUNS",
                            f"{names.char_rogue} - CROWN OF GUNS",
                            f"{names.char_cuz} - CROWN OF GUNS",
                            f"{names.char_fish} - CROWN OF HASTE",
                            f"{names.char_crystal} - CROWN OF HASTE",
                            f"{names.char_eyes} - CROWN OF HASTE",
                            f"{names.char_melting} - CROWN OF HASTE",
                            f"{names.char_plant} - CROWN OF HASTE",
                            f"{names.char_yv} - CROWN OF HASTE",
                            f"{names.char_steroids} - CROWN OF HASTE",
                            f"{names.char_robot} - CROWN OF HASTE",
                            f"{names.char_chicken} - CROWN OF HASTE",
                            f"{names.char_rebel} - CROWN OF HASTE",
                            f"{names.char_horror} - CROWN OF HASTE",
                            f"{names.char_rogue} - CROWN OF HASTE",
                            f"{names.char_cuz} - CROWN OF HASTE",
                            f"{names.char_fish} - CROWN OF DESTINY",
                            f"{names.char_crystal} - CROWN OF DESTINY",
                            f"{names.char_eyes} - CROWN OF DESTINY",
                            f"{names.char_melting} - CROWN OF DESTINY",
                            f"{names.char_plant} - CROWN OF DESTINY",
                            f"{names.char_yv} - CROWN OF DESTINY",
                            f"{names.char_steroids} - CROWN OF DESTINY",
                            f"{names.char_robot} - CROWN OF DESTINY",
                            f"{names.char_chicken} - CROWN OF DESTINY",
                            f"{names.char_rebel} - CROWN OF DESTINY",
                            f"{names.char_horror} - CROWN OF DESTINY",
                            f"{names.char_rogue} - CROWN OF DESTINY",
                            f"{names.char_cuz} - CROWN OF DESTINY",
                            f"{names.char_fish} - CROWN OF CURSES",
                            f"{names.char_crystal} - CROWN OF CURSES",
                            f"{names.char_eyes} - CROWN OF CURSES",
                            f"{names.char_melting} - CROWN OF CURSES",
                            f"{names.char_plant} - CROWN OF CURSES",
                            f"{names.char_yv} - CROWN OF CURSES",
                            f"{names.char_steroids} - CROWN OF CURSES",
                            f"{names.char_robot} - CROWN OF CURSES",
                            f"{names.char_chicken} - CROWN OF CURSES",
                            f"{names.char_rebel} - CROWN OF CURSES",
                            f"{names.char_horror} - CROWN OF CURSES",
                            f"{names.char_rogue} - CROWN OF CURSES",
                            f"{names.char_cuz} - CROWN OF CURSES",
                            f"{names.char_fish} - CROWN OF RISK",
                            f"{names.char_crystal} - CROWN OF RISK",
                            f"{names.char_eyes} - CROWN OF RISK",
                            f"{names.char_melting} - CROWN OF RISK",
                            f"{names.char_plant} - CROWN OF RISK",
                            f"{names.char_yv} - CROWN OF RISK",
                            f"{names.char_steroids} - CROWN OF RISK",
                            f"{names.char_robot} - CROWN OF RISK",
                            f"{names.char_chicken} - CROWN OF RISK",
                            f"{names.char_rebel} - CROWN OF RISK",
                            f"{names.char_horror} - CROWN OF RISK",
                            f"{names.char_rogue} - CROWN OF RISK",
                            f"{names.char_cuz} - CROWN OF RISK"},
         "CROWNS - POSTLOOP": {f"{names.char_fish} - CROWN OF DEATH",
                            f"{names.char_crystal} - CROWN OF DEATH",
                            f"{names.char_eyes} - CROWN OF DEATH",
                            f"{names.char_melting} - CROWN OF DEATH",
                            f"{names.char_plant} - CROWN OF DEATH",
                            f"{names.char_yv} - CROWN OF DEATH",
                            f"{names.char_steroids} - CROWN OF DEATH",
                            f"{names.char_robot} - CROWN OF DEATH",
                            f"{names.char_chicken} - CROWN OF DEATH",
                            f"{names.char_rebel} - CROWN OF DEATH",
                            f"{names.char_horror} - CROWN OF DEATH",
                            f"{names.char_rogue} - CROWN OF DEATH",
                            f"{names.char_cuz} - CROWN OF DEATH",
                            f"{names.char_fish} - CROWN OF BLOOD",
                            f"{names.char_crystal} - CROWN OF BLOOD",
                            f"{names.char_eyes} - CROWN OF BLOOD",
                            f"{names.char_melting} - CROWN OF BLOOD",
                            f"{names.char_plant} - CROWN OF BLOOD",
                            f"{names.char_yv} - CROWN OF BLOOD",
                            f"{names.char_steroids} - CROWN OF BLOOD",
                            f"{names.char_robot} - CROWN OF BLOOD",
                            f"{names.char_chicken} - CROWN OF BLOOD",
                            f"{names.char_rebel} - CROWN OF BLOOD",
                            f"{names.char_horror} - CROWN OF BLOOD",
                            f"{names.char_rogue} - CROWN OF BLOOD",
                            f"{names.char_cuz} - CROWN OF BLOOD",
                            f"{names.char_fish} - CROWN OF HATRED",
                            f"{names.char_crystal} - CROWN OF HATRED",
                            f"{names.char_eyes} - CROWN OF HATRED",
                            f"{names.char_melting} - CROWN OF HATRED",
                            f"{names.char_plant} - CROWN OF HATRED",
                            f"{names.char_yv} - CROWN OF HATRED",
                            f"{names.char_steroids} - CROWN OF HATRED",
                            f"{names.char_robot} - CROWN OF HATRED",
                            f"{names.char_chicken} - CROWN OF HATRED",
                            f"{names.char_rebel} - CROWN OF HATRED",
                            f"{names.char_horror} - CROWN OF HATRED",
                            f"{names.char_rogue} - CROWN OF HATRED",
                            f"{names.char_cuz} - CROWN OF HATRED",
                            f"{names.char_fish} - CROWN OF LOVE",
                            f"{names.char_crystal} - CROWN OF LOVE",
                            f"{names.char_eyes} - CROWN OF LOVE",
                            f"{names.char_melting} - CROWN OF LOVE",
                            f"{names.char_plant} - CROWN OF LOVE",
                            f"{names.char_yv} - CROWN OF LOVE",
                            f"{names.char_steroids} - CROWN OF LOVE",
                            f"{names.char_robot} - CROWN OF LOVE",
                            f"{names.char_chicken} - CROWN OF LOVE",
                            f"{names.char_rebel} - CROWN OF LOVE",
                            f"{names.char_horror} - CROWN OF LOVE",
                            f"{names.char_rogue} - CROWN OF LOVE",
                            f"{names.char_cuz} - CROWN OF LOVE",
                            f"{names.char_fish} - CROWN OF LUCK",
                            f"{names.char_crystal} - CROWN OF LUCK",
                            f"{names.char_eyes} - CROWN OF LUCK",
                            f"{names.char_melting} - CROWN OF LUCK",
                            f"{names.char_plant} - CROWN OF LUCK",
                            f"{names.char_yv} - CROWN OF LUCK",
                            f"{names.char_steroids} - CROWN OF LUCK",
                            f"{names.char_robot} - CROWN OF LUCK",
                            f"{names.char_chicken} - CROWN OF LUCK",
                            f"{names.char_rebel} - CROWN OF LUCK",
                            f"{names.char_horror} - CROWN OF LUCK",
                            f"{names.char_rogue} - CROWN OF LUCK",
                            f"{names.char_cuz} - CROWN OF LUCK",
                            f"{names.char_fish} - CROWN OF PROTECTION",
                            f"{names.char_crystal} - CROWN OF PROTECTION",
                            f"{names.char_eyes} - CROWN OF PROTECTION",
                            f"{names.char_melting} - CROWN OF PROTECTION",
                            f"{names.char_plant} - CROWN OF PROTECTION",
                            f"{names.char_yv} - CROWN OF PROTECTION",
                            f"{names.char_steroids} - CROWN OF PROTECTION",
                            f"{names.char_robot} - CROWN OF PROTECTION",
                            f"{names.char_chicken} - CROWN OF PROTECTION",
                            f"{names.char_rebel} - CROWN OF PROTECTION",
                            f"{names.char_horror} - CROWN OF PROTECTION",
                            f"{names.char_rogue} - CROWN OF PROTECTION",
                            f"{names.char_cuz} - CROWN OF PROTECTION"},
        "SKINS": locations.skin_location_table.keys(),
        "B SKINS": {f"{names.char_fish} - B SKIN",
                    f"{names.char_crystal} - B SKIN",
                    f"{names.char_eyes} - B SKIN",
                    f"{names.char_melting} - B SKIN",
                    f"{names.char_plant} - B SKIN",
                    f"{names.char_yv} - B SKIN",
                    f"{names.char_steroids} - B SKIN",
                    f"{names.char_robot} - B SKIN",
                    f"{names.char_chicken} - B SKIN",
                    f"{names.char_rebel} - B SKIN",
                    f"{names.char_horror} - B SKIN",
                    f"{names.char_rogue} - B SKIN",
                    f"{names.char_cuz} - B SKIN"},
        "C SKINS": {f"{names.char_fish} - C SKIN",
                    f"{names.char_crystal} - C SKIN",
                    f"{names.char_eyes} - C SKIN",
                    f"{names.char_melting} - C SKIN",
                    f"{names.char_plant} - C SKIN",
                    f"{names.char_yv} - C SKIN",
                    f"{names.char_steroids} - C SKIN",
                    f"{names.char_robot} - C SKIN",
                    f"{names.char_chicken} - C SKIN",
                    f"{names.char_rebel} - C SKIN",
                    f"{names.char_horror} - C SKIN",
                    f"{names.char_rogue} - C SKIN",
                    f"{names.char_cuz} - C SKIN"},
    }

    def create_regions(self) -> None:
        menu = NuclearThroneRegion("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)                

        if self.options.goal.value == 5:
            self.options.crownsanity.value = True

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
                    self.multiworld.get_region(f"{required_items[0]} - {names.desert_01}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.desert_03_locations:
                    lvl_fmt = {level : locations.desert_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.desert_02}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.sewers_locations:
                    lvl_fmt = {level : locations.sewers_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.desert_03}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 1))
                elif level in locations.scrapyard_01_locations:
                    lvl_fmt = {level : locations.scrapyard_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.sewers}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.weapons_tier_1: state.has_from_list(items, self.player, 7))
                elif level in locations.scrapyard_02_locations:
                    lvl_fmt = {level : locations.scrapyard_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.scrapyard_01}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.scrapyard_03_locations:
                    lvl_fmt = {level : locations.scrapyard_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.scrapyard_02}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.caves_locations:
                    lvl_fmt = {level : locations.caves_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.scrapyard_03}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 2))
                elif level in locations.frozencity_01_locations:
                    lvl_fmt = {level : locations.frozencity_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.caves}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.weapons_tier_2: state.has_from_list(items, self.player, 7))
                elif level in locations.frozencity_02_locations:
                    lvl_fmt = {level : locations.frozencity_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.frozencity_01}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.frozencity_03_locations:
                    lvl_fmt = {level : locations.frozencity_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.frozencity_02}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.labs_locations:
                    lvl_fmt = {level : locations.labs_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.frozencity_03}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 4))
                elif level in locations.palace_01_locations:
                    lvl_fmt = {level : locations.palace_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.labs}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.weapons_tier_3: state.has_from_list(items, self.player, 7))
                elif level in locations.palace_02_locations:
                    lvl_fmt = {level : locations.palace_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.palace_01}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.palace_03_locations:
                    lvl_fmt = {level : locations.palace_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.palace_02}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.weapons_tier_4: state.has_from_list(items, self.player, 7))
                    if self.options.goal.value == 0 or self.options.goal.value == 3:
                        goal_id = items.character_item_table[required_items[0]].index + 99900
                        goal_name = f"{required_items[0]} - GOAL"
                        region.add_locations({goal_name : goal_id}, NuclearThroneLocation)
                    if self.options.crownsanity.value:
                        region.add_locations(crown_runs[required_items[0]], NuclearThroneLocation)
                elif level in locations.campfire_locations:
                    lvl_fmt = {level : locations.campfire_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.palace_03}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 7))
                    if self.options.goal.value == 4 or self.options.goal.value == 5:
                        goal_id = items.character_item_table[required_items[0]].index + 99900
                        goal_name = f"{required_items[0]} - GOAL"
                        region.add_locations({goal_name : goal_id}, NuclearThroneLocation)
                    if self.options.skinsanity.value:
                        region.add_locations(skin_runs[required_items[0]], NuclearThroneLocation)
                elif level in locations.hq_01_locations:
                    lvl_fmt = {level : locations.hq_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.campfire}", 
                                               self.player).connect(region, f"To {level}",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 7))
                elif level in locations.hq_02_locations:
                    lvl_fmt = {level : locations.hq_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.hq_01}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.hq_03_locations:
                    lvl_fmt = {level : locations.hq_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.hq_02}", 
                                               self.player).connect(region, f"To {level}")
                    if self.options.goal.value == 1 or self.options.goal.value == 2:
                        goal_id = items.character_item_table[required_items[0]].index + 99900
                        goal_name = f"{required_items[0]} - GOAL"
                        region.add_locations({goal_name : goal_id}, NuclearThroneLocation)
                elif level in locations.oasis_locations:
                    lvl_fmt = {level : locations.oasis_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.desert_01}", self.player).connect(region,
                                    f"{required_items[0]} - Oasis Skip",
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
                    self.multiworld.get_region(f"{required_items[0]} - {names.sewers}", 
                                    self.player).connect(region, f"{required_items[0]} - Pizza Sewers Enter",
                                        lambda state, items=required_wep: state.has_any(items, self.player))
                elif level in locations.mansion_locations:
                    lvl_fmt = {level : locations.mansion_locations[level]}
                    required_wep = [names.wep_screwdriver]
                    anarchy_wep = [names.wep_golden_screwdriver, names.wep_energy_screwdriver]
                    if self.options.anarchy_mode.value:
                        required_wep.extend(anarchy_wep)
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.scrapyard_01}", 
                                    self.player).connect(region, f"{required_items[0]} - Mansion Enter", 
                                        lambda state, items=required_wep: state.has_any(items, self.player))
                elif level in locations.cursedcaves_locations:
                    lvl_fmt = {level : locations.cursedcaves_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.scrapyard_03}", 
                                    self.player).connect(region, f"{required_items[0]} - Cursed Cave Enter",
                        lambda state, items=items.mutations_goal_list: state.has_from_list(items, self.player, 2))
                elif level in locations.jungle_locations:
                    lvl_fmt = {level : locations.jungle_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.frozencity_01}",
                                    self.player).connect(region, f"{required_items[0]} - Jungle Enter")
                elif level in locations.vault_locations:
                    lvl_fmt = {level : locations.vault_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{required_items[0]} - {names.scrapyard_02}", 
                                    self.player).connect(region,  f"{required_items[0]} - ScrapVault Enter")
                    self.multiworld.get_region(f"{required_items[0]} - {names.frozencity_02}", 
                                    self.player).connect(region,   f"{required_items[0]} - CityVault Enter")
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
    