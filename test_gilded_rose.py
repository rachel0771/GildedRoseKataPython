# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        
    def test_backstage_passes_increase_in_quality_as_sellin_approaches(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(42, items[0].quality)  

    def test_dexterity_vest_decreases_in_quality_twice_as_fast_after_sell_by_date(self):
        items = [Item("+5 Dexterity Vest", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)  


if __name__ == '__main__':
    unittest.main()
