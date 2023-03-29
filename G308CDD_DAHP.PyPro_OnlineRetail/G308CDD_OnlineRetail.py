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
    cdd.dropna(axis=1, inplace=True)
    messagebox.showinfo("Thông báo", "Đã bỏ các cột null")


def remove_null_rows():
    global cdd
    cdd.dropna(axis=0, inplace=True)
    messagebox.showinfo("Thông báo", "Đã bỏ các dòng null")


def rename_col(old_col, new_col):
    global cdd

    result = messagebox.askquestion("Xác nhận", "Bạn có muốn lưu thay đổi không?")
    if result == "yes":
        cdd.rename(columns={str(old_col): str(new_col)}, inplace=True)
        rename_window.destroy()
    else:
        return
        # rename_window.destroy()


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


def show_shape():
    lbl_output.config(text=cdd.shape)


def cal_percent_null():
    global cdd
    result = cdd.isnull().sum() * 100 / len(cdd)
    return result.sort_values(ascending=0)


def show_percent_null():
    _percent_null = cal_percent_null()
    lbl_output.config(text=_percent_null)
    result = messagebox.askquestion(
        "Question", "Bạn có muốn xuất dưới dạng biểu đồ không?"
    )
    if result == "yes":
        plt.bar(_percent_null.index, _percent_null.values)
        plt.xticks(rotation=90)
        plt.ylabel("%pgiá trị null")
        plt.show()


def drop_col(name_col):
    result = messagebox.askquestion(
        "Thông báo", "Bạn chắc chắn muốn xóa cột" + str(name_col)
    )
    if result == "yes":
        cdd.drop(columns=str(name_col), inplace=True)


def drop_col_window():
    global drop_col_window
    drop_col_window = tk.Toplevel(cdd_root)
    drop_col_window.title("Drop Column")
    drop_col_window.geometry("300x100")

    lbl_name_col = tk.Label(drop_col_window, text="Name column:")
    lbl_name_col.grid(column=0, row=0)

    options = cdd.columns.values.tolist()
    cbx_name_column = ttk.Combobox(
        drop_col_window, values=options, width=20, state="readonly"
    )
    cbx_name_column.grid(column=1, row=0)
    cbx_name_column.current(0)

    def submit():
        name_col = cbx_name_column.get()
        drop_col(name_col)

    button_submit = tk.Button(drop_col_window, text="Submit", command=submit)
    button_submit.grid(column=1, row=2)


def show_description():
    lbl_output.config(text=cdd.describe())


# Set khoảng cách giữu các column
cdd_root.columnconfigure(0, minsize=50)
cdd_root.columnconfigure(1, minsize=50)

# Tạo các toolbox

lbl_output = tk.Label(cdd_root)
# lbl_output.grid(column=2, row=0)
lbl_output.place(x=200)

lbl_output_bar = tk.Label(cdd_root)
# lbl_output.grid(column=2, row=0)
lbl_output_bar.place(x=250)

btn_show_shape = tk.Button(cdd_root, text="Show Shape", width=15, command=show_shape)
btn_show_shape.grid(column=0, row=0)

btn_rename = tk.Button(cdd_root, text="Rename Column", width=15, command=rename_window)
btn_rename.grid(column=0, row=1)

btn_show_percent_null = tk.Button(
    cdd_root, text="Percent null", width=15, command=show_percent_null
)
btn_show_percent_null.grid(column=0, row=2)

btn_drop_col = tk.Button(
    cdd_root, text="Drop Column", width=15, command=drop_col_window
)
btn_drop_col.grid(column=0, row=3)

btn_show_description = tk.Button(
    cdd_root, text="Show Description", width=15, command=show_description
)
btn_show_description.grid(column=0, row=3)

cdd_root.mainloop()
