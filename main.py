
import tkinter as tk
from tkinter import messagebox
from bmi_utils import calculate_bmi, categorize_bmi
from storage import init_db, save_record
from visualize import plot_bmi_trend, plot_category_distribution

def calculate_and_save():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            raise ValueError("Name cannot be empty.")

        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        result_label.config(text=f"BMI: {bmi} ({category})")
        save_record(name, weight, height, bmi, category)
        messagebox.showinfo("Success", "Record saved successfully!")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def show_trend():
    plot_bmi_trend()

def show_distribution():
    plot_category_distribution()

init_db()


root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x300")


tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate & Save", command=calculate_and_save).pack(pady=5)
tk.Button(root, text="Show BMI Trend", command=show_trend).pack(pady=5)
tk.Button(root, text="Show Category Distribution", command=show_distribution).pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()