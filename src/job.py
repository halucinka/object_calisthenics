from src.applications import Applications

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
