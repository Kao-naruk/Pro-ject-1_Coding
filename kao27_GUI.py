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
        1: "ไม่มีหมู่", 7: "หมู่ 1A", 23: "หมู่ 1A", 39: "หมู่ 1A", 85: "หมู่ 1A", 133: "หมู่ 1A", 223: "หมู่ 1A",
        9: "หมู่ 2A", 24: "หมู่ 2A", 40: "หมู่ 2A", 88: "หมู่ 2A", 137: "หมู่ 2A", 226: "หมู่ 2A",
        11: "หมู่ 3A", 27: "หมู่ 3A", 70: "หมู่ 3A", 115: "หมู่ 3A", 204: "หมู่ 3A",
        12: "หมู่ 4A", 28: "หมู่ 4A", 73: "หมู่ 4A", 119: "หมู่ 4A", 207: "หมู่ 4A",
        14: "หมู่ 5A", 31: "หมู่ 5A", 75: "หมู่ 5A", 122: "หมู่ 5A", 209: "หมู่ 5A",
        16: "หมู่ 6A", 32: "หมู่ 6A", 79: "หมู่ 6A", 128: "หมู่ 6A", 208: "หมู่ 6A",
        19: "หมู่ 7A", 36: "หมู่ 7A", 80: "หมู่ 7A", 127: "หมู่ 7A", 210: "หมู่ 7A",
        4: "หมู่ 8A", 20: "หมู่ 8A", 40: "หมู่ 8A", 84: "หมู่ 8A", 131: "หมู่ 8A", 222: "หมู่ 8A",
    }
    rounded_mass = round(relative_atomic_mass)
    return group_mapping.get(rounded_mass, "ไม่ทราบ")

def on_calculate():
    atomic_mass_str = entry.get()
    relative_mass = calculate_relative_atomic_mass(atomic_mass_str)
    if relative_mass is None:
        messagebox.showerror("ข้อผิดพลาด", "ป้อนค่ามวลอะตอมให้ถูกต้อง (ใช้ *, ^ สำหรับการคำนวณ)")
    else:
        group = determine_group(relative_mass)
        result_label.config(text=f"มวลอะตอมสัมพัทธ์: {relative_mass:.2f}\nธาตุนี้อยู่ใน: {group}")

# สร้าง GUI
root = tk.Tk()
root.title("เครื่องคำนวณมวลอะตอม")
root.configure(bg="pink")

tk.Label(root, text="ป้อนมวลอะตอมที่ผู้ใช้ได้มาจากโจทย์ (g):", font=("Arial", 14, "bold"), bg="pink").pack()
entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

tk.Button(root, text="คำนวณ", command=on_calculate, font=("Arial", 14), bg="light pink").pack()
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="pink")
result_label.pack()

tk.Label(root, text="** ใส่ค่าเฉพาะ 1 อะตอม เช่น (2.656*10^-23) **", font=("Arial", 12, "bold"), fg="red", bg="pink").pack()

root.mainloop()



