import unittest
import numpy as np
from bmiCalculator import weight, height, bmi

class TestCalculator(unittest.TestCase):

  def test_weight(self):
    self.assertEqual(weight(1), 0.45)


  def test_height(self):
    self.assertEqual(height(1), np.power(0.025, 2))


  def test_bmi(self):
    # Values not correct - update later
    self.assertEqual(bmi(1, 1), 0.45)



if __name__ == "__main__":
  unittest.main()