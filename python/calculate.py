from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# อ่านข้อมูลจาก Excel
food_data = pd.read_excel('food_data.xlsx')

# ฟังก์ชันคำนวณ TDEE
def calculate_tdee(weight, height, age, gender, activity_level):
    # คำนวณ TDEE ตามโครงสร้างที่คุณใช้
    # ...

# ฟังก์ชันคำนวณ BMR
def calculate_bmr(weight, height, age, gender):
    # คำนวณ BMR ตามโครงสร้างที่คุณใช้
    # ...

# ฟังก์ชันคำนวณ BMI
def calculate_bmi(weight, height):
    # คำนวณ BMI ตามโครงสร้างที่คุณใช้
    # ...

# หน้าหลัก
@app.route('/')
def tdee_calculator():
    return render_template('tdee.html')

# หน้าสำหรับคำนวณ TDEE, BMR, BMI, และแสดงปริมาณสารอาหารที่ควรได้รับต่อวัน
@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age'])
    gender = request.form['gender']
    activity_level = request.form['activity_level']

    # ทำการคำนวณ TDEE, BMR, BMI และปริมาณสารอาหารที่ควรได้รับต่อวัน

    return render_template('tdee.html', tdee=tdee, bmr=bmr, bmi=bmi, nutrition=nutrition)

# หน้าสำหรับคำนวณค่าพลังงานจากอาหารที่เลือก
@app.route('/calculate_nutrition', methods=['POST'])
def calculate_nutrition():
    selected_foods = request.form.getlist('selected_foods')
    servings = [float(request.form[f'{food}_servings']) for food in selected_foods]

    # คำนวณค่าพลังงานจากอาหารที่เลือก
    total_calories = 0
    food_info = []

    for food_name, serving in zip(selected_foods, servings):
        # ค้นหาข้อมูลอาหารจากไฟล์ Excel
        food_info = food_data[food_data['food_name'] == food_name].iloc[0]
        
        # คำนวณค่าพลังงานจากอาหารและเก็บข้อมูล
        calories = food_info['calories'] * serving
        total_calories += calories
        food_info['servings'] = serving
        food_info['calories'] = calories

    return render_template('nutrition.html', selected_foods=selected_foods, food_info=food_info, total_calories=total_calories)

if __name__ == '__main__':
    app.run(debug=True)
    