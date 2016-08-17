#!/usr/bin/env python3

'''
Unit tests for resume.py
'''
from src.resume import Resume

import unittest

class ResumeTest(unittest.TestCase):

    def test(self):
        resume = Resume('The force is strong with me.', 'Luke Skywalker')
        self.assertEqual('Luke Skywalker\nThe force is strong with me.', str(resume))

    def testIsMatchingName(self):
        resume = Resume('The force is strong with me.', 'Luke Skywalker')
        self.assertTrue(resume.isMachingName('Luke Skywalker'))
        self.assertFalse(resume.isMachingName('Leia Organa'))

if __name__ == '__main__':
	unittest.main()
