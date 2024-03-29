import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    def setUp(self):
        self.ds = DataSource()

    #Adding all MetaCritic in the decade
    #Making sure all the years have a value
    #Making sure the average is the actual average
    
# testcase1: Adding all MetaCritic in the decade
    def AvgScoreEqualsTestAvgScore(self):
        ds = self.ds
        start = 2000
        end = 2010
        avg = 91.2
        self.assertEqual(ds.getBestPicAvgScore(start,end), avg)

# testcase2: Making sure all the years have a value
    def AvgScoreNotEqualTestAvgScore(self):
        ds = self.ds
        start = 2000
        end = 2010
        avg = 70.0
        self.assertNotEqual(ds.getBestPicAvgScore(start, end), avg)

# testcase3: Making sure the average is the actual average
    def testNoValue(self):
        ds = self.ds
        start = 2100
        end = 2110
        msg = "Something went wrong when executing the query."
        self.assertEqual(ds.getBestPicAvgScore(start, end), msg)

if __name__ == "__main__":
	unittest.main()