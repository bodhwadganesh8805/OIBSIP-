# BMI body mass Index


Height = input("Enter your Height in Centemeters: ")
try:
    Height=float(Height)
except ValueError:
    print("Please Enter only Numbers!")
Weight = input("Enter your Weight in kg: ")
try:
    Weight=float(Weight)
except ValueError:
    print("Please Enter only Numbers!")

Height = Height/100
BMI = Weight/(Height*Height)

print("Your Body Mass Index is:",BMI)

if(BMI>0):
    if(BMI<=16):
        print("you are Severely Underweight")
    elif(BMI<18.5):
        print("you are Undeweight")
    elif(BMI<=25):
        print("you are Healthy ")
    elif(BMI<=30):
        print("you are overweight")
    else:
        print("you are severely overweight")

else:
    print("Enter valid details...")       
