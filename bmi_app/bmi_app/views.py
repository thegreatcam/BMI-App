 
from django.shortcuts import render
import math

def bmi(request):
    bmi = 0.0
    weight = request.POST.get('weight')
    height = request.POST.get('height')

    if weight and height:
        weight = float(weight)
        height = float(height)
        weight = convertW(weight)
        height = convertH(height)
        bmi = calcBMI(weight, height)

    classification = getClass(bmi)

    return render(request, 'bmi.html', {'bmi': bmi, 'classification': classification})

def convertW(w):
    #conversion from pounds to kilograms
    w = int(w) * 0.454
    return w

def convertH(h):
    #conversion from inches to meters squared
    h = int(h) * 0.0254
    h = pow(h, 2)
    return h

def calcBMI(w, h):
    bmi = float(w/h)
    bmi = format(bmi, ".2f")
    bmi = float(bmi)
    return bmi

def getClass(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"
