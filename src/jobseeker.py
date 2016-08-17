from src.jobs import Jobs

class Jobseeker:

    def __init__(self, name, id): # I broke rule #8 here!
        self.name = name
        self.savedJobs = Jobs()
        self.appliedJobs = Jobs()
        self.id = id

    def __str__(self):
        return str(self.name)

    def apply(self, job, application):
        if not (application.validName()):
            raise Exception('This is not your resume.')
        job.apply(application)
        self.appliedJobs.add(job)

    def saveJob(self, job):
        self.savedJobs.add(job)

    def seeAppliedJobs(self):
        return self.appliedJobs

    def seeSavedJobs(self):
        return self.savedJobs

    def appliedJobsFilterByDay(self, day):
        return self.appliedJobs.filterByDay(day)

    def isMatchingJobseeker(self, jobseeker):
        return (jobseeker.id == self.id)
