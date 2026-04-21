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
    names.mut_rhino_skin:        ItemData(1001, False),
    names.mut_extra_feet:        ItemData(1002, False),
    names.mut_plutonium_hunger:  ItemData(1003, False),
    names.mut_rabbit_paw:        ItemData(1004, False),
    names.mut_throne_butt:       ItemData(1005, False, True),
    names.mut_lucky_shot:        ItemData(1006, False),
    names.mut_bloodlust:         ItemData(1007, False),
    names.mut_gamma_guts:        ItemData(1008, False),
    names.mut_second_stomach:    ItemData(1009, False),
    names.mut_back_muscle:       ItemData(1010, False, True),
    names.mut_scarier_face:      ItemData(1011, False, True),
    names.mut_euphoria:          ItemData(1012, False),
    names.mut_long_arms:         ItemData(1013, False, True),
    names.mut_boiling_veins:     ItemData(1014, False, True),
    names.mut_shotgun_shoulders: ItemData(1015, False),
    names.mut_recycle_gland:     ItemData(1016, False),
    names.mut_laser_brain:       ItemData(1017, False),
    names.mut_eagle_eyes:        ItemData(1019, False),
    names.mut_impact_wrists:     ItemData(1020, False),
    names.mut_bolt_marrow:       ItemData(1021, False),
    names.mut_stress:            ItemData(1022, False),
    names.mut_trigger_fingers:   ItemData(1023, False),
    names.mut_sharp_teeth:       ItemData(1024, False),
    names.mut_patience:          ItemData(1025, False),
    names.mut_hammerhead:        ItemData(1026, False),
    names.mut_strong_spirit:     ItemData(1027, False, True),
    names.mut_open_mind:         ItemData(1028, False, True),
    names.mut_heavy_heart:       ItemData(1029, False)
}

weapon_item_table = {
    names.wep_triple_machinegun:       ItemData(2002, False),
    names.wep_wrench:                  ItemData(2003, False),
    names.wep_machinegun:              ItemData(2004, False),
    names.wep_shotgun:                 ItemData(2005, False),
    names.wep_crossbow:                ItemData(2006, False),
    names.wep_grenade_launcher:        ItemData(2007, True),
    names.wep_double_shotgun:          ItemData(2008, False),
    names.wep_minigun:                 ItemData(2009, False),
    names.wep_auto_shotgun:            ItemData(2010, False),
    names.wep_auto_crossbow:           ItemData(2011, False),
    names.wep_super_crossbow:          ItemData(2012, False),
    names.wep_shovel:                  ItemData(2013, False),
    names.wep_bazooka:                 ItemData(2014, True),
    names.wep_sticky_launcher:         ItemData(2015, False),
    names.wep_smg:                     ItemData(2016, False),
    names.wep_assault_rifle:           ItemData(2017, False),
    names.wep_disc_gun:                ItemData(2018, False),
    names.wep_laser_pistol:            ItemData(2019, False),
    names.wep_laser_rifle:             ItemData(2020, False),
    names.wep_slugger:                 ItemData(2021, False),
    names.wep_gatling_slugger:         ItemData(2022, False),
    names.wep_assault_slugger:         ItemData(2023, False),
    names.wep_energy_sword:            ItemData(2024, False),
    names.wep_super_slugger:           ItemData(2025, False),
    names.wep_hyper_rifle:             ItemData(2026, False),
    names.wep_screwdriver:             ItemData(2027, True),
    names.wep_laser_minigun:           ItemData(2028, False),
    names.wep_blood_launcher:          ItemData(2029, False),
    names.wep_splinter_gun:            ItemData(2030, False),
    names.wep_toxic_bow:               ItemData(2031, False),
    names.wep_wave_gun:                ItemData(2033, False),
    names.wep_plasma_gun:              ItemData(2034, False),
    names.wep_plasma_cannon:           ItemData(2035, False),
    names.wep_energy_hammer:           ItemData(2036, False),
    names.wep_jackhammer:              ItemData(2037, False),
    names.wep_flak_cannon:             ItemData(2038, False),
    names.wep_golden_wrench:           ItemData(2040, False),
    names.wep_golden_machinegun:       ItemData(2041, False),
    names.wep_golden_shotgun:          ItemData(2042, False),
    names.wep_golden_crossbow:         ItemData(2043, False),
    names.wep_golden_grenade_launcher: ItemData(2044, False),
    names.wep_golden_laser_pistol:     ItemData(2045, False),
    names.wep_nuke_launcher:           ItemData(2047, False),
    names.wep_quadruple_machinegun:    ItemData(2049, False),
    names.wep_flamethrower:            ItemData(2050, False),
    names.wep_dragon:                  ItemData(2051, False),
    names.wep_flare_gun:               ItemData(2052, False),
    names.wep_energy_screwdriver:      ItemData(2053, False),
    names.wep_hyper_launcher:          ItemData(2054, False),
    names.wep_laser_cannon:            ItemData(2055, False),
    names.wep_lightning_pistol:        ItemData(2057, False),
    names.wep_lightning_rifle:         ItemData(2058, False),
    names.wep_lightning_shotgun:       ItemData(2059, False),
    names.wep_super_flak_cannon:       ItemData(2060, False),
    names.wep_sawed_off_shotgun:       ItemData(2061, False),
    names.wep_splinter_pistol:         ItemData(2062, False),
    names.wep_super_splinter_gun:      ItemData(2063, False),
    names.wep_lightning_smg:           ItemData(2064, False),
    names.wep_smart_gun:               ItemData(2065, False),
    names.wep_heavy_crossbow:          ItemData(2066, False),
    names.wep_blood_hammer:            ItemData(2067, False),
    names.wep_lightning_cannon:        ItemData(2068, False),
    names.wep_pop_gun:                 ItemData(2069, False),
    names.wep_plasma_rifle:            ItemData(2070, False),
    names.wep_pop_rifle:               ItemData(2071, False),
    names.wep_toxic_launcher:          ItemData(2072, True),
    names.wep_flame_cannon:            ItemData(2073, False),
    names.wep_lightning_hammer:        ItemData(2074, False),
    names.wep_flame_shotgun:           ItemData(2075, False),
    names.wep_double_flame_shotgun:    ItemData(2076, False),
    names.wep_auto_flame_shotgun:      ItemData(2077, False),
    names.wep_cluster_launcher:        ItemData(2078, False),
    names.wep_grenade_shotgun:         ItemData(2079, False),
    names.wep_grenade_rifle:           ItemData(2080, False),
    names.wep_double_minigun:          ItemData(2083, False),
    names.wep_gatling_bazooka:         ItemData(2084, False),
    names.wep_auto_grenade_shotgun:    ItemData(2085, False),
    names.wep_ultra_revolver:          ItemData(2086, False),
    names.wep_ultra_laser_pistol:      ItemData(2087, False),
    names.wep_sledgehammer:            ItemData(2088, False),
    names.wep_heavy_revolver:          ItemData(2089, False),
    names.wep_heavy_machinegun:        ItemData(2090, False),
    names.wep_heavy_slugger:           ItemData(2091, False),
    names.wep_ultra_shovel:            ItemData(2092, False),
    names.wep_ultra_shotgun:           ItemData(2093, False),
    names.wep_ultra_crossbow:          ItemData(2094, False),
    names.wep_ultra_grenade_launcher:  ItemData(2095, False),
    names.wep_plasma_minigun:          ItemData(2096, False),
    names.wep_devastator:              ItemData(2097, False),
    names.wep_golden_plasma_gun:       ItemData(2098, False),
    names.wep_golden_slugger:          ItemData(2099, False),
    names.wep_golden_splinter_gun:     ItemData(2100, False),
    names.wep_golden_screwdriver:      ItemData(2101, False),
    names.wep_golden_bazooka:          ItemData(2102, False),
    names.wep_golden_assault_rifle:    ItemData(2103, False),
    names.wep_super_disc_gun:          ItemData(2104, False),
    names.wep_heavy_auto_crossbow:     ItemData(2105, False),
    names.wep_heavy_assault_rifle:     ItemData(2106, False),
    names.wep_blood_cannon:            ItemData(2107, False),
    names.wep_incinerator:             ItemData(2110, False),
    names.wep_super_plasma_cannon:     ItemData(2111, False),
    names.wep_seeker_pistol:           ItemData(2112, False),
    names.wep_seeker_shotgun:          ItemData(2113, False),
    names.wep_eraser:                  ItemData(2114, False),
    names.wep_guitar:                  ItemData(2115, False),
    names.wep_bouncer_smg:             ItemData(2116, False),
    names.wep_bouncer_shotgun:         ItemData(2117, False),
    names.wep_hyper_slugger:           ItemData(2118, False),
    names.wep_super_bazooka:           ItemData(2119, False),
    names.wep_black_sword:             ItemData(2121, False),
    names.wep_golden_nuke_launcher:    ItemData(2122, False),
    names.wep_golden_disc_gun:         ItemData(2123, False),
    names.wep_heavy_grenade_launcher:  ItemData(2124, False),
    names.wep_gun_gun:                 ItemData(2125, False)
}

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
