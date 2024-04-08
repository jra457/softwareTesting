from flask import Flask, request, render_template
from bmiCalculator import bmi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    w = float(request.form['weight'])
    h = float(request.form['height'])
    bmiVal, category = bmi(w, h)
    return render_template('result.html', bmi=bmiVal, category=category)

if __name__ == '__main__':
    app.run(debug=True)
