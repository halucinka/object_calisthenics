#!/usr/bin/env python3

# Lucia Pal, 2016

'''
Unit tests for resume.py
'''
from resume import Resume

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
