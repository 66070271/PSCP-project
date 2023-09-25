"""PSCP project"""
def bmr():
    sex = input("Enter your gender(Male/Female) : ")
    age = int(input("Enter your age : "))
    weight = float(input("Enter your weight(KG) : "))
    height = float(input("Enter Your height(CM) : "))
    if sex == "Male":
        result = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    elif sex == "Female":
        result = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    return result
bmr()