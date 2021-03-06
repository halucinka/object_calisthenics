#!/usr/bin/env python3

'''
Unit tests for name.py
'''
from src.name import Name
from src.firstName import FirstName
from src.lastName import LastName


import unittest

class NameTest(unittest.TestCase):

    def test(self):
        firstName = FirstName('Luke')
        lastName = LastName('Skywalker')
        name = Name(firstName, lastName)
        self.assertEqual('Luke Skywalker', str(name))


if __name__ == '__main__':
	unittest.main()
