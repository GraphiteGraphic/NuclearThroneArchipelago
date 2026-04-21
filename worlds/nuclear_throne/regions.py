from typing import Dict, Tuple

from BaseClasses import Region
from . import locations, names

class NuclearThroneRegion(Region):
    game = "Nuclear Throne"

nuclearthrone_runs: Dict[str, Tuple[Tuple[str, ...], Dict[str, int]]] = {
    names.char_fish:     ((names.char_fish,),     locations.fish_locations),
    names.char_crystal:  ((names.char_crystal,),  locations.crystal_locations),
    names.char_eyes:     ((names.char_eyes,),     locations.eyes_locations),
    names.char_melting:  ((names.char_melting,),  locations.melting_locations),
    names.char_plant:    ((names.char_plant,),    locations.plant_locations),
    names.char_yv:       ((names.char_yv,),       locations.yv_locations),
    names.char_steroids: ((names.char_steroids,), locations.steroids_locations),
    names.char_robot:    ((names.char_robot,),    locations.robot_locations),
    names.char_chicken:  ((names.char_chicken,),  locations.chicken_locations),
    names.char_rebel:    ((names.char_rebel,),    locations.rebel_locations),
    names.char_horror:   ((names.char_horror,),   locations.horror_locations),
    names.char_rogue:    ((names.char_rogue,),    locations.rogue_locations),
    names.char_cuz:      ((names.char_cuz,),      locations.cuz_locations)
}