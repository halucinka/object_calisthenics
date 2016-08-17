#!/usr/bin/env python3

# Lucia Pal, 2016

'''
Unit tests for Exercise: https://gist.github.com/zsiec/12d81963d1bdd126a6046e50fd2af7d6
'''
from name import Name, FirstName, LastName
from jobseekers import Jobseeker, Jobseekers
from resume import Resume
from recruiters import Recruiter, Recruiters
from jobs import Job, JReq, ATS, Jobs
from applications import Application, Applications
from company import Company
import unittest

class IntegrationTest(unittest.TestCase):

    def setUp(self):
        print('zaciatok testu')

    def tearDown(self):
        print('koniec testu')
    def test(self):
        #company, 2 jobseekers, 2 recruiters, 1 job
        company = Company()
        JS1firstName = FirstName('Luke')
        JS1lastName = LastName('Skywalker')
        JS1name = Name(JS1firstName, JS1lastName)
        JS1 = Jobseeker(JS1name)

        JS2firstName = FirstName('Leia')
        JS2lastName = LastName('Organa')
        JS2name = Name(JS2firstName, JS2lastName)
        JS2 = Jobseeker(JS2name)
        company.addJobseeker(JS1)
        company.addJobseeker(JS2)

        R1firstName = FirstName('Master')
        R1lastName = LastName('Yoda')
        R1name = Name(R1firstName, R1lastName)
        R1 = Recruiter(R1name)

        R2firstName = FirstName('Obivan')
        R2lastName = LastName('Kenobi')
        R2name = Name(R2firstName, R2lastName)
        R2 = Recruiter(R2name)

        company.addRecruiter(R1)
        company.addRecruiter(R2)

        job1jreq = JReq(R1, 'Jedi')
        resumeJS1 = Resume('Force is strong with me.', 'Luke Skywalker')
        application1 = Application(1, JS1, resumeJS1)

        job1jreq.apply(application1)

        print(company.toStringJobseekers())
        print(company.toStringRecruiters())
        self.assertEqual('', '')

    def test_postingAndSeeJobsByRecruiter(self):

        company = Company()
        R1firstName = FirstName('Master')
        R1lastName = LastName('Yoda')
        R1name = Name(R1firstName, R1lastName)
        R1 = Recruiter(R1name)

        company.addRecruiter(R1)

        job1 = Job(R1, 'Jedi')
        job1req = job1.createJob('JReq')
        #posting job by recruiter
        R1.post(job1req)
        # in R1.seeJobs() are all jobs posted by recruiter R1. We print titles by R1.seeJobTitles()
        self.assertEqual('Jedi\n', R1.seeJobTitles())

    def test_jobseekersSavedJobs(self):
        # company, 1 jobseeker, 1 resume, 2 applications, 1 recruiter who posts 2 jobs, 2 saved jobs for jobseeker
        company = Company()

        JS1firstName = FirstName('Luke')
        JS1lastName = LastName('Skywalker')
        JS1name = Name(JS1firstName, JS1lastName)
        JS1 = Jobseeker(JS1name)

        R1firstName = FirstName('Master')
        R1lastName = LastName('Yoda')
        R1name = Name(R1firstName, R1lastName)
        R1 = Recruiter(R1name)

        company.addRecruiter(R1)

        company.addJobseeker(JS1)

        job1 = Job(R1, 'Jedi')
        job1req = job1.createJob('JReq')
        job2 = Job(R1, 'Sith')
        job2ATS = job2.createJob('ATS')



        JS1.saveJob(job1)
        JS1.saveJob(job2)
        self.assertEqual('Jedi\nSith\n', JS1.toStringSavedJobs())

    def test_jobseekersAppliedJobs(self):
        company = Company()

        JS1firstName = FirstName('Luke')
        JS1lastName = LastName('Skywalker')
        JS1name = Name(JS1firstName, JS1lastName)
        JS1 = Jobseeker(JS1name)

        R1firstName = FirstName('Master')
        R1lastName = LastName('Yoda')
        R1name = Name(R1firstName, R1lastName)
        R1 = Recruiter(R1name)

        company.addRecruiter(R1)

        company.addJobseeker(JS1)

        job1 = Job(R1, 'Jedi')
        job1req = job1.createJob('JReq')
        job2 = Job(R1, 'Sith')
        job2ATS = job2.createJob('ATS')

        resumeJS1 = Resume('Force is strong with me.', 'Luke Skywalker')
        application1 = Application(1, JS1, resumeJS1)
        application2 = Application(1, JS1)

        JS1.apply(job1, application1)
        JS1.apply(job2, application2)
        #print(JS1.toStringSavedJobs())
        self.assertEqual('Jedi\nSith\n', JS1.toStringAppliedJobs())

    def test_jobseekersAppliedToJReqWithoutResume(self):
        company = Company()

        JS1firstName = FirstName('Luke')
        JS1lastName = LastName('Skywalker')
        JS1name = Name(JS1firstName, JS1lastName)
        JS1 = Jobseeker(JS1name)

        R1firstName = FirstName('Master')
        R1lastName = LastName('Yoda')
        R1name = Name(R1firstName, R1lastName)
        R1 = Recruiter(R1name)

        company.addRecruiter(R1)

        company.addJobseeker(JS1)

        job1 = Job(R1, 'Jedi')
        job1req = job1.createJob('JReq')

        application1 = Application(1, JS1)
        #print(application1.resume.resumeString)
        self.assertRaises(Exception, JS1.apply(job1, application1))

    def test_jobseekersWrongResume(self):
        company = Company()

        JS1firstName = FirstName('Luke')
        JS1lastName = LastName('Skywalker')
        JS1name = Name(JS1firstName, JS1lastName)
        JS1 = Jobseeker(JS1name)

        R1firstName = FirstName('Master')
        R1lastName = LastName('Yoda')
        R1name = Name(R1firstName, R1lastName)
        R1 = Recruiter(R1name)

        company.addRecruiter(R1)

        company.addJobseeker(JS1)

        job1 = Job(R1, 'Jedi')
        job1req = job1.createJob('JReq')
        job2 = Job(R1, 'Sith')
        job2ATS = job2.createJob('ATS')

        resumeJS1 = Resume('I am princess.', 'Leia')
        application1 = Application(1, JS1, resumeJS1)


        self.assertRaises(Exception, JS1.apply(job1, application1))

if __name__ == '__main__':
	unittest.main()
