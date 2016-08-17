#!/usr/bin/env python3

'''
Unit tests for appications.py
'''
from src.name import Name, FirstName, LastName
from src.jobseeker import Jobseeker
from src.jobseekers import Jobseekers
from src.resume import Resume
from src.day import Day
from src.application import Application
from src.applications import Applications
from src.company import Company

import unittest

class ApplicationsTest(unittest.TestCase):

    def setUp(self):
        name = Name(FirstName('Luke'), LastName('Skywalker'))
        self.jobseeker1 = Jobseeker(name)
        self.day1 = Day(47)
        self.application1 = Application(self.day1, self.jobseeker1)

        name = Name(FirstName('Leia'), LastName('Organa'))
        self.jobseeker2 = Jobseeker(name)
        self.day2 = Day(1)
        self.application2 = Application(self.day2, self.jobseeker2)

        name = Name(FirstName('Han'), LastName('Solo'))
        self.jobseeker3 = Jobseeker(name)
        self.day3 = Day(47)
        self.application3 = Application(self.day3, self.jobseeker3)

    def testAddAndSize(self):
        applications = Applications()
        applications.add(self.application1)
        applications.add(self.application2)
        applications.add(self.application3)
        self.assertEqual(3, applications.size())
        self.assertFalse(applications.empty())

    def testEmpty(self):
        applications = Applications()
        self.assertTrue(applications.empty())

    def testFilterByDay(self):
        applications = Applications()
        applications.add(self.application1)
        applications.add(self.application2)
        applications.add(self.application3)
        self.assertEqual(2, applications.filterByDay(Day(47)).size())
        self.assertEqual(1, applications.filterByDay(Day(1)).size())


if __name__ == '__main__':
	unittest.main()
