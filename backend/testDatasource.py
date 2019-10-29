import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    def setUp(self):
        self.ds = DataSource()

    //Adding all MetaCritic in the decade
    //Making sure all the years have a value
    //Making sure the average is the actual average
    
    def testAvgScoreEqualsTestAvgScore:
        avgScore = 74
        return if avgScore == 