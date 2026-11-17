
def calculate_bmi(weight, height):
    """Calculate BMI using weight in kilograms and height in metres."""
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    if height <= 0:
        raise ValueError("Height must be greater than zero.")

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category
