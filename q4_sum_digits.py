#Filename: q4_sum_digits.py
#Author: Tan Di Sheng
#Created: 20130122
#Modified: 20130122
#Description: This program is used to read an integer between 0 and 1000
#and adds all the digits in the integer.

print("This application is used to sum up all the digits in an interger")

#This creates a loop so that the user can use the application
#for multiple conversions without restarting the application
while (True):

    while (True):

        #The input of the integer is here
        iInput = input("\nPlease input the integer here: ")
        #This checks whether the input is an integer
        if iInput.isdigit():
            break
        else:
            print("Please input an integer.")
        
    #This calculates the total sum of each individual digit in the input
    iInput = int(iInput)
    onesOutput = iInput % 10
    tens = (iInput - onesOutput) / 10
    tensOutput = tens % 10
    hundreds = iInput - tensOutput*10 - onesOutput
    hundredsOutput = hundreds / 100
    print(onesOutput + tensOutput + hundredsOutput)

    #creates an option for the user to continue or stop using
    #the application.
    contorquit = input("Continue? (Type yes or no): ")
    if contorquit == "no":
        quit()
    elif contorquit == "yes":
        continue
