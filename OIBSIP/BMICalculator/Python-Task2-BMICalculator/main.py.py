from history import show_history
import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt

from bmi_calculator import calculate_bmi
from database import create_table, save_record, get_user_records


def calculate():
    name = name_entry.get().strip()

    if not name:
        messagebox.showerror("Input Error", "Please enter your name.")
        return

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi, category = calculate_bmi(weight, height)

        save_record(name, weight, height, bmi, category)

        result_label.config(
            text=f"Your BMI: {bmi}\nCategory: {category}"
        )

    except ValueError as error:
        messagebox.showerror("Input Error", str(error))


def show_history():
    name = name_entry.get().strip()

    if not name:
        messagebox.showerror(
            "Input Error",
            "Enter your name to view your history."
        )
        return

    records = get_user_records(name)

    if not records:
        messagebox.showinfo(
            "No History",
            "No BMI records found for this name."
        )
        return

    dates = [record[4] for record in records]
    bmi_values = [record[2] for record in records]

    plt.figure(figsize=(9, 5))
    plt.plot(dates, bmi_values, marker="o", color="blue")
    plt.title(f"BMI History for {name}")
    plt.xlabel("Date and Time")
    plt.ylabel("BMI")
    plt.xticks(rotation=30, ha="right")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


create_table()

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x430")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

tk.Label(root, text="Name:", font=("Arial", 12)).pack()
name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Weight (kg):", font=("Arial", 12)).pack()
weight_entry = tk.Entry(root, font=("Arial", 12), width=30)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (metres):", font=("Arial", 12)).pack()
height_entry = tk.Entry(root, font=("Arial", 12), width=30)
height_entry.pack(pady=5)

calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate,
    font=("Arial", 12),
    bg="#2878B5",
    fg="white",
    width=20
)
calculate_button.pack(pady=15)

result_label = tk.Label(
    root,
    text="Your result will appear here",
    font=("Arial", 13, "bold"),
    fg="darkgreen"
)
result_label.pack(pady=10)

history_button = tk.Button(
    root,
    text="View BMI History",
    command=show_history,
    font=("Arial", 11),
    width=20
)
history_button.pack(pady=10)

root.mainloop()
