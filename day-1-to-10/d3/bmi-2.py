# Day 3 Exercise: BMI 2.0

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi <= 18.5:
    print("Your BMI is {} and you are underweight.".format(bmi))
elif bmi <= 25:
    print("Your BMI is {} and you are normal weight.".format(bmi))
elif bmi <= 30:
    print("Your BMI is {} and you are overweight.".format(bmi))
elif bmi <= 35:
    print("Your BMI is {} and you are obese.".format(bmi))
else:
    print("Your BMI is {} and you are clinically obese.".format(bmi))
