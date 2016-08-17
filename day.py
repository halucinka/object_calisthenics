class Day:
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return str(self.day)

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and (self.day == other.day))

    def __ne__(self, other):
        return not self.__eq__(other)
