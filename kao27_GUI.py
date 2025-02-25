import tkinter as tk
from tkinter import messagebox

def calculate_relative_atomic_mass(atomic_mass_str):
    try:
        atomic_mass = eval(atomic_mass_str.replace('^', '**'))  # แปลงอินพุตให้สามารถคำนวณได้
        atomic_mass_unit = 1.66e-24
        relative_atomic_mass = atomic_mass / atomic_mass_unit
        return relative_atomic_mass
    except:
        return None

def determine_group(relative_atomic_mass):
    group_mapping = {
        1: "No group", 7: "Group 1A", 23: "Group 1A", 39: "Group 1A", 85: "Group 1A", 133: "Group 1A", 223: "Group 1A",
        9: "Group 2A", 24: "Group 2A", 40: "Group 2A", 88: "Group 2A", 137: "Group 2A", 226: "Group 2A",
        11: "Group 3A", 27: "Group 3A", 70: "Group 3A", 115: "Group 3A", 204: "Group 3A",
        12: "Group 4A", 28: "Group 4A", 73: "Group 4A", 119: "Group 4A", 207: "Group 4A",
        14: "Group 5A", 31: "Group 5A", 75: "Group 5A", 122: "Group 5A", 209: "Group 5A",
        16: "Group 6A", 32: "Group 6A", 79: "Group 6A", 128: "Group 6A", 208: "Group 6A",
        19: "Group 7A", 36: "Group 7A", 80: "Group 7A", 127: "Group 7A", 210: "Group 7A",
        4: "Group 8A", 20: "Group 8A", 40: "Group 8A", 84: "Group 8A", 131: "Group 8A", 222: "Group 8A",
    }
    rounded_mass = round(relative_atomic_mass)
    return group_mapping.get(rounded_mass, "Unknown")

def on_calculate():
    atomic_mass_str = entry.get()
    relative_mass = calculate_relative_atomic_mass(atomic_mass_str)
    if relative_mass is None:
        messagebox.showerror("Error", "Invalid input! Please enter a valid atomic mass.")
    else:
        group = determine_group(relative_mass)
        result_label.config(text=f"Relative Atomic Mass: {relative_mass:.2f}\nElement belongs to: {group}")

# สร้าง GUI
root = tk.Tk()
root.title("Atomic Mass Calculator")

tk.Label(root, text="Enter Atomic Mass (g):").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=on_calculate).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
