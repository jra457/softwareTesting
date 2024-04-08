"""
Name: Jacob Adams
NetID: jra457
GitHub: jra457
Run: python3 bmiCalculator.py
"""

# Convert weight input
def weight(inW):

  newW = inW * 0.45

  return newW



# Convert height input
def height(inH):
  newH = inH * 0.025

  newH = newH ** 2

  return newH



# Calculate bmi
def bmi(w, h):
  bmiVal = weight(w) / height(h)
  category = ""

  #if (bmiVal < 18.5):
  if (bmiVal < 18.4):
    category = "Underweight"
  elif (bmiVal < 24.9):
    category = "Healthy weight"
  elif(bmiVal < 29.9):
    category = "Overweight"
  else:
    category = "Obese"

  return bmiVal, category



# Get weight
def inputWeight():

  while True:
    print('Enter your weight in pounds:')
    weight = input()
    try:
        weight = float(weight)
    except:
        print('Please input your weight in pounds.')
        continue
    if weight <= 0:
        print('Please input a number greater than 0.')
        continue
    break

  return weight



# Get height
def inputHeight():

  while True:
    print('Enter your height in inches:')
    height = input()
    try:
        height = float(height)
    except:
        print('Please input your height in inches.')
        continue
    if height <= 0:
        print('Please input a number greater than 0.')
        continue
    break

  return height



if __name__ == "__main__":  
  print("BMI Calculator for Adults (20+ Years Old)")

  weight = inputWeight()

  height = inputHeight()

  bmiVal, category = bmi(weight, height)

  print(f"BMI: {bmiVal:.1f}, Category: {category}")

