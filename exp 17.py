fever=input("Fever(yes/no):").lower()
cough=input("Cough(yes/no):").lower
if fever=="Yes" and cough=="Yes":
    print("Possible infection;consult a doctor")
elif fever=="Yes":
    print("Medical evaluation recommended")
else:
    print("Insufficient information")
    
