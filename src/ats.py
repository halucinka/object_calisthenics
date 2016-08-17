from src.applications import Applications
from src.job import Job


class ATS(Job):

    def __init__(self, recruiter, title):
        super().__init__(recruiter, title)

    def apply(self, application):
        self.applications.add(application)
