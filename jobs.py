from applications import Applications


class Job(object):

    def __init__(self, recruiter, title):
        self.recruiter = recruiter
        self.title = title
        self.applications = Applications()

    def apply(self, application):
        pass # This function should not be called.

#    def createJob(self, type):
#        if (type == 'JReq'):
#            return JReq(self.recruiter, self.title)
#        if (type == 'ATS'):
#            return ATS(self.recruiter, self.title)

    def numberOfApplications(self):
        return self.applications.size()

    def __str__(self):
        return self.title

    def appliedAtDay(self, day):
        applicationsForDay = self.applications.filterByDay(day)
        return (not applicationsForDay.empty())


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
            if (job.appliedAtDay(day)):
                jobsFilterByDay.add(job)
        return jobsFilterByDay

    def __str__(self):
        return '\n'.join([str(job) for job in self.jobs]) + '\n'
