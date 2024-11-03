#Area_Calculator.py
import math
#Shapes
Triangle = 0.0
Rectangle = 0.0
Square = 0.0
Circle = 0.0
#Equation constants
side = 0.0
length = 0.0
width = 0.0
height = 0.0
base = 0.0
radius = 0.0
pi = math.pi
#Selection
Select = 0
print('==================')
print('Area Calculator 📐')
print('==================')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

while True:
    Select = int(input('Choose out of the 5 options: '))
    try:
        if Select == 1:
            print('You have chosen the Triangle Shape.')
            height = float(input('Please input the height: '))
            base = float(input('Please input the base: '))
            Triangle = (height*base)/2
            print(f"The area is: {Triangle}")
        elif Select == 2:
            print('You have chosen the Rectangle Shape.')
            length = float(input('Please input the length: '))
            width = float(input('Please input the width: '))
            Rectangle = (length*width)
            print(f"The area is: {Rectangle}")
        elif Select == 3:
            print('You have chosen the Sqaure Shape: ')
            side = float(input('Please input the side: '))
            Square = side ** 2
            print(f"The area is: {Square}")
        elif Select == 4:
            print('You have chosen the Circle Shape: ')
            radius = float(input('Please input the radius: '))
            Circle = (radius**2)*pi
            print(f"The area is: {Circle}")
        elif Select == 5:
            print('You have quit the program')
            break
        else:
            print('Input invalid, Please input (1,5)')
    except ValueError:
        print('Error in Value, Please input (1,5)')
