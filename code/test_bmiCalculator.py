"""
Name: Jacob Adams
NetID: jra457
GitHub: jra457
Run: pytest test_bmiCalculator.py
"""
import unittest
import numpy as np
from bmiCalculator import weight, height, bmi_val, bmiCategory

# Average male height: 5'9" = 69"

class TestCalculator(unittest.TestCase):

  def test_weight(self):
    # ~ Underweight Boundary Test
    # Test at weight = 122.1
    self.assertEqual(weight(122.1), np.multiply(122.1, 0.45))

    # ~ Healthy Weight Boundary Test
    # Test at weight = 122.4
    self.assertEqual(weight(122.4), np.multiply(122.4, 0.45))
    # Test at weight = 164.6
    self.assertEqual(weight(164.6), np.multiply(164.6, 0.45))

    # ~ Overweight Boundary Test
    # Test at weight = 164.7
    self.assertEqual(weight(164.7), np.multiply(164.7, 0.45))
    # Test at weight = 197.7
    self.assertEqual(weight(197.7), np.multiply(197.7, 0.45))

    # ~ Obese Boundary Test
    # Test at weight = 197.8
    self.assertEqual(weight(197.8), np.multiply(197.8, 0.45))



  def test_height(self):
    self.assertEqual(height(69), np.power(np.multiply(69, 0.025), 2))



  def test_bmi_val(self):
    # ~ Underweight Boundary Test
    # Test at weight = 122.1, height = 69"
    self.assertEqual(bmi_val(122.1, 69), np.divide(np.multiply(122.1, 0.45), np.power(np.multiply(69, 0.025), 2)))

    # ~ Healthy Weight Boundary Test
    # Test at weight = 122.4, height = 69"
    self.assertEqual(bmi_val(122.4, 69), np.divide(np.multiply(122.4, 0.45), np.power(np.multiply(69, 0.025), 2)))
    # Test at weight = 164.6, height = 69"
    self.assertEqual(bmi_val(164.6, 69), np.divide(np.multiply(164.6, 0.45), np.power(np.multiply(69, 0.025), 2)))

    # ~ Overweight Boundary Test
    # Test at weight = 164.7, height = 69"
    self.assertEqual(bmi_val(164.7, 69), np.divide(np.multiply(164.7, 0.45), np.power(np.multiply(69, 0.025), 2)))
    # Test at weight = 197.7, height = 69"
    self.assertEqual(bmi_val(197.7, 69), np.divide(np.multiply(197.7, 0.45), np.power(np.multiply(69, 0.025), 2)))

    # ~ Obese Boundary Test
    # Test at weight = 197.8, height = 69"
    self.assertEqual(bmi_val(197.8, 69), np.divide(np.multiply(197.8, 0.45), np.power(np.multiply(69, 0.025), 2)))



  def test_bmiCategory(self):
    # ~ Underweight Boundary Test
    # BMI = 18.4
    self.assertEqual(bmiCategory(18.3), "Underweight")

    # ~ Healthy Weight Boundary Test
    # BMI = 18.5
    self.assertEqual(bmiCategory(18.5), "Healthy weight")
    # BMI = 24.8
    self.assertEqual(bmiCategory(24.8), "Healthy weight")

    # ~ Overweight Boundary Test
    # BMI = 25.0
    self.assertEqual(bmiCategory(25.0), "Overweight")
    # BMI = 24.8
    self.assertEqual(bmiCategory(29.8), "Overweight")

    # ~ Obese Boundary Test
    # BMI = 29.9
    self.assertEqual(bmiCategory(29.9), "Obese")



if __name__ == "__main__":
  unittest.main()