class Jobseekers:
    '''singleton'''

    def __init__(self):
        self.jobseekers = []

    def add(self, jobseeker):
        self.jobseekers.append(jobseeker)

    def toString(self):
        string = ''
        for jobseeker in self.jobseekers:
            string += jobseeker.toString() + '\n'
        return string
