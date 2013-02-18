#Filename: q1_fahrenheit_to_celsius.py
#Author: Tan Di Sheng
#Created: 20130122
#Modified: 20130122
#Description: This program reads a Fahrenheit degree in double decimal
#from standard input, then converts it to Celsius and displays the result
#in standard output

print("""This is an application to convert a temperature reading in Fahrenheit
degree to Celsius degree""")

#Creates a loop to repeat calculation without restarting application.
while (True):
    
    fahrenheit = input("\nPlease input the temperature in Fahrenheit: ")
    #Creates a try and except loop to check that input is a number.
    try: 
        float(fahrenheit)
    except:
        print("Please input a number")
    else:
        fahrenheit = float(fahrenheit)
        celsius = (5/9) * (fahrenheit -32)
        print("The temperature in Celsius is: " + str(celsius))

    #creates an option for the user to continue or stop using
        #the application.
        contorquit = input("Continue? (Type yes or no): ")
        if contorquit == "no":
            quit()
        elif contorquit == "yes":
            continue
