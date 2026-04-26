from BaseClasses import Item
from typing import NamedTuple, Dict
from . import names


class ItemData(NamedTuple):
    index: int
    progression: bool
    useful: bool = False  # primarily use this for incredibly useful items
    skip_balancing: bool = False
    trap: bool = False


class NuclearThroneItem(Item):
    game = "Nuclear Throne"


character_item_table = {
    names.char_fish:     ItemData(1, True),
    names.char_crystal:  ItemData(2, True),
    names.char_eyes:     ItemData(3, True),
    names.char_melting:  ItemData(4, True),
    names.char_plant:    ItemData(5, True),
    names.char_yv:       ItemData(6, True),
    names.char_steroids: ItemData(7, True),
    names.char_robot:    ItemData(8, True),
    names.char_chicken:  ItemData(9, True),
    names.char_rebel:    ItemData(10, True),
    names.char_horror:   ItemData(11, True),
    names.char_rogue:    ItemData(12, True),
    names.char_cuz:      ItemData(16, True),
}

mutations_item_table = {
    names.mut_rhino_skin:        ItemData(1001, True),
    names.mut_extra_feet:        ItemData(1002, False),
    names.mut_plutonium_hunger:  ItemData(1003, True),
    names.mut_rabbit_paw:        ItemData(1004, False, True),
    names.mut_throne_butt:       ItemData(1005, True),
    names.mut_lucky_shot:        ItemData(1006, False),
    names.mut_bloodlust:         ItemData(1007, False, True),
    names.mut_gamma_guts:        ItemData(1008, False, True),
    names.mut_second_stomach:    ItemData(1009, False, True),
    names.mut_back_muscle:       ItemData(1010, True),
    names.mut_scarier_face:      ItemData(1011, True),
    names.mut_euphoria:          ItemData(1012, True),
    names.mut_long_arms:         ItemData(1013, False, True),
    names.mut_boiling_veins:     ItemData(1014, True),
    names.mut_shotgun_shoulders: ItemData(1015, False, True),
    names.mut_recycle_gland:     ItemData(1016, False, True),
    names.mut_laser_brain:       ItemData(1017, False, True),
    names.mut_eagle_eyes:        ItemData(1019, False),
    names.mut_impact_wrists:     ItemData(1020, False, True),
    names.mut_bolt_marrow:       ItemData(1021, False, True),
    names.mut_stress:            ItemData(1022, True),
    names.mut_trigger_fingers:   ItemData(1023, True),
    names.mut_sharp_teeth:       ItemData(1024, False),
    names.mut_patience:          ItemData(1025, False),
    names.mut_hammerhead:        ItemData(1026, False),
    names.mut_strong_spirit:     ItemData(1027, True),
    names.mut_open_mind:         ItemData(1028, False),
    names.mut_heavy_heart:       ItemData(1029, False)
}

mutations_goal_list = [
    names.mut_rhino_skin,
    names.mut_plutonium_hunger,
    names.mut_throne_butt,      
    names.mut_back_muscle,   
    names.mut_scarier_face,
    names.mut_euphoria,
    names.mut_boiling_veins,    
    names.mut_stress,           
    names.mut_trigger_fingers,  
    names.mut_strong_spirit
]

weapon_item_table = {
    names.wep_triple_machinegun:       ItemData(2002, True),
    names.wep_wrench:                  ItemData(2003, True),
    names.wep_machinegun:              ItemData(2004, True),
    names.wep_shotgun:                 ItemData(2005, True),
    names.wep_crossbow:                ItemData(2006, True),
    names.wep_grenade_launcher:        ItemData(2007, True),
    names.wep_double_shotgun:          ItemData(2008, True),
    names.wep_minigun:                 ItemData(2009, True),
    names.wep_auto_shotgun:            ItemData(2010, True),
    names.wep_auto_crossbow:           ItemData(2011, True),
    names.wep_super_crossbow:          ItemData(2012, True),
    names.wep_shovel:                  ItemData(2013, True),
    names.wep_bazooka:                 ItemData(2014, True),
    names.wep_sticky_launcher:         ItemData(2015, True),
    names.wep_smg:                     ItemData(2016, True),
    names.wep_assault_rifle:           ItemData(2017, True),
    names.wep_disc_gun:                ItemData(2018, False),
    names.wep_laser_pistol:            ItemData(2019, True),
    names.wep_laser_rifle:             ItemData(2020, True),
    names.wep_slugger:                 ItemData(2021, True),
    names.wep_gatling_slugger:         ItemData(2022, True),
    names.wep_assault_slugger:         ItemData(2023, True),
    names.wep_energy_sword:            ItemData(2024, True),
    names.wep_super_slugger:           ItemData(2025, True),
    names.wep_hyper_rifle:             ItemData(2026, True),
    names.wep_screwdriver:             ItemData(2027, True),
    names.wep_laser_minigun:           ItemData(2028, True),
    names.wep_blood_launcher:          ItemData(2029, True),
    names.wep_splinter_gun:            ItemData(2030, True),
    names.wep_toxic_bow:               ItemData(2031, False),
    names.wep_wave_gun:                ItemData(2033, True),
    names.wep_plasma_gun:              ItemData(2034, True),
    names.wep_plasma_cannon:           ItemData(2035, True),
    names.wep_energy_hammer:           ItemData(2036, True),
    names.wep_jackhammer:              ItemData(2037, True),
    names.wep_flak_cannon:             ItemData(2038, True),
    names.wep_golden_wrench:           ItemData(2040, True),
    names.wep_golden_machinegun:       ItemData(2041, True),
    names.wep_golden_shotgun:          ItemData(2042, True),
    names.wep_golden_crossbow:         ItemData(2043, True),
    names.wep_golden_grenade_launcher: ItemData(2044, True),
    names.wep_golden_laser_pistol:     ItemData(2045, True),
    names.wep_nuke_launcher:           ItemData(2047, True),
    names.wep_quadruple_machinegun:    ItemData(2049, True),
    names.wep_flamethrower:            ItemData(2050, False),
    names.wep_dragon:                  ItemData(2051, True),
    names.wep_flare_gun:               ItemData(2052, True),
    names.wep_energy_screwdriver:      ItemData(2053, True),
    names.wep_hyper_launcher:          ItemData(2054, True),
    names.wep_laser_cannon:            ItemData(2055, True),
    names.wep_lightning_pistol:        ItemData(2057, True),
    names.wep_lightning_rifle:         ItemData(2058, True),
    names.wep_lightning_shotgun:       ItemData(2059, True),
    names.wep_super_flak_cannon:       ItemData(2060, True),
    names.wep_sawed_off_shotgun:       ItemData(2061, True),
    names.wep_splinter_pistol:         ItemData(2062, True),
    names.wep_super_splinter_gun:      ItemData(2063, True),
    names.wep_lightning_smg:           ItemData(2064, True),
    names.wep_smart_gun:               ItemData(2065, True),
    names.wep_heavy_crossbow:          ItemData(2066, True),
    names.wep_blood_hammer:            ItemData(2067, False),
    names.wep_lightning_cannon:        ItemData(2068, True),
    names.wep_pop_gun:                 ItemData(2069, True),
    names.wep_plasma_rifle:            ItemData(2070, True),
    names.wep_pop_rifle:               ItemData(2071, True),
    names.wep_toxic_launcher:          ItemData(2072, False, True),
    names.wep_flame_cannon:            ItemData(2073, True),
    names.wep_lightning_hammer:        ItemData(2074, True),
    names.wep_flame_shotgun:           ItemData(2075, True),
    names.wep_double_flame_shotgun:    ItemData(2076, True),
    names.wep_auto_flame_shotgun:      ItemData(2077, True),
    names.wep_cluster_launcher:        ItemData(2078, True),
    names.wep_grenade_shotgun:         ItemData(2079, True),
    names.wep_grenade_rifle:           ItemData(2080, True),
    names.wep_double_minigun:          ItemData(2083, True),
    names.wep_gatling_bazooka:         ItemData(2084, True),
    names.wep_auto_grenade_shotgun:    ItemData(2085, True),
    names.wep_ultra_revolver:          ItemData(2086, False, True),
    names.wep_ultra_laser_pistol:      ItemData(2087, False, True),
    names.wep_sledgehammer:            ItemData(2088, True),
    names.wep_heavy_revolver:          ItemData(2089, True),
    names.wep_heavy_machinegun:        ItemData(2090, True),
    names.wep_heavy_slugger:           ItemData(2091, True),
    names.wep_ultra_shovel:            ItemData(2092, False, True),
    names.wep_ultra_shotgun:           ItemData(2093, False, True),
    names.wep_ultra_crossbow:          ItemData(2094, False, True),
    names.wep_ultra_grenade_launcher:  ItemData(2095, False, True),
    names.wep_plasma_minigun:          ItemData(2096, True),
    names.wep_devastator:              ItemData(2097, True),
    names.wep_golden_plasma_gun:       ItemData(2098, False),
    names.wep_golden_slugger:          ItemData(2099, False),
    names.wep_golden_splinter_gun:     ItemData(2100, False),
    names.wep_golden_screwdriver:      ItemData(2101, False),
    names.wep_golden_bazooka:          ItemData(2102, False),
    names.wep_golden_assault_rifle:    ItemData(2103, False),
    names.wep_super_disc_gun:          ItemData(2104, False),
    names.wep_heavy_auto_crossbow:     ItemData(2105, True),
    names.wep_heavy_assault_rifle:     ItemData(2106, True),
    names.wep_blood_cannon:            ItemData(2107, True),
    names.wep_incinerator:             ItemData(2110, True),
    names.wep_super_plasma_cannon:     ItemData(2111, True),
    names.wep_seeker_pistol:           ItemData(2112, True),
    names.wep_seeker_shotgun:          ItemData(2113, True),
    names.wep_eraser:                  ItemData(2114, True),
    names.wep_guitar:                  ItemData(2115, False, True),
    names.wep_bouncer_smg:             ItemData(2116, True),
    names.wep_bouncer_shotgun:         ItemData(2117, True),
    names.wep_hyper_slugger:           ItemData(2118, True),
    names.wep_super_bazooka:           ItemData(2119, True),
    names.wep_black_sword:             ItemData(2121, False, True),
    names.wep_golden_nuke_launcher:    ItemData(2122, False),
    names.wep_golden_disc_gun:         ItemData(2123, False),
    names.wep_heavy_grenade_launcher:  ItemData(2124, True),
    names.wep_gun_gun:                 ItemData(2125, False)
}

weapons_tier_1 = [
    names.wep_machinegun,
    names.wep_assault_rifle,
    names.wep_shotgun,
    names.wep_slugger,
    names.wep_crossbow,
    names.wep_grenade_launcher,
    names.wep_laser_pistol,
    names.wep_screwdriver,
    names.wep_wrench,
    names.wep_smg,
    names.wep_pop_gun,
    names.wep_disc_gun,
    names.wep_triple_machinegun,
    names.wep_pop_rifle,
    names.wep_shovel,
    names.wep_sledgehammer,
    names.wep_flame_shotgun,
    names.wep_double_shotgun,
    names.wep_assault_slugger,
    names.wep_toxic_bow,
    names.wep_heavy_crossbow,
    names.wep_splinter_gun,
    names.wep_toxic_launcher,
    names.wep_bazooka,
    names.wep_flamethrower,
    names.wep_laser_rifle,
    names.wep_plasma_gun,
    names.wep_jackhammer
]

weapons_tier_2 = [
    names.wep_minigun,
    names.wep_bouncer_shotgun,
    names.wep_bouncer_smg,
    names.wep_sawed_off_shotgun,
    names.wep_auto_shotgun,
    names.wep_flak_cannon,
    names.wep_splinter_pistol,
    names.wep_flare_gun,
    names.wep_lightning_pistol,
    names.wep_double_flame_shotgun,
    names.wep_auto_crossbow,
    names.wep_seeker_pistol,
    names.wep_sticky_launcher,
    names.wep_grenade_shotgun,
    names.wep_cluster_launcher,
    names.wep_laser_cannon,
    names.wep_hyper_rifle,
    names.wep_eraser,
    names.wep_super_crossbow,
    names.wep_splinter_gun,
    names.wep_heavy_grenade_launcher,
    names.wep_plasma_rifle,
    names.wep_lightning_rifle,
    names.wep_heavy_revolver,
    names.wep_gatling_slugger,
    names.wep_seeker_shotgun,
    names.wep_grenade_rifle,
    names.wep_laser_minigun,
    names.wep_lightning_shotgun,
    names.wep_energy_screwdriver
]

weapons_tier_3 = [
    names.wep_smart_gun,
    names.wep_heavy_machinegun,
    names.wep_wave_gun,
    names.wep_heavy_slugger,
    names.wep_super_slugger,
    names.wep_auto_flame_shotgun,
    names.wep_nuke_launcher,
    names.wep_blood_launcher,
    names.wep_blood_hammer,
    names.wep_energy_sword,
    names.wep_energy_hammer,
    names.wep_super_bazooka,
    names.wep_plasma_cannon,
    names.wep_lightning_hammer,
    names.wep_quadruple_machinegun,
    names.wep_super_flak_cannon,
    names.wep_gatling_bazooka,
    names.wep_blood_cannon,
    names.wep_heavy_assault_rifle,
    names.wep_dragon,
    names.wep_flame_cannon,
    names.wep_lightning_smg,
    names.wep_lightning_cannon
]

weapons_sphere_4 = [
    names.wep_double_minigun,
    names.wep_hyper_launcher,
    names.wep_auto_grenade_shotgun,
    names.wep_hyper_slugger,
    names.wep_plasma_minigun,
    names.wep_incinerator,
    names.wep_heavy_auto_crossbow,
    names.wep_super_plasma_cannon,
    names.wep_devastator
]

filler_item_table = {
    names.junk: ItemData(3000, False),
}

trap_item_table = {
    names.trap_bigdog:     ItemData(3001, False, trap=True),
    names.trap_curse:      ItemData(3002, False, trap=True),
    names.trap_drop:       ItemData(3003, False, trap=True),
    names.trap_frog:       ItemData(3004, False, trap=True),
    names.trap_horror:     ItemData(3005, False, trap=True),
    names.trap_maggot:     ItemData(3006, False, trap=True),
    names.trap_popo:       ItemData(3007, False, trap=True),
    names.trap_skeleton:   ItemData(3008, False, trap=True),
    names.trap_tmnt:       ItemData(3009, False, trap=True),
    names.trap_eat:        ItemData(3010, False, trap=True),
    names.trap_slow:       ItemData(3011, False, trap=True),
    names.trap_speed:      ItemData(3012, False, trap=True),
    names.trap_rusty:      ItemData(3013, False, trap=True),
    names.trap_accuracy:   ItemData(3014, False, trap=True),
    names.trap_low_hp:     ItemData(3015, False, trap=True),
    names.trap_crown:      ItemData(3016, False, trap=True),
    names.trap_empty_clip: ItemData(3017, False, trap=True),
    names.trap_nuke:       ItemData(3018, False, trap=True),
    names.trap_car_wreck:  ItemData(3019, False, trap=True),
}

filler_item_weights = {
    names.junk: 1
}

item_table = {
    **character_item_table,
    **weapon_item_table,
    **mutations_item_table,
    **filler_item_table,
    **trap_item_table
}

item_lookup_table = {
    **character_item_table,
    **weapon_item_table,
    **mutations_item_table,
    **filler_item_table,
    **trap_item_table,
    "VICTORY": ItemData(5000, True)
}

item_names = {
    "Weapons": {name for name in weapon_item_table.keys()},
    "Characters": {name for name in character_item_table.keys()},
    "Mutations": {name for name in mutations_item_table.keys()}
}

lookup_item_to_id: Dict[str, int] = {item_name: data.index for item_name, data in item_lookup_table.items()}
