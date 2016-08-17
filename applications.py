class Application:

    def __init__(self, day, jobseeker, *resume): # I broke rule #8 here. (3 variables)
        self.resume = resume
        self.day = day
        self.jobseeker = jobseeker

    def hasResume(self):
        return (self.resume != None)

    def validName(self):
        if (self.jobseeker.toString() != self.resume.nameString):
            return False
        return True

class Applications:

    def __init__(self):
        self.applications = []

    def add(self, application):
        self.applications.append(application)

    def filterByDay(self, day):
        applicationsForDay = Application()
        for app in self.applications:
            if (app.day == day):
                applicationsForDay.add(app)
        return applicationsForDay

    def size(self):
        return len(self.applications)

    def empty(self):
        return (self.size() == 0)
