#Filename: q3_miles_to_kilometre.py
#Author: Tan Di Sheng
#Created: 20130122
#Modified: 20130122
#Description: This program is used to convert the input from miles
#into kilometers

print("""This is an application used to convert a distance in terms
of miles to a distance in terms of kilometres""")

#This creates a loop so that the user can use the application
#for multiple conversions without restarting the application
while (True):

    while (True):

        #The input of distance in miles is here
        mInput = input("\nPlease input the distance in miles here: ")
        try:
            float(mInput)
        except:
            print("Please input a number")
        else:
            break

    #Changes input to a float so that the conversion can be done
    mInput = float(mInput)

    #The conversion of miles to kilometers is done here
    kOutput = mInput * 1.60934

    print(str(mInput) + " miles is equals to " + "{0:5.3f}".format(kOutput)
    + " kilometers")

    #Allows the user to choose whether to continue or stop using
    #the application.
    contorquit = input("Continue? (Type yes or no): ")
    if contorquit == "no":
        quit()
    elif contorquit == "yes":
        continue
