#!/usr/bin/env python3

# Lucia Pal, 2016

'''
Unit tests for jobs.py
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
from src.resume import Resume
from src.application import Application


import unittest

class JobsTest(unittest.TestCase):

    def setUp(self):
        name = Name(FirstName('Master'), LastName('Yoda'))
        recruiter = Recruiter(name)

        name = Name(FirstName('Luke'), LastName('Skywalker'))
        self.jobseeker = Jobseeker(name, 1)

        self.jreq = JReq(recruiter, 'Jedi', 1)
        self.resume = Resume('The force is strong with me.', 'Luke Skywalker')
        application1 = Application(Day(1), self.jobseeker, self.resume)
        self.jobseeker.apply(self.jreq, application1)

        self.ats = ATS(recruiter, 'Sith', 2)
        application2 = Application(Day(1), self.jobseeker)
        self.jobseeker.apply(self.ats, application2)

        self.ats2 = ATS(recruiter, 'Sith2', 3)
        application3 = Application(Day(47), self.jobseeker)
        self.jobseeker.apply(self.ats2, application3)

    def tearDown(self):
        pass

    def testAddAndStr(self):
        jobs = Jobs()
        jobs.add(self.jreq)
        jobs.add(self.ats)
        self.assertEqual("Jedi\nSith\n",str(jobs))

    def testFilterByDay(self):
        jobs = Jobs()
        jobs.add(self.jreq)
        jobs.add(self.ats)
        jobs.add(self.ats2)
        self.assertEqual('Jedi\nSith\n', str(jobs.filterByDay(Day(1))))

    def testSeeJobseekers(self):
        jobs = Jobs()
        jobs.add(self.jreq)
        jobs.add(self.ats)
        self.assertEqual('Luke Skywalker\n', str(jobs.seeAppliedJobseekers()))

    def testIsThereJob(self):
        jobs = Jobs()
        jobs.add(self.jreq)
        self.assertTrue(jobs.isThereJob(self.jreq))
        self.assertFalse(jobs.isThereJob(self.ats))

    def testAggregateStatisticsByJob(self):
        jobs = Jobs()
        jobs.add(self.jreq)
        jobs.add(self.ats)
        self.assertEqual('1 1\n2 1\n', str(jobs.aggregateStatisticsByJob())) #

if __name__ == '__main__':
	unittest.main()
