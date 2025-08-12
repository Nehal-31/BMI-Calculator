

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    if height <= 0 or weight <= 0:
        raise ValueError("Height and Weight must be positive numbers.")
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def categorize_bmi(bmi):
    """Return BMI category based on WHO standards."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"