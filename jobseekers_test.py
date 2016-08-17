#!/usr/bin/env python3

'''
Unit tests for jobseekers.py
'''
from src.name import Name, FirstName, LastName
from src.jobseeker import Jobseeker
from src.jobseekers import Jobseekers
from src.resume import Resume
from src.day import Day
from src.application import Application
from src.applications import Applications
from src.recruiter import Recruiter
from src.jreq import JReq
from src.ats import ATS

import unittest

class jobseekersTest(unittest.TestCase):

    def setUp(self):
        firstName = FirstName('Luke')
        lastName = LastName('Skywalker')
        name = Name(firstName, lastName)
        self.jobseeker1 = Jobseeker(name, 1)

        firstName = FirstName('Leia')
        lastName = LastName('Organa')
        name = Name(firstName, lastName)
        self.jobseeker2 = Jobseeker(name, 2)

        firstName = FirstName('Han')
        lastName = LastName('Solo')
        name = Name(firstName, lastName)
        self.jobseeker3 = Jobseeker(name, 3)


    def tearDown(self):
        pass

    def test(self):
        jobseekers = Jobseekers()
        jobseekers.add(self.jobseeker1)
        jobseekers.add(self.jobseeker1)
        jobseekers.add(self.jobseeker2)
        jobseekers.add(self.jobseeker3)
        self.assertEqual('Luke Skywalker\nLeia Organa\nHan Solo\n', str(jobseekers))


if __name__ == '__main__':
	unittest.main()
