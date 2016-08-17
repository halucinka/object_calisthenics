from src.applications import Applications

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
