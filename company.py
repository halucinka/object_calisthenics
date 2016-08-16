from recruiters import Recruiters
from jobseekers import Jobseekers
class Company:
    def __init__(self):
        self.recruiters = Recruiters()
        self.jobseekers = Jobseekers()

    def addJobseeker(self, jobseeker):
        self.jobseekers.add(jobseeker)

    def addRecruiter(self, recruiter):
        self.recruiters.add(recruiter)

    def toStringJobseekers(self):
        return self.jobseekers.toString()

    def toStringRecruiters(self):
        return self.recruiters.toString()

    def seeJobseekersForGivenDay(self, day):
        jobseekersForGivenDay = Jobseekers()
        for jobseeker in self.jobseekers:
            if (jobseeker.appliedJobsFilterDay(day) != None):
                jobseekersForGivenDay.add(jobseeker)
        return jobseekersForGivenDay

    def aggregateStatisticsByJob(self, job): # I broke rule #1 and #5 (playing with privates).
        #returns dictionary(named statistics) - key = job (job needs some id #TODO), value = number of applications
        for jobseeker in self.jobseekers:
            for job in jobseeker.appliedJobs:
                if job not in statistics:
                    statistics[job] = 0
                statistics[job] += job.numberOfApplicants()
