#Filename: q2_calc_cylinder_volume.py
#Author: Tan Di Sheng
#Created: 20130121
#Modified: 20130121
#Description: This program reads the radius and length of a cylinder and
#computes its volume.

#Imports in the module required for pi
import math
print("""This application is used to calculate the base area and volume of
a cylinder using its radius and length.""")

#Creates a loop for the user to use the application repeatedly without
#restarting the application.
while (True):

    #Creates a loop to check whether floats are entered.
    while (True):
        rInput = input("\nPlease input the radius of the cylinder: ")
        lInput = input("Please input the length of the cylinder: ")
        try:
            float(rInput) and float(lInput)
        except:
            print("Please input a number")
        else:
            break

    rInput = float(rInput)
    lInput = float(lInput)

    aInput = rInput * rInput * math.pi
    print("The base area of the cylinder is: " + "{0:5.2f}".format(aInput))

    vInput = aInput * lInput
    print("The total volume of the cylinder is: " + "{0:5.2f}".format(vInput))

    #Allows the user to choose whether to continue or stop using
    #the application.
    contorquit = input("Continue? (Type yes or no): ")
    if contorquit == "no":
        quit()
    elif contorquit == "yes":
        continue
    
