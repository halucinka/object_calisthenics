#!/usr/bin/env python3

'''
Unit tests for appication.py
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

class ApplicationTest(unittest.TestCase):

    def setUp(self):
        firstName = FirstName('Luke')
        lastName = LastName('Skywalker')
        name = Name(firstName, lastName)

        self.jobseeker = Jobseeker(name, 1)
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




if __name__ == '__main__':
	unittest.main()
