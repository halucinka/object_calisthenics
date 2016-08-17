from src.applications import Applications
from src.job import Job

class JReq(Job):

    def __init__(self, recruiter, title):
        super().__init__(recruiter, title)

    def apply(self, application):
        if (not application.hasResume()):
            raise Exception('JReq application needs a resume.')
        self.applications.add(application)
