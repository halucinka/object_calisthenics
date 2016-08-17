from src.jobseekers import Jobseekers
from src.jobs import Jobs
from src.statistics import Statistics

class Recruiter:

    def __init__(self, name):
        self.name = name
        self.jobs = Jobs()

    def __str__(self):
        return str(self.name)

    def post(self, job):
        self.jobs.add(job)

    def seeJobs(self):
        return self.jobs

    def seeJobTitles(self):
        return str(self.jobs)

    def seeJobseekersForGivenJob(self, job):
        return job.seeAppliedJobseekers()

    def seeJobseekersForGivenDay(self, day):
        jobseekers = Jobseekers()
        jobsForGivenDay = self.jobs.filterByDay(day)
        return jobsForGivenDay.seeAppliedJobseekers()

    def seeJobseekersForGivenJobForGivenDay(self, job, day):
        jobseekers = Jobseekers()
        jobsForGivenDay = self.jobs.filterByDay(day)
        if (jobsForGivenDay.isThereJob(job)):
            jobseekers = self.seeJobseekersForGivenJob(job)
        return jobseekers

    def aggregateStatisticsByJob(self):
        return self.jobs.aggregateStatisticsByJob()
