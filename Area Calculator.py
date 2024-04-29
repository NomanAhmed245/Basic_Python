#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a program to create area calculator
print("*** AREA CALCULATOR ***")
print(""" Press 1 to find the area of circle  
Press 2 to find the area of triangle
Press 3 to find the area of rectangle
Press 4 to find the area of square """)

choice = int(input("Whose area do you want to determine? "))
if choice == 1:
    diameter = float(input("Enter the diameter of the circle "))
    area = (22/7)*diameter**2
    print("This is the area of the area circle ",area)
elif choice == 2:
    base = float(input("Enter the base of the triangle "))
    hight = float(input("Enter the height of the triangle "))
    area = 0.5*base*hight
    print("This is the area of the triangle ",area)
elif choice == 3:
    width = float(input("Enter the width of the rectangle "))
    length = float(input("Enter the length of the rectangle "))
    area = length*width
    print("This is the area of the rectangle ",area)
elif choice == 4:
    side = float(input("Enter the side of the square "))
    area = side**2
    print("This is the area of the square ",area)
else:
    print("Not Found")


# In[ ]:




