# MSU Software Q&A Spring 2022
# Assignment 2
# Cody Armand, cra252 
# 3/9/2022 

#Collect and store user input for height and weight
def BmiInput():
    global heightFT
    global heightIN 
    global weight 

    heightFT = input("Enter Height in feet: ")
    heightIN = input("Enter Height in inches: ")  
    weight = input("Enter weight in pounds: ")  

#If user input isn't numerical, print error message and ask for input again
def DataValid(): 
    isValid = False

    while not isValid: 
        if(heightFT.isdigit() == False): 
            print("Invalid Input, Try Again")
            BmiInput() 
        elif(heightIN.isdigit() == False): 
            print("Invalid Input, Try Again")
            BmiInput()
        elif(weight.isdigit() == False): 
            print("Invalid Input, Try Again")
            BmiInput() 
        else: 
            isValid = True


def Conversion(): 
    global BMI 

    BMI = round((int(weight) * 0.45) / (((int(heightFT) * 12) + int(heightIN)) * 0.025)**2, 1)  

def Output():  
    print("The BMI for a person who is " + str(heightFT) + "ft. " + str(heightIN) + "in. and weighs " + str(weight) + " pounds is " + str(BMI)) 

    if(BMI < 18.5): 
        print("Underweight") 
    elif(18.5 <= BMI < 25): 
        print("Normal Weight") 
    elif(25 <= BMI < 30):
        print("Overweight") 
    else: 
        print("Obese")


BmiInput() 
DataValid() 
Conversion()
Output()
