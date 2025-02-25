import tkinter as tk
from tkinter import messagebox

def calculate_relative_atomic_mass():
    try:
        atomic_mass = float(entry_mass.get())
        atomic_mass_unit = 1.66e-24
        relative_atomic_mass = atomic_mass / atomic_mass_unit
        label_result.config(text=f"Relative Atomic Mass: {relative_atomic_mass:.2f}")
        determine_group(relative_atomic_mass)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def determine_group(relative_atomic_mass):
    rounded_mass = round(relative_atomic_mass)
    
    if rounded_mass in [1]:
        group = "No group"
    elif rounded_mass in [7, 23, 39, 85, 133, 223]:
        group = "Group 1A"
    elif rounded_mass in [9, 24, 40, 88, 137, 226]:
        group = "Group 2A"
    elif rounded_mass in [11, 27, 70, 115, 204]:
        group = "Group 3A"
    elif rounded_mass in [12, 28, 73, 119, 207]:
        group = "Group 4A"
    elif rounded_mass in [14, 31, 75, 122, 209]:
        group = "Group 5A"
    elif rounded_mass in [16, 32, 79, 128, 209]:
        group = "Group 6A"
    elif rounded_mass in [19, 35, 80, 127, 210]:
        group = "Group 7A"
    elif rounded_mass in [4, 20, 40, 84, 131, 222]:
        group = "Group 8A"
    else:
        group = "Unknown"
    
    label_group.config(text=f"Element belongs to: {group}")

# GUI Setup
root = tk.Tk()
root.title("Atomic Mass Calculator")
root.geometry("400x250")

tk.Label(root, text="Enter Atomic Mass (g):").pack(pady=5)
entry_mass = tk.Entry(root)
entry_mass.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_relative_atomic_mass).pack(pady=10)

label_result = tk.Label(root, text="Relative Atomic Mass: ")
label_result.pack(pady=5)

label_group = tk.Label(root, text="Element belongs to: ")
label_group.pack(pady=5)

root.mainloop()
