#!/usr/bin/env python3

'''
Unit tests for recruiter.py
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

class recruiterTest(unittest.TestCase):

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
        #self.resume2 = Resume('The force is strong with me.', 'Leia Organa')

        self.day = Day(47)
        self.application = Application(self.day, self.jobseeker, self.resume)
        self.recruiter.post(self.jreq)
        self.recruiter.post(self.ats)

    def tearDown(self):
        pass

    def testStr(self):
        self.assertEqual('Obivan Kenobi', str(self.recruiter))

    def testPostAndSeeJobTitles(self):
        self.assertEqual('Jedi\nSith\n', self.recruiter.seeJobTitles())

    def testSeeJobs(self):
        jobs = self.recruiter.seeJobs()
        self.assertEqual('Jedi\nSith\n', str(jobs))

    def testSeeJobseekersForGivenJob(self):
        application = Application(self.day, self.jobseeker, self.resume)
        self.jreq.apply(application)
        self.assertEqual('Luke Skywalker\n', str(self.recruiter.seeJobseekersForGivenJob(self.jreq)))

    def testSeeJobseekersForGivenDay(self):
        application = Application(self.day, self.jobseeker, self.resume)
        self.jreq.apply(application)
        self.assertEqual('Luke Skywalker\n', str(self.recruiter.seeJobseekersForGivenDay(Day(47))))

    def testSeeJobseekersForGivenJobForGivenDay(self):
        application = Application(self.day, self.jobseeker, self.resume)
        self.jreq.apply(application)

        firstName = FirstName('Leia')
        lastName = LastName('Organa')
        name = Name(firstName, lastName)
        jobseeker2 = Jobseeker(name, 2)
        application2 = Application(Day(47), jobseeker2)
        self.ats.apply(application2)
        self.application = Application(self.day, self.jobseeker, self.resume)

        firstName = FirstName('Han')
        lastName = LastName('Solo')
        name = Name(firstName, lastName)
        jobseeker3 = Jobseeker(name, 3)
        application3 = Application(Day(47), jobseeker3)
        self.ats.apply(application3)
        self.application = Application(self.day, self.jobseeker, self.resume)

        self.assertEqual('Leia Organa\nHan Solo\n', str(self.recruiter.seeJobseekersForGivenJobForGivenDay(self.ats, Day(47))))

    def testAggregateStatisticsByJob(self):
        self.assertEqual('', str(self.recruiter.aggregateStatisticsByJob()))


if __name__ == '__main__':
	unittest.main()
