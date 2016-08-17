class Application:

    def __init__(self, day, jobseeker, resume = None): # I broke rule #8 here. (3 variables)
        self.resume = resume
        self.day = day
        self.jobseeker = jobseeker

    def hasResume(self):
        return (self.resume != None)

    def validName(self):
        return self.resume.isMachingName(str(self.jobseeker))
