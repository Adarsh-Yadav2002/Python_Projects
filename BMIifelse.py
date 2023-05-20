Height=float(input("Enter the value in cm :-"))
Weight=float(input("Enter the value in kg :-"))
BMI=Weight/(Height/100)**2
print("The body Mass Index is:-", BMI)

if BMI <= 18.5:
       print("You are underweight")
elif BMI<= 24.9:
       print("You are Healthy")
elif BMI<= 29.9:
       print("You are at Overweight")
else :
      print("shiiittt obese")