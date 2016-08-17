from src.jobseekers import Jobseekers
from src.jobs import Jobs
class Recruiter:

    def __init__(self, name):
        self.name = name
        self.jobs = Jobs()

    def toString(self):
        return self.name.toString()

    def post(self, job):
        self.jobs.add(job)

    def seeJobs(self):
        return self.jobs

    def seeJobTitles(self):
        return self.jobs.toString()

    def seeJobseekersForGivenJob(self, job):
        jobseekers = Jobseekers() # je potom jobseekers stale singleton???
        for app in job.applications:
            jobseekers.add(app.jobseeker)
        return jobseekers

    def seeJobseekersForGivenDay(self, day):
        jobseekers = Jobseekers()
        jobsForGivenDay = self.jobs.filterByDay(day)
        for job in jobsForGivenDay:
            for app in job.applications:
                jobseekers.add(app.jobseeker)

    def seeJobseekersForGivenJobForGivenDay(self, job, day):
        jobseekers = Jobseekers()
        jobsForGivenDay = self.jobs.filterByDay(day)
        if job in jobsForGivenDay:
            jobseekers = self.seeJobseekersForGivenJob(job)
        return jobseekers


class Recruiters:
    '''singleton'''

    def __init__(self):
        self.recruiters = []

    def add(self, recruiter):
        self.recruiters.append(recruiter)

    def toString(self):
        toString = ''
        for recruiter in self.recruiters:
            toString += recruiter.toString() + '\n'
        return toString
