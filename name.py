class FirstName:

    def __init__(self, firstNameString):
        self.firstNameString = firstNameString

    def __str__(self):
        return self.firstNameString


class LastName:

    def __init__(self, lastNameString):
        self.lastNameString = lastNameString

    def __str__(self):
        return self.lastNameString


class Name:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return (str(self.firstName) + ' ' + str(self.lastName))
