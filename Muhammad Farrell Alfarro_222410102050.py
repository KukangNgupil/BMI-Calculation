#Hitung BMI

weight = int(input("Input your Weight(kg): "))
height = int(input("Input your Height(cm): "))

bmi = weight/((height/100)**2)

print("----------")
print(f"Your BMI Score is {bmi}")

if bmi <18.5 :
    print("BMI calculation results say that you are Underweight")
elif 18.5 <= bmi <= 24.9 :
    print("BMI calculation results say that you are Normal Weight")
elif 25.0 <= bmi <= 29.9 :
    print("BMI calculation results say that you are Overweight")
elif 30.0 <= bmi <= 34.9 :
    print("BMI calculation results say that you are Obesity class I")
elif 35.0 <= bmi <= 39.9 :
    print("BMI calculation results say that you are Obesity class II")
else :
    print("BMI calculation results say that you are Obesity class III")
print("----------")
