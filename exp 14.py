age=int(input("Enter age:"))
bmi=float(input("Enter BMI:"))
if age<18:
    print("Balanced growth diet")
elif bmi<18.5:
    print("Consult a dietitian")
elif bmi<25:
    print("Maintain a balanced diet")
else:
    print("Consult a dietitian")
