#!/usr/bin/env python3

# Lucia Pal, 2016

'''
Unit tests for name.py
'''
from name import Name, FirstName, LastName

import unittest

class FirstNameTest(unittest.TestCase):

    def test(self):
        firstName = FirstName('Luke')
        self.assertEqual('Luke', str(firstName))


class LastNameTest(unittest.TestCase):

    def test(self):
        lastName = LastName('Skywalker')
        self.assertEqual('Skywalker', str(lastName))


class NameTest(unittest.TestCase):

    def test(self):
        firstName = FirstName('Luke')
        lastName = LastName('Skywalker')
        name = Name(firstName, lastName)
        self.assertEqual('Luke Skywalker', str(name))


if __name__ == '__main__':
	unittest.main()
