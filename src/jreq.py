from src.applications import Applications
from src.job import Job

class JReq(Job):

    def __init__(self, recruiter, title, id):
        super().__init__(recruiter, title, id)

    def apply(self, application):
        if (not application.hasResume()):
            raise Exception('JReq application needs a resume.')
        self.applications.add(application)
