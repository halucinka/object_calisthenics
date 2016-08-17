#!/usr/bin/env python3

# Lucia Pal, 2016

'''
Unit tests for appication_test.py
'''
from name import Name, FirstName, LastName
from jobseekers import Jobseeker, Jobseekers
from resume import Resume
from day import Day
from applications import Application, Applications
from company import Company

import unittest

class ApplicationTest(unittest.TestCase):

    def setUp(self):
        firstName = FirstName('Luke')
        lastName = LastName('Skywalker')
        name = Name(firstName, lastName)

        self.jobseeker = Jobseeker(name)
        self.resume = Resume('The force is strong with me.', 'Luke Skywalker')
        self.resume2 = Resume('The force is strong with me.', 'Leia Organa')

        self.day = Day(47)

    def tearDown(self):
        pass

    def testHasResume(self):
        self.application = Application(self.day, self.jobseeker, self.resume)
        self.assertTrue(self.application.hasResume())

    def testHasResume2(self):
        self.application = Application(self.day, self.jobseeker)
        self.assertFalse(self.application.hasResume())

    def testValidName(self):
        self.application = Application(self.day, self.jobseeker, self.resume)
        self.assertTrue(self.application.validName())

    def testValidName2(self):
        self.application = Application(self.day, self.jobseeker, self.resume2)
        self.assertFalse(self.application.validName())


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
