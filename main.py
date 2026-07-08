from tkinter import *
from tkinter import messagebox
from bmi import calculate_bmi
from database import create_database, save_record, get_records

# Create database
create_database()

# Create Window
root = Tk()
root.title("BMI Calculator")
root.geometry("450x550")
root.resizable(False, False)

# Variables
current_bmi = None
current_category = None

# ---------------- TITLE ----------------
Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    fg="blue"
).pack(pady=10)

# ---------------- NAME ----------------
Label(root, text="Name", font=("Arial", 12)).pack()

name_entry = Entry(root, width=35)
name_entry.pack(pady=5)

# ---------------- WEIGHT ----------------
Label(root, text="Weight (kg)", font=("Arial", 12)).pack()

weight_entry = Entry(root, width=35)
weight_entry.pack(pady=5)

# ---------------- HEIGHT ----------------
Label(root, text="Height (m)", font=("Arial", 12)).pack()

height_entry = Entry(root, width=35)
height_entry.pack(pady=5)

# ---------------- RESULT ----------------
result_label = Label(
    root,
    text="",
    font=("Arial", 13, "bold"),
    fg="green"
)
result_label.pack(pady=15)


# ---------------- CALCULATE ----------------
def calculate():

    global current_bmi, current_category

    try:

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi, category = calculate_bmi(weight, height)

        current_bmi = bmi
        current_category = category

        result_label.config(
            text=f"BMI : {bmi}\nCategory : {category}"
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid values."
        )


# ---------------- SAVE ----------------
def save():

    if current_bmi is None:
        messagebox.showwarning(
            "Warning",
            "Please calculate BMI first."
        )
        return

    name = name_entry.get()

    weight = float(weight_entry.get())
    height = float(height_entry.get())

    save_record(
        name,
        weight,
        height,
        current_bmi,
        current_category
    )

    messagebox.showinfo(
        "Success",
        "Record Saved Successfully!"
    )


# ---------------- HISTORY ----------------
def history():

    records = get_records()

    history_window = Toplevel(root)

    history_window.title("BMI History")

    history_window.geometry("600x300")

    text = Text(history_window)

    text.pack(fill=BOTH, expand=True)

    text.insert(
        END,
        "ID\tNAME\tWEIGHT\tHEIGHT\tBMI\tCATEGORY\n\n"
    )

    for row in records:
        text.insert(
            END,
            f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\n"
        )


# ---------------- CLEAR ----------------
def clear():

    name_entry.delete(0, END)
    weight_entry.delete(0, END)
    height_entry.delete(0, END)

    result_label.config(text="")


# ---------------- BUTTONS ----------------
Button(
    root,
    text="Calculate BMI",
    width=20,
    bg="green",
    fg="white",
    command=calculate
).pack(pady=5)

Button(
    root,
    text="Save",
    width=20,
    bg="blue",
    fg="white",
    command=save
).pack(pady=5)

Button(
    root,
    text="View History",
    width=20,
    bg="orange",
    fg="white",
    command=history
).pack(pady=5)

Button(
    root,
    text="Clear",
    width=20,
    bg="red",
    fg="white",
    command=clear
).pack(pady=5)

root.mainloop()