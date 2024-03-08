"""
Name: Jacob Adams
NetID: jra457
GitHub: jra457
Run: pytest test_bmiCalculator.py
"""
import unittest
import numpy as np
from bmiCalculator import weight, height, bmi

# Average male height: 5'9" = 69"
# Average female height: 5'4" = 64"

class TestCalculator(unittest.TestCase):

  def test_weight(self):
    # Test at weight = 1
    self.assertEqual(weight(1), 0.45)


  def test_height(self):
    # Test at height = 1
    self.assertEqual(height(1), np.power(0.025, 2))


  def test_bmi(self):
    # Test at weight & height = 1
    self.assertEqual(bmi(1, 1), np.divide(0.45, np.power(0.025, 2)))
  
    # Test at weight = 1, height = 69"
    self.assertEqual(bmi(1, 69), np.divide(np.multiply(1, 0.45), np.power(np.multiply(69, 0.025), 2)))

    # ~ Underweight Boundary Test
    # Test at weight = 122.1, height = 69"
    self.assertEqual(bmi(122.1, 69), np.divide(np.multiply(122.1, 0.45), np.power(np.multiply(69, 0.025), 2)))

    # ~ Healthy Weight Boundary Test
    # Test at weight = 122.4, height = 69"
    self.assertEqual(bmi(122.4, 69), np.divide(np.multiply(122.4, 0.45), np.power(np.multiply(69, 0.025), 2)))
    # Test at weight = 164.6, height = 69"
    self.assertEqual(bmi(164.6, 69), np.divide(np.multiply(164.6, 0.45), np.power(np.multiply(69, 0.025), 2)))

    # ~ Overweight Boundary Test
    # Test at weight = 164.7, height = 69"
    self.assertEqual(bmi(164.7, 69), np.divide(np.multiply(164.7, 0.45), np.power(np.multiply(69, 0.025), 2)))
    # Test at weight = 197.7, height = 69"
    self.assertEqual(bmi(197.7, 69), np.divide(np.multiply(197.7, 0.45), np.power(np.multiply(69, 0.025), 2)))

    # ~ Obese Boundary Test
    # Test at weight = 197.8, height = 69"
    self.assertEqual(bmi(197.8, 69), np.divide(np.multiply(197.8, 0.45), np.power(np.multiply(69, 0.025), 2)))



if __name__ == "__main__":
  unittest.main()