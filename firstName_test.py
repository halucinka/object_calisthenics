#!/usr/bin/env python3

'''
Unit tests for firstName.py
'''
from src.name import Name
from src.firstName import FirstName
from src.lastName import LastName

import unittest

class FirstNameTest(unittest.TestCase):

    def test(self):
        firstName = FirstName('Luke')
        self.assertEqual('Luke', str(firstName))


if __name__ == '__main__':
	unittest.main()
