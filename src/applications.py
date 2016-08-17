class Applications:

    def __init__(self):
        self.applications = []

    def add(self, application):
        self.applications.append(application)

    def filterByDay(self, day):
        applicationsForDay = Applications()
        for app in self.applications:
            if (app.day == day):
                applicationsForDay.add(app)
        return applicationsForDay

    def size(self):
        return len(self.applications)

    def empty(self):
        return (self.size() == 0)
