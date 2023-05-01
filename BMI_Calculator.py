print("-----------BMI Calculator-----------")

def calculateBMI():
    h=float(input("Enter the height: "))
    w=float(input("Enter the weight: "))

    heightInMeters=h/100
    squareOfHeight=heightInMeters**2
    bmi=round((w/squareOfHeight),2)
    bmiTxt="Your BMI is : {}"
    print(bmiTxt.format(bmi))

    if(bmi<18.5):
        print("You are Under Weight")
    elif(bmi > 18.5 and bmi <24.9):
        print("You are normal")
    elif(bmi>25 and bmi < 29.9):
        print("You are Over Weight")
    else:
        print("You are Obese")

calculateBMI()