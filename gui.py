import tkinter as tk
from tkinter import messagebox
import subprocess
from datetime import datetime

root = tk.Tk()
root.title("Face Attendance System")
root.geometry("600x450")
root.configure(bg="#2C3E50")

title = tk.Label(
    root,
    text="FACE ATTENDANCE SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#2C3E50",
    fg="white"
)
title.pack(pady=20)

date_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#2C3E50",
    fg="white"
)
date_label.pack()

def update_time():
    now = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    date_label.config(text=now)
    root.after(1000, update_time)

update_time()

def register_user():
    subprocess.run(["python", "register_user.py"])

def train_model():
    subprocess.run(["python", "train_model.py"])
    messagebox.showinfo("Success", "Model Trained Successfully!")

def start_attendance():
    subprocess.run(["python", "attendance.py"])

btn1 = tk.Button(root,
                 text="Register User",
                 width=25,
                 height=2,
                 bg="#3498DB",
                 fg="white",
                 font=("Arial",12,"bold"),
                 command=register_user)
btn1.pack(pady=10)

btn2 = tk.Button(root,
                 text="Train Model",
                 width=25,
                 height=2,
                 bg="#27AE60",
                 fg="white",
                 font=("Arial",12,"bold"),
                 command=train_model)
btn2.pack(pady=10)

btn3 = tk.Button(root,
                 text="Start Attendance",
                 width=25,
                 height=2,
                 bg="#E67E22",
                 fg="white",
                 font=("Arial",12,"bold"),
                 command=start_attendance)
btn3.pack(pady=10)

btn4 = tk.Button(root,
                 text="Exit",
                 width=25,
                 height=2,
                 bg="#E74C3C",
                 fg="white",
                 font=("Arial",12,"bold"),
                 command=root.destroy)
btn4.pack(pady=10)

root.mainloop()