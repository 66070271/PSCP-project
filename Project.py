"""PSCP project"""
import pandas as pd
def bmr(sex, age, height, weight):
    if sex == "Male":
        result = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    elif sex == "Female":
        result = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    return result
def test():
    df = pd.read_excel(r'food_data.xlsx')
    print(df)
test()