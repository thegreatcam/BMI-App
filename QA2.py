import math
#must use shebang to run as shell script
bmi=0.0
weight=input("Enter a weight(pounds):")
height=input("Enter a height(inches):")
print("\n")

weight=float(weight)
height=float(height)

def convertW(w):
    #conversion from pounds to kilograms
    w=int(w)*0.454
    return w

def convertH(h):
    #conversion from inches to meters squared
    h=int(h)*0.0254
    h=pow(h,2)
    
    return h

weight=convertW(weight)
height=convertH(height)

def calcBMI(w,h):
    bmi=float(w/h)
    bmi=format(bmi,".2f")
    bmi=float(bmi)
    return bmi

bmi=calcBMI(weight,height)
 
print("Your BMI is",bmi)
print("\n")

def getClass(bmi):
    cl="none"
    if(bmi<18.5):
        cl="Underweight"
        
    elif((bmi>=18.5) and (bmi<=24.9)):
        cl="Normal weight"
        
    elif((bmi>=25) and (bmi<=29.9)):
        cl="Overweight"
         
    elif(bmi>=30):
      cl="Obese"
    else:
        return
    return cl

print(getClass(bmi))