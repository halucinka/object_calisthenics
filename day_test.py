#!/usr/bin/env python3

'''
Unit tests for day.py
'''
from src.day import Day
import unittest

class DayTest(unittest.TestCase):

    def test(self):
        day = Day(47)
        self.assertEqual('47', str(day))

    def testEquality1(self):
        day1 = Day(47)
        day2 = Day(47)
        self.assertTrue(day1 == day2)
        self.assertFalse(day1 != day2)

    def testEquality2(self):
        day1 = Day(47)
        day2 = Day(42)
        self.assertFalse(day1 == day2)
        self.assertTrue(day1 != day2)



if __name__ == '__main__':
	unittest.main()
