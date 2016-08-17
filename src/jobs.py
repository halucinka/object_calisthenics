from src.applications import Applications
from src.jobseekers import Jobseekers
from src.statistics import Statistics

class Jobs:

    def __init__(self):
        self.jobs = []

    def add(self, job):
        if not (self.isThereJob(job)):
            self.jobs.append(job)

    def filterByDay(self, day):
        jobsFilterByDay = Jobs()
        for job in self.jobs:
            if (job.appliedAtDay(day)):
                jobsFilterByDay.add(job)
        return jobsFilterByDay

    def __str__(self):
        return '\n'.join([str(job) for job in self.jobs]) + '\n'

    def seeAppliedJobseekers(self):
        jobseekers = Jobseekers()
        for job in self.jobs:
            for jobseeker in job.seeAppliedJobseekers().seeJobseekers(): #wrong
                jobseekers.add(jobseeker)
        return jobseekers

    def isThereJob(self, job):
        for j in self.jobs:
            if (j.id == job.id):
                return True
        return False

    def aggregateStatisticsByJob(self):
        statistics = Statistics()
        for job in self.jobs:
            statistics.add(job, job.numberOfApplications())
        return statistics
