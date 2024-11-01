#This code is made from CodeDex: The Legend of Python.
weight = float(input("Enter Your Weight: ").strip());
height = float(input("Enter Your Height: ").strip());
x = weight/float(height * height)
if x < 18.5:
  print('Underweight')
elif x>=18.5 and x < 25:
  print('Normal')
elif x>=25 and x<30:
  print('Overweight')
elif x>=30:
  print('Obese')
