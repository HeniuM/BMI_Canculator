from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        gender = request.form['gender']
        bmi = calculate_bmi(weight, height)

        recommended_bmi_range = get_recommended_bmi_range(gender)

        return render_template('result.html', bmi=bmi, recommended_bmi_range=recommended_bmi_range)
    return render_template('index.html')


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def get_recommended_bmi_range(gender):
    if gender == 'male':
        return "Recommended BMI range for men: 18.5 - 24.9"
    elif gender == 'female':
        return "Recommended BMI range for women: 18.5 - 24.9"
    else:
        return "Recommended BMI range: 18.5 - 24.9"


if __name__ == '__main__':
    app.run(debug=True)
