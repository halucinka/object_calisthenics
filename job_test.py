#!/usr/bin/env python3

# Lucia Pal, 2016

'''
Unit tests for appication_test.py
'''
from name import Name, FirstName, LastName
from jobseekers import Jobseeker, Jobseekers
from recruiters import Recruiter
from resume import Resume
from day import Day
from jobs import JReq, ATS, Jobs
from applications import Application, Applications
from company import Company

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
