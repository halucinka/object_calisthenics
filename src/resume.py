class Resume:

    def __init__(self, resumeString, nameString):
        self.resumeString = resumeString
        self.nameString = nameString

    def __str__(self):
        return (self.nameString + '\n' + self.resumeString)

    def isMachingName(self, name):
        return self.nameString == name
