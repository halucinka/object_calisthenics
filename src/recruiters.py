from src.jobseekers import Jobseekers
from src.jobs import Jobs
from src.statistics import Statistics

class Recruiters:

    def __init__(self):
        self.recruiters = []

    def add(self, recruiter):
        self.recruiters.append(recruiter)

    def __str__(self):
        return '\n'.join(str(recruiter) for recruiter in self.recruiters) + '\n'

    def aggregateStatisticsByJob(self):
        statistics = Statistics()
        for recruiter in self.recruiters:
            statistics.addOtherStatistics(recruiter.aggregateStatisticsByJob)
        return statistics
