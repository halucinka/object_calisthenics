class Jobseekers:

    def __init__(self):
        self.jobseekers = []

    def add(self, jobseeker):
        for js in self.jobseekers:
            if (js.isMatchingJobseeker(jobseeker)):
                return
        self.jobseekers.append(jobseeker)

    def seeJobseekers(self): #wrong
        return self.jobseekers

    def jobseekersForGivenDay(self, day):
        jobseekersForGivenDay = Jobseekers()
        for jobseeker in self.jobseekers:
            if (jobseeker.appliedJobsFilterByDay(day) != None):
                jobseekersForGivenDay.add(jobseeker)
        return jobseekersForGivenDay



    def __str__(self):
        return '\n'.join(str(jobseeker) for jobseeker in self.jobseekers) + '\n'
