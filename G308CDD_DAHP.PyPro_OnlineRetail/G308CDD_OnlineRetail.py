import numpy as np
import pandas as pd
from scipy import stats
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
import matplotlib.pyplot as plt
import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox
from tkinter import ttk


cdd = pd.read_csv("./G308CDD_DAHP_OnlineRetail.csv", encoding="ISO-8859-1")

# Tạo đối tượng nhận diện giọng nói
r = sr.Recognizer()

# Tạo đối tượng tkinter
cdd_root = tk.Tk()
cdd_root.title("Ứng dụng EDA")
cdd_root.geometry("500x300")


# Tạo các hàm xử lý
def remove_null_col():
    global cdd
    cdd = cdd.dropna(axis=1)
    messagebox.showinfo("Thông báo", "Đã bỏ các cột null")


def remove_null_rows():
    global cdd
    cdd = cdd.dropna(axis=0)
    messagebox.showerror("Thông báo", "Đã bỏ các dòng null")


def rename_col(old_col, new_col):
    global cdd

    result = messagebox.askquestion("Xác nhận", "Bạn có muốn lưu thay đổi không?")
    if result == "yes":
        cdd = cdd.rename(columns={str(old_col): str(new_col)})
        rename_window.destroy()
    else:
        rename_window.destroy()


def rename_window():
    global rename_window
    rename_window = tk.Toplevel(cdd_root)
    rename_window.title("Rename Column")
    rename_window.geometry("300x100")

    lbl_old_name_col = tk.Label(rename_window, text="Name of old column:")
    lbl_old_name_col.grid(column=0, row=0)

    lbl_new_name_column = tk.Label(rename_window, text="Name of new column:")
    lbl_new_name_column.grid(column=0, row=1)

    options = cdd.columns.values.tolist()
    cbx_old_name_column = ttk.Combobox(
        rename_window, values=options, width=20, state="readonly"
    )
    cbx_old_name_column.grid(column=1, row=0)
    cbx_old_name_column.current(0)

    txt_new_name_column = tk.Text(rename_window, width=20, height=1)
    txt_new_name_column.grid(column=1, row=1)

    def submit():
        old_col = cbx_old_name_column.get()
        new_col = txt_new_name_column.get("1.0", "end-1c")
        rename_col(old_col, new_col)

    button_submit = tk.Button(rename_window, text="Submit", command=submit)
    button_submit.grid(column=1, row=2)


button = tk.Button(cdd_root, text="Click me!", command=rename_window)
button.grid(column=0, row=0)

cdd_root.mainloop()
