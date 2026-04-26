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
            goal_location = world.multiworld.get_location(f"GOAL - {names.char_cuz}", world.player)
            goal_location.place_locked_item(NuclearThroneItem("VICTORY", 
                                                              ItemClassification.progression, 5000, world.player))
            world.set_rule(goal_location,
                lambda state, items=items.mutations_goal_list: state.has_from_list(items, world.player, 7))

        else:          
            goal_location = world.multiworld.get_location(f"GOAL - {world.item_id_to_name[i]}",
                                                           world.player)
            goal_location.place_locked_item(NuclearThroneItem("VICTORY", ItemClassification.progression, 5000,
                                                               world.player))
            world.set_rule(goal_location,
                lambda state, items=items.mutations_goal_list: state.has_from_list(items, world.player, 7))
