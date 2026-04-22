import logging
from worlds.AutoWorld import World
from BaseClasses import ItemClassification

from . import items, locations, rules, web_world, names
from .locations import NuclearThroneLocation
from .regions import NuclearThroneRegion, nuclearthrone_runs
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

    def create_regions(self) -> None:
        menu = NuclearThroneRegion("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)                

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
                                               self.player).connect(region, f"To {level}")
                elif level in locations.scrapyard_01_locations:
                    lvl_fmt = {level : locations.scrapyard_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.sewers} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
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
                                               self.player).connect(region, f"To {level}")
                elif level in locations.frozencity_01_locations:
                    lvl_fmt = {level : locations.frozencity_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.caves} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
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
                                               self.player).connect(region, f"To {level}")
                elif level in locations.palace_01_locations:
                    lvl_fmt = {level : locations.palace_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.labs} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.palace_02_locations:
                    lvl_fmt = {level : locations.palace_02_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.palace_01} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                elif level in locations.palace_03_locations:
                    lvl_fmt = {level : locations.palace_03_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.palace_02} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                    if self.options.goal.value == 0 or self.options.goal.value == 3:
                        goal_id = items.character_item_table[required_items[0]].index + 99900
                        goal_name = f"GOAL - {required_items[0]}"
                        region.add_locations({goal_name : goal_id}, NuclearThroneLocation)
                elif level in locations.campfire_locations:
                    lvl_fmt = {level : locations.campfire_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.palace_03} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
                    if self.options.goal.value == 4:
                        goal_id = items.character_item_table[required_items[0]].index + 99900
                        goal_name = f"GOAL - {required_items[0]}"
                        region.add_locations({goal_name : goal_id}, NuclearThroneLocation)
                elif level in locations.hq_01_locations:
                    lvl_fmt = {level : locations.hq_01_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.campfire} - {required_items[0]}", 
                                               self.player).connect(region, f"To {level}")
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
                                    f"Oasis Skip - {required_items[0]}")
                    region.connect(self.multiworld.get_region(f"{names.desert_03} - {required_items[0]}", self.player),
                                    f"Oasis Leave - {required_items[0]}")
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
                    region.connect(self.multiworld.get_region(f"{names.scrapyard_01} - {required_items[0]}",
                                    self.player), f"Pizza Sewers Leave - {required_items[0]}")
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
                    region.connect(self.multiworld.get_region(f"{names.scrapyard_03} - {required_items[0]}",
                                    self.player), f"Mansion Leave - {required_items[0]}")
                elif level in locations.cursedcaves_locations:
                    lvl_fmt = {level : locations.cursedcaves_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.scrapyard_03} - {required_items[0]}", 
                                    self.player).connect(region, f"Cursed Cave Enter - {required_items[0]}")
                    region.connect(self.multiworld.get_region(f"{names.frozencity_01} - {required_items[0]}",
                                    self.player), f"Cursed Cave Leave - {required_items[0]}")
                elif level in locations.jungle_locations:
                    lvl_fmt = {level : locations.jungle_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.frozencity_01} - {required_items[0]}",
                                    self.player).connect(region, f"Jungle Enter - {required_items[0]}")
                    region.connect(self.multiworld.get_region(f"{names.frozencity_03} - {required_items[0]}", 
                                    self.player), f"Jungle Leave - {required_items[0]}")
                elif level in locations.vault_locations:
                    lvl_fmt = {level : locations.vault_locations[level]}
                    region.add_locations(lvl_fmt, NuclearThroneLocation)
                    self.multiworld.get_region(f"{names.desert_02} - {required_items[0]}", 
                                    self.player).connect(region, f"DesertVault Enter - {required_items[0]}")
                    region.connect(self.multiworld.get_region(f"{names.desert_03} - {required_items[0]}", 
                                    self.player), f"DesertVault Leave - {required_items[0]}")
                    self.multiworld.get_region(f"{names.scrapyard_02} - {required_items[0]}", 
                                    self.player).connect(region,  f"ScrapVault Enter - {required_items[0]}")
                    region.connect(self.multiworld.get_region(f"{names.scrapyard_03} - {required_items[0]}", 
                                    self.player),  f"ScrapVault Leave - {required_items[0]}")
                    self.multiworld.get_region(f"{names.frozencity_02} - {required_items[0]}", 
                                    self.player).connect(region,   f"CityVault Enter - {required_items[0]}")
                    region.connect(self.multiworld.get_region(f"{names.frozencity_03} - {required_items[0]}",
                                    self.player),   f"CityVault Leave - {required_items[0]}")
                    self.multiworld.get_region(f"{names.palace_02} - {required_items[0]}", 
                                    self.player).connect(region, f"PalaceVault Enter - {required_items[0]}")
                    region.connect(self.multiworld.get_region(f"{names.palace_03} - {required_items[0]}",
                                    self.player), f"PalaceVault Leave - {required_items[0]}")
                self.multiworld.regions.append(region)         

    def set_rules(self) -> None:
        rules.set_rules(self)
        self.set_completion_rule(lambda state: state.has("VICTORY", self.player, self.options.goal_number.value))

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
                                            self.options.car_trap_weight.value])[0]
    
    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict("starting_character", "starting_weapon",
                                    "starting_secondary", "goal", "endurance_number", "anarchy_mode")
    