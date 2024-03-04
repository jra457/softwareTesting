# Convert weight input
def weight(inW):
  return inW * 0.45

# Convert height input
def height(inH):
  newH = inH * 0.025

  newH = newH ** 2

  return newH

# Calculate bmi
def bmi(w, h):
   return (weight(w) / height(h))


def main():
  
  print("BMI Calculator for Adults (20+ Years Old)")

  # weight = input("Enter your weight in pounds: ")
  weight = 125 # For testing

  # height = input("Enter your height in inches: ")
  height = 63 # For testing

  bmiVal = bmi(weight, height)

  if (bmiVal < 18.5):
    print(f"BMI: {bmiVal:.1f}, Cateogry: Underweight")
  elif (bmiVal < 24.9):
    print(f"BMI: {bmiVal:.1f}, Cateogry: Healthy weight")
  elif(bmiVal < 29.9):
    print(f"BMI: {bmiVal:.1f}, Cateogry: Overweight")
  else:
    print(f"BMI: {bmiVal:.1f}, Cateogry: Obesity")




if __name__ == "__main__":
  main()
