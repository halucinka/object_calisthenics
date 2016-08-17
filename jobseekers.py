from jobs import Jobs
class Jobseeker:

    def __init__(self, name): # I broke rule #8 here!
        self.name = name
        self.savedJobs = Jobs()
        self.appliedJobs = Jobs()


    def toString(self):
        return self.name.toString()

    def apply(self, job, application):
        if not application.validName:
            raise Exception('This is not your resume.')
        job.apply(application)
        self.appliedJobs.add(job)

    def saveJob(self, job):
        self.savedJobs.add(job)

    def toStringSavedJobs(self):
        return self.savedJobs.toString()

    def toStringAppliedJobs(self):
        return self.appliedJobs.toString()

    def appliedJobsFilterDay(self, day):
        return self.appliedJobs.filterDay(day)



class Jobseekers:
    '''singleton'''

    def __init__(self):
        self.jobseekers = []

    def add(self, jobseeker):
        self.jobseekers.append(jobseeker)

    def toString(self):
        string = ''
        for jobseeker in self.jobseekers:
            string += jobseeker.toString() + '\n'
        return string
