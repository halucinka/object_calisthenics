#!/usr/bin/env python3


'''
Unit tests for JReq.py
'''

from src.firstName import FirstName
from src.lastName import LastName
from src.name import Name
from src.jobseeker import Jobseeker
from src.recruiter import Recruiter
from src.day import Day
from src.resume import Resume
from src.jreq import JReq
from src.ats import ATS
from src.application import Application


import unittest

class JReqTest(unittest.TestCase):

    def setUp(self):
        name = Name(FirstName('Master'), LastName('Yoda'))
        recruiter = Recruiter(name)

        name = Name(FirstName('Luke'), LastName('Skywalker'))
        self.jobseeker = Jobseeker(name)
        self.jreq = JReq(recruiter, 'Jedi') #TITLE SHOULD BE CLASS
        self.day = Day(47)

    def tearDown(self):
        pass

    def testApplyAndNumberOfApplications(self):
        resume = Resume('The force is strong with me.', 'Luke Skywalker')
        application = Application(self.day, self.jobseeker, resume)
        self.jreq.apply(application)
        self.assertEqual(1, self.jreq.numberOfApplications())

    def testApplyException(self):
        application = Application(self.day, self.jobseeker)
        self.assertRaises(Exception, self.jreq.apply, application)

    def testAppliedAtDay(self):
        resume = Resume('The force is strong with me.', 'Luke Skywalker')
        application = Application(self.day, self.jobseeker, resume)
        self.jreq.apply(application)
        self.assertTrue(self.jreq.appliedAtDay(Day(47)))

    def testAppliedAtDay2(self):
        resume = Resume('The force is strong with me.', 'Luke Skywalker')
        application = Application(self.day, self.jobseeker, resume)
        self.jreq.apply(application)
        self.assertFalse(self.jreq.appliedAtDay(Day(1)))


if __name__ == '__main__':
	unittest.main()
