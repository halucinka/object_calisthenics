from applications import Applications
class Job(object):

    def __init__(self, recruiter, title):
        self.recruiter = recruiter
        self.title = title
        self.applications = Applications()

    def apply(self, application):
        pass # This function should not be called.

    def createJob(self, type):
        if (type == 'JReq'):
            return JReq(self.recruiter, self.title)
        if (type == 'ATS'):
            return ATS(self.recruiter, self.title)

    def numberOfApplicants(self):
        return self.applications.size()

    def toString(self):
        return self.title


class JReq(Job):

    def __init__(self, recruiter, title):
        super().__init__(recruiter, title)

    def apply(self, application):
        if (not application.hasResume()):
            raise Exception('JReq application needs a resume.')
        self.applications.add(application)



class ATS(Job):

    def __init__(self, recruiter, title):
        super().__init__(recruiter, title)

    def apply(self, application):
        self.applications.add(application)

class Jobs:

    def __init__(self):
        self.jobs = []

    def add(self, job):
        self.jobs.append(job)

    def filterByDay(self, day): # I broke rule #1.
        jobsFilterByDay = Jobs()
        for job in self.jobs:
            if (job.appliedAtDay):
                jobsFilterByDay.add(job)
        return jobsFilterByDay

    def toString(self):
        string = ''
        for job in self.jobs:
            string += job.toString() + '\n'
        return string
