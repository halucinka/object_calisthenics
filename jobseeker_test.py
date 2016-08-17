#!/usr/bin/env python3

'''
Unit tests for jobseeker.py
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

class jobseekerTest(unittest.TestCase):

    def setUp(self):
        firstName = FirstName('Obivan')
        lastName = LastName('Kenobi')
        name = Name(firstName, lastName)
        self.recruiter = Recruiter(name)

        self.jreq = JReq(self.recruiter, 'Jedi', 1)
        self.ats = ATS(self.recruiter, 'Sith', 2)


        firstName = FirstName('Luke')
        lastName = LastName('Skywalker')
        name = Name(firstName, lastName)
        self.jobseeker = Jobseeker(name, 1)
        self.resume = Resume('The force is strong with me.', 'Luke Skywalker')
        self.resume2 = Resume('The force is strong with me.', 'Leia Organa')

        self.application1 = Application(Day(47), self.jobseeker, self.resume)
        self.application2 = Application(Day(47), self.jobseeker, self.resume2)
        self.application3 = Application(Day(1), self.jobseeker, self.resume)
        self.application4 = Application(Day(1), self.jobseeker, self.resume)
    def tearDown(self):
        pass

    def testApplyAndSeeAppliedJobs(self):
        self.jobseeker.apply(self.jreq, self.application1)
        self.jobseeker.apply(self.ats, self.application1)
        self.assertEqual('Jedi\nSith\n', str(self.jobseeker.seeAppliedJobs()))

    def testApplyAndSeeAppliedJobsException(self):
        self.assertRaises(Exception, self.jobseeker.apply, self.jreq, self.application2)

    def testSaveJobAndSeeSavedJobs(self):
        self.jobseeker.saveJob(self.jreq)
        self.jobseeker.saveJob(self.ats)
        self.assertEqual('Jedi\nSith\n', str(self.jobseeker.seeSavedJobs()))

    def testAppliedJobsFilterByDay(self):
        self.jobseeker.apply(self.jreq, self.application1)
        self.jobseeker.apply(self.ats, self.application1)
        self.jobseeker.apply(self.jreq, self.application3)
        self.jobseeker.apply(self.ats, self.application4)
        self.assertEqual('Jedi\nSith\n', str(self.jobseeker.appliedJobsFilterByDay(Day(47))))


    def testIsMatchingJobseeker(self):
        self.assertTrue(self.jobseeker.isMatchingJobseeker(self.jobseeker))
        name = Name(FirstName('Leia'), LastName('Organa'))
        jobseeker2 = Jobseeker(name, 2)
        self.assertFalse(self.jobseeker.isMatchingJobseeker(jobseeker2))

if __name__ == '__main__':
	unittest.main()
