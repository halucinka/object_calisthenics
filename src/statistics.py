from src.jobseekers import Jobseekers

class Statistics:

    def __init__(self):
        self.statistics = {}

    def add(self, job, numberOfApplicants):
        if job.id not in self.statistics:
            self.statistics[job.id] = 0
        self.statistics[job.id] += numberOfApplicants

    def addById(self, jobId, numberOfApplicants):
        if jobId not in self.statistics:
            self.statistics[jobId] = 0
        self.statistics[jobId] += numberOfApplicants

    def addOtherStatistics(self, other):
        if (isinstance(other, self.__class__)):
            for id in other.statistics:
                self.addById(id, other.statistics[id])

    def __str__(self):
        return (('\n'.join(str(key) + ' ' + str(self.statistics[key]) for key in self.statistics)) + '\n' )
