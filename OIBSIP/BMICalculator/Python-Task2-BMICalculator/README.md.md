# BMI Calculator

## 1. Project Overview

The BMI Calculator is a Python desktop application developed using Tkinter. It calculates Body Mass Index (BMI) based on the user's weight and height.

The application also stores BMI records and displays a user's BMI history through a graphical chart.

## 2. Features

- User-friendly graphical interface.
- BMI calculation using weight and height.
- BMI category classification.
- Support for multiple named users.
- SQLite database for storing BMI records.
- BMI history visualization using Matplotlib.
- Input validation and error handling.

## 3. Technologies Used

- Python 3.12
- Tkinter
- SQLite
- Matplotlib
- Visual Studio Code

## 4. BMI Calculation Formula

BMI = Weight (kg) / Height (m)²

## 5. BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5–24.9 | Normal |
| 25–29.9 | Overweight |
| 30 or above | Obese |

## 6. Project Structure

```text
BMI_Calculator/
├── main.py
├── bmi_calculator.py
├── database.py
├── history.py
├── requirements.txt
├── README.md
└── screenshots/
```

## 7. Installation

Install the required package:

```bash
python -m pip install -r requirements.txt
```

## 8. How to Run

Run the application using:

```bash
python main.py
```

## 9. Database

The application uses SQLite to store user names, weight, height, BMI values, categories, and recorded dates.

## 10. Author

Your Name

## 11. Internship

Oasis Infobyte

Python Programming Track

Task 2 – BMI Calculator

## 12. Disclaimer

BMI is a screening measure and should not be used as a substitute for professional medical advice.