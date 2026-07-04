from BaseClasses import ItemClassification
from .items import NuclearThroneItem
from . import names, items
import typing, random

if typing.TYPE_CHECKING:
    from . import NuclearThroneWorld


def set_rules(world: "NuclearThroneWorld") -> None:

    if world.options.starting_weapon.value == -1:
        weps = [3,4,5,6,7,17,19,21,27]
        world.options.starting_weapon.value = weps[random.randint(0, 8)]
    elif world.options.starting_weapon.value == -2:
        excl_weps = [39,40,41,42,43,44,45,98,99,100,101,102,103,108,109,126,127]
        wep = random.randint(1, 128)
        while wep in excl_weps:
            wep = random.randint(1, 128)
        world.options.starting_weapon.value = wep
    
    if world.options.starting_secondary.value == -1:
        weps = [3,4,5,6,7,17,19,21,27]
        world.options.starting_secondary.value = weps[random.randint(0, 8)]
    elif world.options.starting_secondary.value == -2:
        excl_weps = [39,40,41,42,43,44,45,98,99,100,101,102,103,108,109,126,127]
        wep = random.randint(1, 128)
        while wep in excl_weps:
            wep = random.randint(1, 128)
        world.options.starting_secondary.value = wep
        
    for i in range(1,14):
        if i == 13:
            goal_location = world.multiworld.get_location(f"{names.char_cuz} - GOAL", world.player)
            goal_location.place_locked_item(NuclearThroneItem("VICTORY", 
                                                              ItemClassification.progression, 5000, world.player))
            world.set_rule(goal_location,
                lambda state, items=items.mutations_goal_list: state.has_from_list(items, world.player, 7))
        else:          
            goal_location = world.multiworld.get_location(f"{world.item_id_to_name[i]} - GOAL", world.player)
            goal_location.place_locked_item(NuclearThroneItem("VICTORY", ItemClassification.progression, 5000,
                                                               world.player))
            world.set_rule(goal_location,
                lambda state, items=items.mutations_goal_list: state.has_from_list(items, world.player, 7))
    
    if world.options.skinsanity.value:
        fish_bskin_loc = world.multiworld.get_location(f"{names.char_fish} - B SKIN", world.player)
        world.set_rule(fish_bskin_loc,
            lambda state, items=items.character_list: state.has_all(items, world.player))

        fish_cskin_loc = world.multiworld.get_location(f"{names.char_fish} - C SKIN", world.player)
        world.set_rule(fish_cskin_loc,
            lambda state, items=items.character_list: state.has_all(items, world.player))
        
        melting_bskin_loc = world.multiworld.get_location(f"{names.char_melting} - B SKIN", world.player)
        world.set_rule(melting_bskin_loc,
            lambda state, items=items.mutations_list: state.has_from_list(items, world.player, 12))
        
        melting_cskin_loc = world.multiworld.get_location(f"{names.char_melting} - C SKIN", world.player)
        world.set_rule(melting_cskin_loc,
            lambda state, items=items.mutations_list: state.has_from_list(items, world.player, 13))
                
        plant_cskin_loc = world.multiworld.get_location(f"{names.char_plant} - C SKIN", world.player)
        world.set_rule(plant_cskin_loc,
            lambda state, items=[names.wep_blood_cannon, names.wep_blood_hammer,
                                 names.wep_blood_launcher, names.mut_bloodlust]: \
                                 state.has_from_list(items, world.player, 2))

        yv_bskin_loc = world.multiworld.get_location(f"{names.char_yv} - B SKIN", world.player)
        world.set_rule(yv_bskin_loc,
            lambda state, items=[names.wep_golden_crossbow, names.wep_golden_machinegun,
                                 names.wep_golden_grenade_launcher, names.wep_golden_laser_pistol,
                                 names.wep_golden_shotgun, names.wep_golden_wrench]: \
                                 state.has_any(items, world.player))

        yv_cskin_loc = world.multiworld.get_location(f"{names.char_yv} - C SKIN", world.player)
        world.set_rule(yv_cskin_loc,
            lambda state, items=[names.char_cuz]: state.has_all(items, world.player))

        robot_bskin_loc = world.multiworld.get_location(f"{names.char_robot} - B SKIN", world.player)
        world.set_rule(robot_bskin_loc,
            lambda state, items=[names.wep_hyper_launcher, names.wep_hyper_rifle,
                                 names.wep_hyper_slugger]: state.has_any(items, world.player))

        chicken_cskin_loc = world.multiworld.get_location(f"{names.char_chicken} - C SKIN", world.player)
        world.set_rule(chicken_cskin_loc,
            lambda state, items=[names.wep_black_sword]: state.has_all(items, world.player))

        cuz_bskin_loc = world.multiworld.get_location(f"{names.char_cuz} - B SKIN", world.player)
        world.set_rule(cuz_bskin_loc,
            lambda state, items=[names.wep_golden_crossbow, names.wep_golden_machinegun,
                                 names.wep_golden_grenade_launcher, names.wep_golden_laser_pistol,
                                 names.wep_golden_shotgun, names.wep_golden_wrench]: \
                                 state.has_from_list(items, world.player, 3))
