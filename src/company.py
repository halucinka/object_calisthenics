from src.recruiters import Recruiters
from src.jobseekers import Jobseekers
from src.statistics import Statistics

class Company:
    def __init__(self):
        self.recruiters = Recruiters()
        self.jobseekers = Jobseekers()

    def addJobseeker(self, jobseeker):
        self.jobseekers.add(jobseeker)

    def addRecruiter(self, recruiter):
        self.recruiters.add(recruiter)

    def displayJobseekers(self):
        return str(self.jobseekers)

    def displayRecruiters(self):
        return str(self.recruiters)

    def seeJobseekersForGivenDay(self, day):
        return self.jobseekers.jobseekersForGivenDay(day)

    def aggregateStatisticsByJob(self):
        return self.recruiters.aggregateStatisticsByJob()
