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
from src.application import Application


import unittest

class JobsTest(unittest.TestCase):

    def setUp(self):
        name = Name(FirstName('Master'), LastName('Yoda'))
        recruiter = Recruiter(name)

        name = Name(FirstName('Luke'), LastName('Skywalker'))
        jobseeker = Jobseeker(name)

        self.jreq = JReq(recruiter, 'Jedi') #TITLE SHOULD BE CLASS
        application1 = Application(Day(1), jobseeker)

        self.ats = ATS(recruiter, 'Sith')
        application2 = Application(Day(47), jobseeker)
        self.ats.apply(application2)

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
        self.assertEqual('Sith\n', str(jobs.filterByDay(Day(47))))



if __name__ == '__main__':
	unittest.main()
