# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Check the actual item name
        self.assertEqual("foo", items[0].name)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Aged Brie increases in quality by 1 each day
        self.assertEqual(1, items[0].quality)

    def test_backstage_passes_increase_in_quality_as_sellin_approaches(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Increases by 2 when there are less than or equal to 10 days 
        self.assertEqual(42, items[0].quality)

    def test_dexterity_vest_decreases_in_quality_twice_as_fast_after_sell_by_date(self):
        items = [Item("+5 Dexterity Vest", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Decreases by 2 after the sell by date
        self.assertEqual(8, items[0].quality)

    # A new test for Conjured items
    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality) 


if __name__ == '__main__':
    unittest.main()
