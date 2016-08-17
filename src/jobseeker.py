from src.jobs import Jobs

class Jobseeker:

    def __init__(self, name): # I broke rule #8 here!
        self.name = name
        self.savedJobs = Jobs()
        self.appliedJobs = Jobs()

    def __str__(self):
        return str(self.name)

    def apply(self, job, application):
        if not application.validName:
            raise Exception('This is not your resume.')
        job.apply(application)
        self.appliedJobs.add(job)

    def saveJob(self, job):
        self.savedJobs.add(job)

    def savedJobsToString(self):
        return self.savedJobs.toString()

    def appliedJobsToString(self):
        return self.appliedJobs.toString()

    def appliedJobsFilterDay(self, day):
        return self.appliedJobs.filterDay(day)
