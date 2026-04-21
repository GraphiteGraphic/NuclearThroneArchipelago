from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld
from . import preset, options

class NuclearThroneWebWorld(WebWorld):
    theme = "partyTime"
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Nuclear Throne randomizer connected to an Archipelago Multiworld.",
            "English",
            "setup_en.md",
            "setup/en",
            ["RomanPenguin"]
        )
    ]

    option_groups = options.nuclearthrone_option_groups
    options_presets = preset.nuclearthrone_options_presets