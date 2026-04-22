from dataclasses import dataclass
import random
from typing import List
from Options import (OptionGroup, Choice, Range, PerGameCommonOptions, Toggle, NamedRange)


class StartingCharacter(Choice):
    """
    The initial character unlocked at the start
    """
    display_name = "Starting Character"
    option_default = 0
    option_fish = 1
    option_crystal = 2
    option_eyes = 3
    option_melting = 4
    option_plant = 5
    option_yv = 6
    option_steroids = 7
    option_robot = 8
    option_chicken = 9
    option_rebel = 10
    option_horror = 11
    option_rogue = 12
    option_cuz = 16
    default = 0

    @classmethod
    def from_text(cls, text: str) -> Choice:
        text = text.lower()
        if text == "random":
            choice_list = list(cls.name_lookup)
            choice_list.remove(0)
            return cls(random.choice(choice_list))
        return super().from_text(text)


class StartingWeapon(NamedRange):
    """
    Vanilla: Start the run with the default starting weapon
    Random-Balanced: Start the run with a feasible weapon
    Random: Start the run with a randomly determined non-golden weapon
    Custom ID: Start the run with a weapon based on ID value. 
        For example; putting in "1" will let you start off with a revolver on everyone. 
        Maximum value is 128.
    """
    display_name = "Starting Primary"
    range_start = 0
    range_end = 128
    default = 0
    special_range_names = {
        "vanilla": 0,
        "random-balanced": -1,
        "random": -2
    }
    

class StartingSecondary(NamedRange):
    """
    Vanilla: Start your run with no secondary weapon
    Random-Balanced: Start your run with a feasible weapon as your secondary
    Random: Start your run with a randomly determined non-golden weapon as your secondary.
    Custom ID: Start the run with a weapon based on ID value. 
        For example; putting in "1" will let you start off with a revolver on everyone. 
        Maximum value is 128.
    """
    display_name = "Starting Secondary"
    range_start = 0
    range_end = 128
    default = 0
    special_range_names = {
        "vanilla": 0,
        "random-balanced": -1,
        "random": -2
    }


class Goal(Choice):
    """
    Throne: Sit on the Throne or at the Captain's desk
    Captain: Defeat the Captain
    Boss Rush: Defeat all bosses in a single run
    Wasteland King: Sit on the Throne on Loop 3 or higher
    Endurance: Reach Desert 1 of the identified Loop number (Default: 1)
    """
    display_name = "Goal"
    option_throne = 0
    option_captain = 1
    option_boss_rush = 2
    option_wasteland_king = 3
    option_endurance = 4
    default = 0
    
    @classmethod
    def from_text(cls, text: str) -> Choice:
        text = text.lower()
        if text == "random":
            choice_list = list(cls.name_lookup)
            return cls(random.choice(choice_list))
        return super().from_text(text)


class GoalNumber(Range):
    """
    Number of characters required to achieve the goal to win.
    """
    display_name = "Characters required to reach Goal"
    range_start = 1
    range_end = 13
    default = 1


class EnduranceNumber(Range):
    """
    Number of loops required to achieve the Endurance goal.
    """
    display_name = "Loops required to reach Endurance Goal"
    range_start = 1
    range_end = 25
    default = 1


class AnarchyMode(Toggle):
    """
    Enables weapons to spawn on any level
    """
    display_name = "Anarchy Mode"
    default = False


class TrapPercentage(Range):
    """
    Percentage of filler items to be converted to trap items
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class DropTrapPercentage(Range):
    """
    Chance that any given trap drops your weapons
    """
    display_name = "Drop Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class CurseTrapPercentage(Range):
    """
    Chance that any given trap curses your weapons
    """
    display_name = "Curse Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class EatTrapPercentage(Range):
    """
    Chance that any given trap forces you to eat your active weapon
    """
    display_name = "Eat Weapon Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class BigDogTrapPercentage(Range):
    """
    Chance that any given trap transforms you into Big Dog temporarily
    """
    display_name = "Big Dog Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class FrogTrapPercentage(Range):
    """
    Chance that any given trap transforms you into Frog temporarily
    """
    display_name = "Frog Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class HorrorTrapPercentage(Range):
    """
    Chance that any given trap summons a hostile horror
    """
    display_name = "Horror Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class MaggotTrapPercentage(Range):
    """
    Chance that any given trap summons a single maggot on top of you
    """
    display_name = "Maggot Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class PopoTrapPercentage(Range):
    """
    Chance that any given trap summons several IDPD
    """
    display_name = "IDPD Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class SkeletonTrapPercentage(Range):
    """
    Chance that any given trap transforms you into Skeleton temporarily
    """
    display_name = "Skeleton Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class TMNTTrapPercentage(Range):
    """
    Chance that any given trap summons 4 turtles and a rat around you
    """
    display_name = "Turtle Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class SlowTrapPercentage(Range):
    """
    Chance that any given trap halves your speed temporarily
    """
    display_name = "Slow Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class SpeedTrapPercentage(Range):
    """
    Chance that any given trap drastically increases your speed temporarily
    """
    display_name = "Speed Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class RustyTrapPercentage(Range):
    """
    Chance that any given trap replaces your active weapon with the Rusty Revolver
    """
    display_name = "Rusty Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class AccuracyTrapPercentage(Range):
    """
    Chance that any given trap worsens your accuracy temporarily
    """
    display_name = "Accuracy Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class LowHPTrapPercentage(Range):
    """
    Chance that any given trap sets your HP to 1
    """
    display_name = "One Hit Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class CrownTrapPercentage(Range):
    """
    Chance that any given trap gives you a random crown
    """
    display_name = "Crown Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class EmptyClipTrapPercentage(Range):
    """
    Chance that any given trap empties your active weapon ammo
    """
    display_name = "Empty Clip Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class NukeTrapPercentage(Range):
    """
    Chance that any given trap replaces your weapons with Nuke Launchers and replaces your ammo with max explosives
    """
    display_name = "Nuke Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


class CarWreckTrapPercentage(Range):
    """
    Chance that any given trap replaces existing props with 1HP Car Wrecks
    """
    display_name = "Car Wreck Trap Percentage"
    range_start = 0
    range_end = 100
    default = 50


@dataclass
class NuclearThroneOptions(PerGameCommonOptions):
    starting_character: StartingCharacter
    starting_weapon: StartingWeapon
    starting_secondary: StartingSecondary
    goal: Goal
    goal_number: GoalNumber
    endurance_number: EnduranceNumber
    anarchy_mode: AnarchyMode
    trap_percentage: TrapPercentage
    drop_trap_weight: DropTrapPercentage
    eat_trap_weight: EatTrapPercentage
    curse_trap_weight: CurseTrapPercentage
    bigdog_trap_weight: BigDogTrapPercentage
    frog_trap_weight: FrogTrapPercentage
    horror_trap_weight: HorrorTrapPercentage
    maggot_trap_weight: MaggotTrapPercentage
    popo_trap_weight: PopoTrapPercentage
    skeleton_trap_weight: SkeletonTrapPercentage
    tmnt_trap_weight: TMNTTrapPercentage
    slow_trap_weight: SlowTrapPercentage
    speed_trap_weight: SpeedTrapPercentage
    rusty_trap_weight: RustyTrapPercentage
    accuracy_trap_weight: AccuracyTrapPercentage
    low_hp_trap_weight: LowHPTrapPercentage
    crown_trap_weight: CrownTrapPercentage
    empty_clip_trap_weight: EmptyClipTrapPercentage
    nuke_trap_weight: NukeTrapPercentage
    car_trap_weight: CarWreckTrapPercentage

nuclearthrone_option_groups: List[OptionGroup] = [
    OptionGroup("Goal Options", [Goal, GoalNumber, EnduranceNumber]),
    OptionGroup("World Options", [StartingCharacter, StartingWeapon, StartingSecondary, AnarchyMode,]),
    OptionGroup("Trap Options", [TrapPercentage, DropTrapPercentage, CurseTrapPercentage, EatTrapPercentage,
                                BigDogTrapPercentage, FrogTrapPercentage, HorrorTrapPercentage,
                                MaggotTrapPercentage, PopoTrapPercentage, SkeletonTrapPercentage,
                                TMNTTrapPercentage, SlowTrapPercentage, SpeedTrapPercentage,
                                RustyTrapPercentage, AccuracyTrapPercentage, LowHPTrapPercentage,
                                CrownTrapPercentage, EmptyClipTrapPercentage, NukeTrapPercentage,
                                CarWreckTrapPercentage])
]
