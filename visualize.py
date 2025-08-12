# visualize.py
import matplotlib.pyplot as plt
from storage import fetch_records

def plot_bmi_trend():
    """Plot BMI trend over time for all users."""
    records = fetch_records()
    if not records:
        print("No data to visualize.")
        return

    timestamps = [rec[6] for rec in records]
    bmi_values = [rec[4] for rec in records]

    plt.figure(figsize=(8, 5))
    plt.plot(timestamps, bmi_values, marker="o", linestyle="-", color="blue")
    plt.xticks(rotation=45, ha="right")
    plt.title("BMI Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.tight_layout()
    plt.show()

def plot_category_distribution():
    """Plot BMI category distribution."""
    records = fetch_records()
    if not records:
        print("No data to visualize.")
        return

    categories = [rec[5] for rec in records]
    category_counts = {cat: categories.count(cat) for cat in set(categories)}

    plt.figure(figsize=(6, 6))
    plt.pie(category_counts.values(), labels=category_counts.keys(), autopct="%1.1f%%", startangle=90)
    plt.title("BMI Category Distribution")
    plt.show()