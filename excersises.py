# import random
# import calendar

# print(f"The ramdom number is : {random.randint(1, 200)}")

# #from kilometer to miles

# kilometer = float(input("Enter the kilometers: "))

# convert = 0.621371

# miles = kilometer * convert

# print(f"{kilometer} kilometers is equals to {miles} miles")

# #write a program to convert celsius to farenheit

# celsius = float(input("Enter the temperature in celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# print(f"{celsius} celsius is equals to {fahrenheit} fahrenheit")

# #display calendar
# year = int(input("Enter the year: "))
# month = int(input("Enter the month in numbers: "))

# cal = (calendar.month(year, month))

# print(cal)

#calculate the quadratic equation (-b +- (b^2 - 4ac)^1/2)/2a

import math

a = float(input("Enter the value for a: "))
b = float(input("Enter th evalue for b: "))
c = float(input("Enter the value for c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant))/ 2*a
    root2 = (-b - math.sqrt(discriminant))/ 2*a
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2} ")

elif discriminant==0:
    root = -b/2*a
    print(f"Root: {root}")

else:
    real = -b/2*a
    imaginary = math.sqrt(abs(discriminant))
    print(f"Root 1: {real} + {imaginary}i")
    print(f"Root 2: {real} - {imaginary}j")