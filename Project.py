from flask import Flask , render_template , request
app = Flask(__name__)
# ฟังก์ชันคำนวณ BMR โดยใช้สูตร Harris-Benedict
def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return round(bmr,2)

# ฟังก์ชันคำนวณ TDEE โดยใช้ BMR และระดับกิจกรรม
def calculate_tdee(bmr, activity_level):
    activity_levels = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'super_active': 1.9
    }
    return round(bmr * activity_levels[activity_level],2)

# ฟังก์ชันคำนวณ BMI
def calculate_bmi(weight, height):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return round(bmi,2)

# ฟังก์ชันคำนวณปริมาณสารอาหาร (โปรตีน, ไขมัน, และคาร์โบไฮเดรต)
def calculate_nutrition(goal, tdee):
    if goal == 'fat_loss':
        protein_ratio = 0.25
        fat_ratio = 0.25
        carbohydrate_ratio = 0.5
    elif goal == 'muscle_gain':
        protein_ratio = 0.3
        fat_ratio = 0.25
        carbohydrate_ratio = 0.45
    else:
        protein_ratio = 0.2
        fat_ratio = 0.25
        carbohydrate_ratio = 0.55

    calories_per_day = tdee
    protein_per_day = round((protein_ratio * calories_per_day) / 4,2)  # 1 กรัมโปรตีนมี 4 แคลอรี่
    fat_per_day = round((fat_ratio * calories_per_day) / 9,2)  # 1 กรัมไขมันมี 9 แคลอรี่
    carbohydrate_per_day = round((carbohydrate_ratio * calories_per_day) / 4,2)  # 1 กรัมคาร์โบไฮเดรตมี 4 แคลอรี่

    return {
        'calories_per_day': calories_per_day,
        'protein_per_day': protein_per_day,
        'fat_per_day': fat_per_day,
        'carbohydrate_per_day': carbohydrate_per_day
    }

@app.route("/")
def home():
    return render_template("realtdee.html")

@app.route("/calculate")
def calculate():
    return render_template("calculate.html")

@app.route("/result",methods = ['POST'])
def result():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age'])
    gender = request.form['gender']
    goal = request.form['goal']
    activity_level = request.form['activity_level']

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)
    bmi = calculate_bmi(weight, height)
    nutrition = calculate_nutrition(goal, tdee)

    return render_template('result.html', bmr=bmr, tdee=tdee, bmi=bmi, nutrition=nutrition)

@app.route("/contact")
def about():
    return render_template("contact.html")
if __name__ == "__main__":
    app.run(debug=True)