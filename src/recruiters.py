from src.jobseekers import Jobseekers
from src.jobs import Jobs

class Recruiters:
    '''singleton'''

    def __init__(self):
        self.recruiters = []

    def add(self, recruiter):
        self.recruiters.append(recruiter)

    def toString(self):
        toString = ''
        for recruiter in self.recruiters:
            toString += recruiter.toString() + '\n'
        return toString
