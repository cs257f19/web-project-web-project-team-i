import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    def setUp(self):
        self.ds = DataSource()

    //Adding all MetaCritic in the decade
    //Making sure all the years have a value
    //Making sure the average is the actual average
    
    def AvgScoreEqualsTestAvgScore:
        start = 2000
        end = 2010
        avg = 91.2
        self.assertEqual(ds.getBestPicAvgScore(start,end), avg)

    def AvgScoreNotEqualTestAvgScore:
        start = 2000
        end = 2010
        avg = 70.0
        self.assertNotEqual(ds.getBestPicAvgScore(start, end), avg)

    