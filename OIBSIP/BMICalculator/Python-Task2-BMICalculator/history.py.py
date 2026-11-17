
import matplotlib.pyplot as plt
from database import get_user_records


def show_history(name):
    """Display the BMI history chart for a user."""

    records = get_user_records(name)

    if not records:
        print("No BMI history found for this user.")
        return

    dates = [record[4] for record in records]
    bmi_values = [record[2] for record in records]

    plt.figure(figsize=(9, 5))

    plt.plot(
        dates,
        bmi_values,
        marker="o",
        color="blue",
        linewidth=2
    )

    plt.title(f"BMI History for {name}")
    plt.xlabel("Date and Time")
    plt.ylabel("BMI")

    plt.xticks(rotation=30, ha="right")
    plt.grid(True)
    plt.tight_layout()

    plt.show()
