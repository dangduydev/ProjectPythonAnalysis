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
from tkinter import filedialog


# cdd = pd.read_csv("./G308CDD_DAHP_OnlineRetail.csv", encoding="ISO-8859-1")
# global cdd


# Tạo đối tượng nhận diện giọng nói
r = sr.Recognizer()

# Tạo đối tượng tkinter
cdd_root = tk.Tk()
cdd_root.title("Ứng dụng EDA")
cdd_root.geometry("500x300")


# Tạo các hàm xử lý


def openTextFile():
    global filePath, cdd
    filePath = filedialog.askopenfilename(
        title="Chọn tệp CSV",
        filetypes=(("Text File (.txt)", "*.txt"), ("CSV File (.csv)", "*.csv")),
    )

    f1 = open(filePath, "r", encoding="utf-8")
    cdd = pd.read_csv(filePath, encoding="ISO-8859-1")
    f1.close()


def removeNullCols():
    # global cdd
    cdd.dropna(axis=1, inplace=True)
    messagebox.showinfo("Thông báo", "Đã bỏ các cột null")


def removeNullRows():
    # global cdd
    cdd.dropna(axis=0, inplace=True)
    messagebox.showinfo("Thông báo", "Đã bỏ các dòng null")


def renameCol(old_col, new_col):
    # global cdd

    result = messagebox.askquestion("Xác nhận", "Bạn có muốn lưu thay đổi không?")
    if result == "yes":
        cdd.rename(columns={str(old_col): str(new_col)}, inplace=True)
        rename_window.destroy()
    else:
        return
        # rename_window.destroy()


# Tạo cửa sổ để thực hiện đổi tên 1 cột
def renameColWindow():
    global rename_window
    rename_window = tk.Toplevel(cdd_root)
    rename_window.title("Rename Column")
    rename_window.geometry("300x100")

    lbl_old_name_col = tk.Label(rename_window, text="Name of old column:")
    lbl_old_name_col.grid(column=0, row=0)

    lbl_new_name_col = tk.Label(rename_window, text="Name of new column:")
    lbl_new_name_col.grid(column=0, row=1)

    options = cdd.columns.values.tolist()
    cbx_old_name_col = ttk.Combobox(
        rename_window, values=options, width=20, state="readonly"
    )
    cbx_old_name_col.grid(column=1, row=0)
    cbx_old_name_col.current(0)

    txt_new_name_col = tk.Text(rename_window, width=20, height=1)
    txt_new_name_col.grid(column=1, row=1)

    def submit():
        old_col = cbx_old_name_col.get()
        new_col = txt_new_name_col.get("1.0", "end-1c")
        renameCol(old_col, new_col)

    btn_submit = tk.Button(rename_window, text="Submit", command=submit)
    btn_submit.grid(column=1, row=2)


def showShape():
    lbl_output.config(text=cdd.shape)


def calPercentNull():
    # global cdd
    result = cdd.isnull().sum() * 100 / len(cdd)
    return result.sort_values(ascending=0)


def showPercentNull():
    _percent_null = calPercentNull()
    lbl_output.config(text=_percent_null)
    result = messagebox.askquestion(
        "Question", "Bạn có muốn xuất dưới dạng biểu đồ không?"
    )
    if result == "yes":
        plt.bar(_percent_null.index, _percent_null.values)
        plt.xticks(rotation=90)
        plt.ylabel("%pgiá trị null")
        plt.show()


def dropCol(name_col):
    result = messagebox.askquestion(
        "Thông báo", "Bạn chắc chắn muốn xóa cột" + str(name_col)
    )
    if result == "yes":
        cdd.drop(columns=str(name_col), inplace=True)


def dropColWindow():
    global drop_col_window
    drop_col_window = tk.Toplevel(cdd_root)
    drop_col_window.title("Drop Column")
    drop_col_window.geometry("300x100")

    lbl_name_col = tk.Label(drop_col_window, text="Name column:")
    lbl_name_col.grid(column=0, row=0)

    options = cdd.columns.values.tolist()
    cbx_name_col = ttk.Combobox(
        drop_col_window, values=options, width=20, state="readonly"
    )
    cbx_name_col.grid(column=1, row=0)
    cbx_name_col.current(0)

    def submit():
        name_col = cbx_name_col.get()
        dropCol(name_col)

    btn_submit = tk.Button(drop_col_window, text="Submit", command=submit)
    btn_submit.grid(column=1, row=2)


def showDescription():
    lbl_output.config(text=cdd.describe())


# Set khoảng cách giữu các column
cdd_root.columnconfigure(0, minsize=50)
cdd_root.columnconfigure(1, minsize=50)

# Tạo các toolbox

btn_OpenTextFile = tk.Button(
    cdd_root, text="Open Text file", width=15, command=openTextFile
)
btn_OpenTextFile.grid(column=0, row=15)

lbl_output = tk.Label(cdd_root)
# lbl_output.grid(column=2, row=0)
lbl_output.place(x=200)

lbl_output_bar = tk.Label(cdd_root)
# lbl_output.grid(column=2, row=0)
lbl_output_bar.place(x=250)

btn_show_shape = tk.Button(cdd_root, text="Show Shape", width=15, command=showShape)
btn_show_shape.grid(column=0, row=0)

btn_rename = tk.Button(
    cdd_root, text="Rename Column", width=15, command=renameColWindow
)
btn_rename.grid(column=0, row=1)

btn_show_percent_null = tk.Button(
    cdd_root, text="Percent null", width=15, command=showPercentNull
)
btn_show_percent_null.grid(column=0, row=2)

btn_drop_col = tk.Button(cdd_root, text="Drop Column", width=15, command=dropColWindow)
btn_drop_col.grid(column=0, row=3)

btn_show_description = tk.Button(
    cdd_root, text="Show Description", width=15, command=showDescription
)
btn_show_description.grid(column=0, row=4)

cdd_root.mainloop()
