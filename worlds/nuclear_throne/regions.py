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

crown_runs: Dict[str, Dict[str, int]] = {
    names.char_fish:     locations.crown_locations_fish,
    names.char_crystal:  locations.crown_locations_crystal,
    names.char_eyes:     locations.crown_locations_eyes,
    names.char_melting:  locations.crown_locations_melting,
    names.char_plant:    locations.crown_locations_plant,
    names.char_yv:       locations.crown_locations_yv,
    names.char_steroids: locations.crown_locations_steroids,
    names.char_robot:    locations.crown_locations_robot,
    names.char_chicken:  locations.crown_locations_chicken,
    names.char_rebel:    locations.crown_locations_rebel,
    names.char_horror:   locations.crown_locations_horror,
    names.char_rogue:    locations.crown_locations_rogue,
    names.char_cuz:      locations.crown_locations_cuz
}

skin_runs: Dict[str, Dict[str, int]] = {
    names.char_fish:     locations.skin_locations_fish,
    names.char_crystal:  locations.skin_locations_crystal,
    names.char_eyes:     locations.skin_locations_eyes,
    names.char_melting:  locations.skin_locations_melting,
    names.char_plant:    locations.skin_locations_plant,
    names.char_yv:       locations.skin_locations_yv,
    names.char_steroids: locations.skin_locations_steroids,
    names.char_robot:    locations.skin_locations_robot,
    names.char_chicken:  locations.skin_locations_chicken,
    names.char_rebel:    locations.skin_locations_rebel,
    names.char_horror:   locations.skin_locations_horror,
    names.char_rogue:    locations.skin_locations_rogue,
    names.char_cuz:      locations.skin_locations_cuz
}