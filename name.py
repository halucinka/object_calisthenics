class FirstName:

    def __init__(self, firstNameString):
        self.firstNameString = firstNameString

    def toString(self):
        return self.firstNameString


class LastName:

    def __init__(self, lastNameString):
        self.lastNameString = lastNameString

    def toString(self):
        return self.lastNameString


class Name:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def toString(self):
        return (self.firstName.toString() + ' ' + self.lastName.toString())
