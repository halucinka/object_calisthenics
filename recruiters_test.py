#!/usr/bin/env python3

'''
Unit tests for recruiters.py
'''
from src.name import Name, FirstName, LastName
from src.recruiter import Recruiter
from src.recruiters import Recruiters
from src.statistics import Statistics


import unittest

class recruitersTest(unittest.TestCase):

    def setUp(self):
        firstName = FirstName('Obivan')
        lastName = LastName('Kenobi')
        name = Name(firstName, lastName)
        self.recruiter1 = Recruiter(name)

        firstName = FirstName('Master')
        lastName = LastName('Yoda')
        name = Name(firstName, lastName)
        self.recruiter2 = Recruiter(name)

    def tearDown(self):
        pass

    def testStrAndAdd(self):
        recruiters = Recruiters()
        recruiters.add(self.recruiter1)
        recruiters.add(self.recruiter2)
        self.assertEqual('Obivan Kenobi\nMaster Yoda\n', str(recruiters))

    

if __name__ == '__main__':
	unittest.main()
