from flask import Blueprint, render_template, request, flash, redirect, url_for
from model import preprocess_and_predict

bp = Blueprint('main', __name__)

@bp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect data from form
        age_input = (request.form.get('age'))
        gender = request.form.get('gender')       
        weight_input = (request.form.get('weight'))     
        height_input = (request.form.get('height'))      
        exercise = request.form.get('exercise')      
        smokinghist = request.form.get('smokinghist')     
        alcconsumption = request.form.get('alcconsumption')
        

        # Error handling
        errors = []
        if not age_input:
            errors.append('Please fill in your age!')
        else:
            try:
                age = int(age_input)
            except ValueError:
                errors.append('Please enter a valid integer for age!')

        if not gender:
            errors.append('Please select your gender!')

        if not weight_input:
            errors.append('Please fill in your weight!')
        else:
            try:
                weight = float(weight_input)
            except ValueError:
                errors.append('Please enter a valid number for weight!')

        if not height_input:
            errors.append('Please fill in your height!')
        else:
            try:
                height = float(height_input)
            except ValueError:
                errors.append('Please enter a valid number for height!')

        if not exercise:
            errors.append('Please state whether you exercise!')

        if not smokinghist:
            errors.append('Please state if you have smoked before')

        if not alcconsumption:
            errors.append('Please state how often you consume alcohol')

        if errors:
            return render_template('index.html', errors=errors)
        
        else:
            user_data = {
                'Exercise': exercise,
                'Sex': gender,
                'Age_Category': age,
                'Height_(cm)': height,
                'Weight_(kg)': weight,
                'Smoking_History': smokinghist,
                'Alcohol Consumption': alcconsumption
            }
                
        # Pass data to the model to predict the disease risk
        prediction = preprocess_and_predict(user_data)

        return render_template('index.html', prediction=prediction)
    return render_template('index.html') 