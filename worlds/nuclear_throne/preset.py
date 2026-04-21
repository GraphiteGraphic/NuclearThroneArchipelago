from typing import Dict, Any

beginner = {
    "death_link": False,
    "goal": "throne",
    "starting_character": "default",
    "goal_number": 1,
    "anarchy_mode": True,
    "trap_percentage": 0,
}

random = {
    "death_link": False,
    "goal": "random",
    "starting_character": "random",
    "starting_weapon": "random-balanced",
    "starting_secondary": "random",
    "goal_number": "random",
    "anarchy_mode": True,
    "trap_percentage": "random",
    "drop_trap_weight": "random",
    "eat_trap_weight": "random",
    "curse_trap_weight": "random",
    "bigdog_trap_weight": "random",
    "frog_trap_weight": "random",
    "horror_trap_weight": "random",
    "maggot_trap_weight": "random",
    "popo_trap_weight": "random",
    "skeleton_trap_weight": "random",
    "tmnt_trap_weight": "random",
    "slow_trap_weight": "random",
    "speed_trap_weight": "random",
    "rusty_trap_weight": "random",
    "accuracy_trap_weight": "random",
    "low_hp_trap_weight": "random",
    "crown_trap_weight": "random",
    "empty_clip_trap_weight": "random",
    "nuke_trap_weight": "random",
    "car_trap_weight": "random",
}

nuclearthrone_options_presets: Dict[str, Dict[str, Any]] = {
    "Beginner": beginner,
    "Random": random,
}
