import typing

from .bases import NuclearThroneTestBase
from ..locations import (fish_locations, crystal_locations, eyes_locations, melting_locations, plant_locations, yv_locations, steroids_locations, rebel_locations, robot_locations, chicken_locations, rogue_locations, cuz_locations)
from .. import names
from .. import preset


class TestLocations(NuclearThroneTestBase):
    options = preset.beginner

    def test_characters(self) -> None:
        self.run_location_test(self, f"{names.char_fish} - {names.desert_01}", [names.char_fish])
        self.run_location_test(self, f"{names.char_crystal} - {names.desert_01}", [names.char_crystal])
        self.run_location_test(self, f"{names.char_eyes} - {names.desert_01}", [names.char_eyes])
        self.run_location_test(self, f"{names.char_melting} - {names.desert_01}", [names.char_melting])
        self.run_location_test(self, f"{names.char_plant} - {names.desert_01}", [names.char_plant])
        self.run_location_test(self, f"{names.char_yv} - {names.desert_01}", [names.char_yv])
        self.run_location_test(self, f"{names.char_steroids} - {names.desert_01}", [names.char_steroids])
        self.run_location_test(self, f"{names.char_robot} - {names.desert_01}", [names.char_robot])
        self.run_location_test(self, f"{names.char_chicken} - {names.desert_01}", [names.char_chicken])
        self.run_location_test(self, f"{names.char_rebel} - {names.desert_01}", [names.char_rebel])
        self.run_location_test(self, f"{names.char_horror} - {names.desert_01}", [names.char_horror])
        self.run_location_test(self, f"{names.char_rogue} - {names.desert_01}", [names.char_rogue])
        self.run_location_test(self, f"{names.char_cuz} - {names.desert_01}", [names.char_cuz])

    def run_location_test(self, location: str, itempool: typing.List[str]) -> None:
        items = itempool.copy()
        while len(itempool) > 0:
            self.assertFalse(self.can_reach_location(location), str(self.multiworld.seed))
            self.collect_by_name(itempool.pop())
        self.assertTrue(self.can_reach_location(location), str(self.multiworld.seed))
        self.remove(self.get_items_by_name(items))
