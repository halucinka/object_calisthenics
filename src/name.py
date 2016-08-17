from src.firstName import FirstName
from src.lastName import LastName

class Name:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return (str(self.firstName) + ' ' + str(self.lastName))
