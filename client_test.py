import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """
class TestGetRatio(unittest.TestCase):

    def test_normal_case(self):
        self.assertAlmostEqual(getRatio(10, 2), 5)
        self.assertAlmostEqual(getRatio(3, 2), 1.5)
        self.assertAlmostEqual(getRatio(5, 5), 1)

    def test_division_by_zero(self):
        self.assertIsNone(getRatio(10, 0))

    def test_zero_numerator(self):
        self.assertAlmostEqual(getRatio(0, 10), 0)

    def test_negative_values(self):
        self.assertAlmostEqual(getRatio(-10, 2), -5)
        self.assertAlmostEqual(getRatio(10, -2), -5)
        self.assertAlmostEqual(getRatio(-10, -2), 5)
    def test_float_values(self):
      self.assertAlmostEqual(getRatio(10.5, 2), 5.25)
      self.assertAlmostEqual(getRatio(5.5, 2.2), 2.5)
      self.assertAlmostEqual(getRatio(0.0, 2.5), 0.0)
      self.assertAlmostEqual(getRatio(3.14, 1.57), 2.0)
      self.assertAlmostEqual(getRatio(1.0, 0.5), 2.0)



if __name__ == '__main__':
    unittest.main()
