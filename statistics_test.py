#!/usr/bin/env python3

'''
Unit tests for recruiter.py
'''
from src.statistics import Statistics
from src.jreq import JReq
from src.ats import ATS
from src.name import Name
from src.firstName import FirstName
from src.lastName import LastName
from src.recruiter import Recruiter

import unittest

class companyTest(unittest.TestCase):
    def test(self):
        name = Name(FirstName('Master'), LastName('Yoda'))
        recruiter = Recruiter(name)
        jreq = JReq(recruiter, 'Jedi', 1) #TITLE SHOULD BE CLASS
        ats = JReq(recruiter, 'Sith', 2)

        s = Statistics()
        s.add(jreq, 2)
        s.addById(1, 3)
        s.add(ats, 47)
        self.assertEqual('1 5\n2 47\n', str(s))

        s2 = Statistics()
        s2.add(jreq, 2)
        s2.addOtherStatistics(s)
if __name__ == '__main__':
	unittest.main()
