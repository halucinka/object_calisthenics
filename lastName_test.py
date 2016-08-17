#!/usr/bin/env python3

'''
Unit tests for lastName.py
'''
from src.lastName import LastName

import unittest


class LastNameTest(unittest.TestCase):

    def test(self):
        lastName = LastName('Skywalker')
        self.assertEqual('Skywalker', str(lastName))

if __name__ == '__main__':
	unittest.main()
