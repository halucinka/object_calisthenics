#!/usr/bin/env python3

'''
Unit tests for ats.py
'''

from src.firstName import FirstName
from src.lastName import LastName
from src.name import Name
from src.jobseeker import Jobseeker
from src.recruiter import Recruiter
from src.day import Day
from src.jobs import Jobs
from src.jreq import JReq
from src.ats import ATS
from src.application import Application


import unittest

class ATSTest(unittest.TestCase):

    def setUp(self):
        name = Name(FirstName('Master'), LastName('Yoda'))
        recruiter = Recruiter(name)

        name = Name(FirstName('Luke'), LastName('Skywalker'))
        self.jobseeker = Jobseeker(name)
        self.ats = ATS(recruiter, 'Jedi') #TITLE SHOULD BE CLASS
        self.day = Day(47)

    def tearDown(self):
        pass

    def testApplyAndNumberOfApplications(self):
        application = Application(self.day, self.jobseeker)
        self.ats.apply(application)
        self.assertEqual(1, self.ats.numberOfApplications())

    def testAppliedAtDay(self):
        application = Application(self.day, self.jobseeker)
        self.ats.apply(application)
        self.assertTrue(self.ats.appliedAtDay(Day(47)))

    def testAppliedAtDay2(self):
        application = Application(self.day, self.jobseeker)
        self.ats.apply(application)
        self.assertFalse(self.ats.appliedAtDay(Day(1)))




if __name__ == '__main__':
	unittest.main()
