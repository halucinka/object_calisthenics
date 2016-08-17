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
from src.company import Company
from src.statistics import Statistics

import unittest

class companyTest(unittest.TestCase):

    def setUp(self):

        self.company = Company()

        firstName = FirstName('Obivan')
        lastName = LastName('Kenobi')
        name = Name(firstName, lastName)
        self.recruiter1 = Recruiter(name)
        self.company.addRecruiter(self.recruiter1)

        firstName = FirstName('Master')
        lastName = LastName('Yoda')
        name = Name(firstName, lastName)
        self.recruiter2 = Recruiter(name)
        self.company.addRecruiter(self.recruiter2)

        self.jreq = JReq(self.recruiter1, 'Jedi', 1)
        self.ats = ATS(self.recruiter2, 'Sith', 2)

        firstName = FirstName('Luke')
        lastName = LastName('Skywalker')
        name = Name(firstName, lastName)
        self.jobseeker1 = Jobseeker(name, 1)
        self.company.addJobseeker(self.jobseeker1)
        self.resume1 = Resume('The force is strong with me.', 'Luke Skywalker')
        self.application1 = Application(Day(1), self.jobseeker1, self.resume1)
        self.jobseeker1.apply(self.jreq, self.application1)

        firstName = FirstName('Leia')
        lastName = LastName('Organa')
        name = Name(firstName, lastName)
        self.jobseeker2 = Jobseeker(name, 2)
        self.company.addJobseeker(self.jobseeker2)
        self.resume2 = Resume('I am princess.', 'Leia Organa')
        self.application2 = Application(Day(1), self.jobseeker2, self.resume2)
        self.jobseeker2.apply(self.jreq, self.application2)

        firstName = FirstName('Han')
        lastName = LastName('Solo')
        name = Name(firstName, lastName)
        self.jobseeker3 = Jobseeker(name, 3)
        self.company.addJobseeker(self.jobseeker3)
        self.application3 = Application(Day(47), self.jobseeker3)
        self.jobseeker3.apply(self.ats, self.application3)


    def tearDown(self):
        pass

    def testAddJobseekerAndDisplayJobseeker(self):
        self.assertEqual('Luke Skywalker\nLeia Organa\nHan Solo\n', self.company.displayJobseekers())

    def testAddRecruiterAndDisplayRecruiter(self):
        self.assertEqual('Obivan Kenobi\nMaster Yoda\n', self.company.displayRecruiters())

    def testSeeJobseekersForGivenDay(self):
        self.assertEqual('Hans Solo\n', str(self.company.seeJobseekersForGivenDay(Day(1))))

    def testAggregateStatisticsByJob(self):
        self.assertEqual('', str(self.company.aggregateStatisticsByJob())) # 2 for jedi, 1 for sith


if __name__ == '__main__':
	unittest.main()
