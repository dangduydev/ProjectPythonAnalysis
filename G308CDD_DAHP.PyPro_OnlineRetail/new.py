import tkinter as cdd_tk
from tkinter import messagebox
import numpy as np
import speech_recognition as sr
from tkinter import ttk
from gtts import gTTS
import playsound
import os
import pandas as pd
from scipy import stats
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.preprocessing import Binarizer
import cv2
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg
import os
import subprocess
import plotly.graph_objs as go
import plotly.offline as pyoff
import plotly.io as pio
import matplotlib.pyplot as plt
import io
import plotly.express as px


class Window(cdd_tk.Tk):
    def __init__(self):
        super().__init__()
        self.G337CDD_FILE = os.path.abspath("") + "\G337CDD.mp3"
        self.title("Cao Dang Duy 08")
        self.geometry("630x270")
        self.radio = cdd_tk.IntVar()
        self.btnExit = cdd_tk.Button(self, text="Exit", command=self.on_closing)
        self.btnExit.place(x=140, y=30, w=90, h=50)
        self.lb1 = cdd_tk.Label(
            self, text="Nhập yêu cầu cần thực hiện: ", font=("Arial Bold", 10)
        )
        self.lb1.place(x=10, y=100)
        self.txtIn = cdd_tk.Entry(self)
        self.txtIn.place(x=230, y=100, w=130, h=20)
        self.button = cdd_tk.Button(self, text="Voice", command=self.new_window_voice)
        self.button.place(x=10, y=30, width=90, height=50)
        self.btnEDA = cdd_tk.Button(self, text="Thực Hiện", command=self.ThucHien_text)
        self.btnEDA.place(x=270, y=30, w=90, h=50)
        self.lbVoice = cdd_tk.Label(self, text="Bạn vừa nói", font=("Arial Bold", 10))
        self.lbVoice.place(x=10, y=160)
        self.lbtxt = cdd_tk.Label(
            self,
            text="\t  1. Phân tích dữ liệu thăm dò.\n\n2. Đóng ứng dụng.\n\n3. Xử lý ảnh video.\n\n  4. Game flappy Bird.",
            font=("Arial Bold", 10),
        )
        self.lbtxt.place(x=360, y=30)
        self.dict = {
            1: self.new_window_panel,
            2: self.on_closing,
            3: self.Cut_frame,
            4: self.game,
        }
        self.number = 0
        self.data = None
        self.dropcolum = None

    def game(self):
        subprocess.run(["python", "flappy.py"])

    def set_up(self):
        self.child = child_window(self)
        self.child.mainloop()

    def new_window_voice(self):
        form1 = cdd_tk.Toplevel()
        form1.title(
            "08 CAO ĐĂNG DUY, 211103C_HCMUTE, ĐỒ ÁN HỌC PHẦN: LẬP TRÌNH PYTHON, T5.2023"
        )
        form1.geometry("400x400")
        form1.resizable(cdd_tk.FALSE, cdd_tk.FALSE)
        label1 = cdd_tk.Label(
            form1,
            text="Chọn ngôn ngữ muốn nói: ",
            relief=cdd_tk.SUNKEN,
            font=("Arial Bold", 10),
            borderwidth=3,
            width=25,
            height=2,
            anchor="center",
        )
        radio1 = cdd_tk.Radiobutton(
            form1,
            text="Tiếng Anh",
            variable=self.radio,
            value=1,
            font=("Arial Bold", 14),
        )
        radio2 = cdd_tk.Radiobutton(
            form1,
            text="Tiếng Việt",
            variable=self.radio,
            value=2,
            font=("Arial Bold", 14),
        )
        btnnoi = cdd_tk.Button(form1, text="Bắt đầu nói:", command=self.Noi)
        btnphat = cdd_tk.Button(form1, text="Phát lại", command=self.Phat)
        label1.place(x=95, y=70)
        radio1.place(x=120, y=130)
        radio2.place(x=120, y=160)
        btnnoi.place(x=150, y=230)
        btnphat.place(x=162, y=270)

    def new_window_panel(self):
        panel = new_panel(self)
        panel.mainloop()

    def Noi(self):
        r37CDD = sr.Recognizer()
        with sr.Microphone() as Source:
            if self.radio.get() == 1:
                lang = "en"
            elif self.radio.get() == 2:
                lang = "vi"
            messagebox.showinfo("Thông báo", "Bấm OK để bắt đầu, trong 5s")
            file_audio_data = r37CDD.record(Source, duration=5)
            try:
                v37CDDlenh = r37CDD.recognize_google(file_audio_data, language=lang)
                if v37CDDlenh == "hài" or v37CDDlenh == "ai" or v37CDDlenh == "hi":
                    v37CDDlenh = "2"
                self.number = self.convert(v37CDDlenh)
                self.lbVoice.config(text=f"Bạn vừa nói là: {self.number}")
            except:
                self.lbVoice.config(text="Bạn nói gì tôi nghe không rõ....!")
            if os.path.isfile(f"G337CDD.mp3"):
                os.remove(f"G337CDD.mp3")
            self.G337CDD_FILE = "G337CDD.mp3"
            v37CDDText = gTTS(text=v37CDDlenh, lang=lang)
            v37CDDText.save(self.G337CDD_FILE)
            self.Phat()
            self.ThucThi()

    def Phat(self):
        playsound.playsound(self.G337CDD_FILE)

    def eda_click(self):
        result = self.txtIn.get("1.0", cdd_tk.END)
        if result == "":
            result = self.lbVoice.cget("text")
        self.lbEDA.config(text=result)
        self.txtIn.delete("1.0", cdd_tk.END)

    def on_closing(self):
        if cdd_tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    def convert(self, text):
        t = text.upper()
        if t == "MỘT" or t == "1":
            number = 1
        elif t == "HAI" or t == "2":
            number = 2
        elif t == "BA" or t == "3":
            number = 3
        elif t == "BỐN" or t == "4":
            number = 4
        elif t == "NĂM" or t == "5":
            number = 5
        elif t == "SÁU" or t == "6":
            number = 6
        return number

    def Cut_frame(self):
        cutframe = Cut_Frame(self)
        cutframe.mainloop()

    def ThucThi(self):
        self.dict[self.number]()

    def ThucHien_text(self):
        self.number = self.convert(self.txtIn.get())
        self.dict[self.number]()


class child_window(cdd_tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("XỬ LÝ  & CHỌN CÁC GIÁ TRỊ CẦN XỬ LÝ")
        self.geometry("800x500")
        self.resizable(cdd_tk.FALSE, cdd_tk.FALSE)
        cdd_tk.Label(self, text="Các Thuộc tính").place(x=15, y=15)
        self.txtSource = cdd_tk.Entry(self, width=30)  # Entry = cho nhập DL vào
        self.txtSource.place(x=120, y=15)
        self.btnAdd = cdd_tk.Button(self, text="Add", width=10, command=self.insert)
        self.btnAdd.place(x=320, y=10)
        self.direction_var = cdd_tk.StringVar(value="Thuận")
        self.forward_radio = cdd_tk.Radiobutton(
            self, text="Copy Forward", variable=self.direction_var, value="Thuận"
        )
        self.backward_radio = cdd_tk.Radiobutton(
            self, text="Copy Backward", variable=self.direction_var, value="Nghịch"
        )
        self.forward_radio.place(x=400, y=10)
        self.backward_radio.place(x=500, y=10)
        self.listbox1 = cdd_tk.Listbox(
            self, height=25, width=40, font="Consolas 8", selectmode=cdd_tk.EXTENDED
        )
        self.listbox1.bind(
            "<Button-3>", self.ShowPopupMenuA
        )  # <Button-3> : đăng ký sự kiện cho chuột phải của
        self.listbox1.place(x=15, y=50)
        self.listbox2 = cdd_tk.Listbox(
            self, height=25, width=40, font="Consolas 8", selectmode=cdd_tk.EXTENDED
        )
        self.listbox2.place(x=450, y=50)
        self.listbox2.bind("<Button-3>", self.ShowPopupMenuB)
        cdd_tk.Label(self, text="Số lượng").place(x=15, y=420)
        self.lblSoLuong = cdd_tk.Label(
            self,
            relief=cdd_tk.SUNKEN,
            font="Times 8",
            borderwidth=3,
            width=15,
            height=1,
        )
        self.lblSoLuong.place(x=100, y=420)
        self.btn1 = cdd_tk.Button(
            self, text="Copy to left", width=10, command=self.CopyToLeft
        )
        self.btn2 = cdd_tk.Button(
            self, text="Copy to right", width=10, command=self.CopyToRight
        )
        self.btn3 = cdd_tk.Button(
            self, text="Move to left", width=10, command=self.MoveToLeft
        )
        self.btn4 = cdd_tk.Button(
            self, text="Move to right", width=10, command=self.MoveToRight
        )
        self.btn5 = cdd_tk.Button(self, text="delete", width=10, command=self.Delete)
        self.btn1.place(x=320, y=70)
        self.btn2.place(x=320, y=110)
        self.btn3.place(x=320, y=150)
        self.btn4.place(x=320, y=190)
        self.btn5.place(x=320, y=230)
        self.btn_dropcolum = cdd_tk.Button(
            self, text="Chấp nhận", command=lambda: self.valueWasChose(parent)
        )
        self.btn_dropcolum.place(x=700, y=420)
        self.data = parent.data.columns.tolist()

    def on_closing(self):
        if cdd_tk.messagebox.askokcancel(
            "Đóng chương trình", "Bạn có chắc muốn thoát?"
        ):
            self.destroy()

    def insert(self):
        for dt in self.data:
            self.listbox1.insert(cdd_tk.END, dt)

    def total(self):
        dem = 0
        a = self.txtSource.get().strip()
        kq = a.ljust(20)
        # kq = chuỗi <-từ- chuỗi a = canh chỉnh left & bên right là fillchar(space) -> chiều dài width
        if a != "":
            self.listbox1.insert(cdd_tk.END, kq)
        # Đếm số dòng trong listbox
        dem = self.listbox1.size()
        # Điền thông tin vào label
        self.lblSoLuong.configure(text=dem)
        self.txtSource.delete(0, cdd_tk.END)

    def valueWasChose(self, parent):
        all_items = []
        for i in range(self.listbox2.size()):
            all_items.append(self.listbox2.get(i))

        parent.dropcolum = all_items
        print(parent.dropcolum)

    def CopyToRight(self):
        direction = self.direction_var.get()
        if direction == "Thuận":
            selection = self.listbox1.curselection()
            selection = sorted(selection)  # sắp xếp theo thứ tự tăng dần
            self.listbox2.insert(cdd_tk.END, *[self.listbox1.get(i) for i in selection])
        else:
            selection = self.listbox1.curselection()
            selection = sorted(selection, reverse=True)  # sắp xếp theo thứ tự giảm dần
            self.listbox2.insert(0, *[self.listbox1.get(i) for i in selection])
        self.listbox1.select_clear(0, cdd_tk.END)  # b
        self.total()

    def MoveToRight(self):
        direction = self.direction_var.get()
        selection = self.listbox1.curselection()
        selection = sorted(selection, reverse=(direction == "Nghịch"))
        if selection:
            values = [self.listbox1.get(i) for i in selection]
            self.listbox2.insert(cdd_tk.END, *values)
        if direction == "Thuận":
            for i in reversed(selection):
                self.listbox1.delete(i)
        else:
            for i in selection:
                self.listbox1.delete(i)
        self.listbox1.selection_clear(0, cdd_tk.END)
        self.total()

    def Delete(self):
        selection = self.listbox1.curselection()
        if len(selection) > 0:
            for i in reversed(selection):
                self.listbox1.delete(i)
        selection2 = self.listbox2.curselection()
        if len(selection2) > 0:
            for i in reversed(selection2):
                self.listbox2.delete(i)
        self.total()

    def CopyToLeft(self):
        direction = self.direction_var.get()
        if direction == "Thuận":
            selection = self.listbox2.curselection()
            selection = sorted(selection)
            if len(selection) > 0:
                values = [self.listbox2.get(i) for i in selection]
                self.listbox1.insert(cdd_tk.END, *values)
        else:
            selection = self.listbox2.curselection()
            selection = sorted(selection, reverse=True)
            if len(selection) > 0:
                values = [self.listbox2.get(i) for i in selection]
                self.listbox1.insert(cdd_tk.END, *values)
        self.total()

    def MoveToLeft(self):
        direction = self.direction_var.get()
        selection = self.listbox2.curselection()
        selection = sorted(selection, reverse=(direction == "Nghịch"))
        if selection:
            values = [self.listbox2.get(i) for i in selection]
            self.listbox1.insert(cdd_tk.END, *values)
            if direction == "Thuận":
                for i in reversed(selection):
                    self.listbox2.delete(i)
            else:
                for i in selection:
                    self.listbox2.delete(i)
        self.listbox2.selection_clear(0, cdd_tk.END)
        self.total()

    def ShowPopupMenuA(self, e):
        if self.listbox1.size() > 0:
            popMenu = cdd_tk.Menu(self.listbox1, tearoff=cdd_tk.FALSE)
            popMenu.add_command(label="Copy To Right", command=self.CopyToRight)
            popMenu.add_command(label="Move To Right", command=self.MoveToRight)
            popMenu.add_command(label="Delete", command=self.Delete)
            popMenu.tk_popup(
                e.x_root, e.y_root
            )  # phải thiết lập x_root, y_root để showpopup

    def ShowPopupMenuB(self, e):
        if self.listbox1.size() > 0:
            popMenu = cdd_tk.Menu(self.listbox2, tearoff=cdd_tk.FALSE)
            popMenu.add_command(label="Copy To Left", command=self.CopyToLeft)
            popMenu.add_command(label="Move To Left", command=self.MoveToLeft)
            popMenu.add_command(label="Delete", command=self.Delete)
            popMenu.tk_popup(
                e.x_root, e.y_root
            )  # phải thiết lập x_root, y_root để showpopup


class new_panel(cdd_tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("EDA")
        self.geometry("1200x700")
        self.resizable(cdd_tk.FALSE, cdd_tk.FALSE)
        self.data = pd.read_csv(
            ".\G308CDD_DAHP_OnlineRetail.csv", encoding="ISO-8859-1"
        )
        parent.data = self.data
        self.panel = cdd_tk.Frame(self, bg="white", bd=2, relief=cdd_tk.SUNKEN)
        self.panel.place(x=10, y=10, w=980, h=580)
        self.btn = cdd_tk.Button(
            self, text="Chọn Colum", command=lambda: self.EAD_column(parent), width=10
        )
        self.btn.place(x=1052, y=20)
        self.label = cdd_tk.Label(self, text="Chọn số cột lượng cột NULL:")
        self.label.place(x=1030, y=60)
        self.btn_data = cdd_tk.Button(
            self, text="Hiển thị", command=lambda: self.EDA_data(parent), width=10
        )
        self.btn_data.place(x=1052, y=550)
        self.text = cdd_tk.Text(self.panel)
        self.text.pack(fill=cdd_tk.BOTH, expand=True)
        self.flat = 0
        self.spin = cdd_tk.Spinbox(self, from_=1, to=8, width=10)
        self.spin.place(x=1052, y=100)
        self.btn_row = cdd_tk.Button(
            self, text="Xử Lý Row", command=lambda: self.EAD_row(parent), width=10
        )
        self.btn_row.place(x=1052, y=140)
        self.btn_dothi = cdd_tk.Button(
            self, text="Vẽ đồ thị", command=self.EDA_vedothi, width=10
        )
        self.btn_dothi.place(x=1052, y=180)
        self.btn_thaythe = cdd_tk.Button(
            self, text="Thay thế", command=self.EDA_thaythe, width=10
        )
        self.btn_thaythe.place(x=1052, y=220)
        self.btn_roirac = cdd_tk.Button(
            self, text="Rời rạc", command=self.EDA_roiRac, width=10
        )
        self.btn_roirac.place(x=1052, y=260)
        self.method_label = cdd_tk.Label(self, text="Select method:", width=10)
        self.method_label.place(x=1052, y=300)
        method_list = ["Chi2", "f_classif"]
        self.method = ttk.Combobox(self, values=method_list, state="readonly", width=10)
        self.method.place(x=1052, y=340)
        self.spin2 = cdd_tk.Spinbox(self, from_=1, to=8, width=10)
        self.spin2.place(x=1052, y=380)
        self.btn_phantich = cdd_tk.Button(
            self, text="PT Thăm dò", command=self.EDA_Thamdo, width=10
        )
        self.btn_phantich.place(x=1052, y=420)
        self.method.current(0)
        self.btn_dauvao = cdd_tk.Button(
            self, text="Lấy đầu vào", command=lambda: self.EDA_DauVao(parent), width=10
        )
        self.btn_dauvao.place(x=1052, y=460)
        self.btn_csv = cdd_tk.Button(
            self, text="Mở csv", width=10, command=self.open_csv
        )
        self.btn_csv.place(x=10, y=600)
        self.btn_reset = cdd_tk.Button(self, text="reset", command=self.reset, width=10)
        self.btn_reset.place(x=120, y=600)
        self.btn_vedothi = cdd_tk.Button(
            self, text="Vẽ Đồ thị", width=10, command=lambda: self.VeDoThi(parent)
        )
        self.btn_vedothi.place(x=230, y=600)

    def open_csv(self):
        df = pd.read_csv(".\G308CDD_DAHP_OnlineRetail.csv", encoding="ISO-8859-1")
        df = df.head(1000)
        self.text.delete("1.0", cdd_tk.END)
        self.text.insert(cdd_tk.END, df.to_string())
        self.panel.update()

    def reset(self):
        self.text.delete("1.0", cdd_tk.END)
        self.text.destroy()
        self.text = cdd_tk.Text(self.panel)
        self.text.pack(fill=cdd_tk.BOTH, expand=True)

    def VeDoThi(self, parent):
        form = Do_Thi(parent)
        form.mainloop()

    def EDA_Thamdo(self):
        text = self.method.get()
        if text == "Chi2":
            self.flat = 6
        else:
            self.flat = 7
        self.k = int(self.spin2.get())

    def EAD_row(self, parent):
        self.flat = 2
        child = child_window(parent)
        child.mainloop()

    def EAD_column(self, parent):
        self.flat = 1
        child = child_window(parent)
        child.mainloop()

    def EDA_vedothi(self):
        self.data = pd.read_csv(
            "G308CDD_DAHP_OnlineRetail.csv", encoding="unicode_escape"
        )
        self.data["TotalPrice"] = data.apply(
            lambda row: row["UnitPrice"] * row["Quantity"], axis=1
        )
        no_outliers_df = self.data[(np.abs(stats.zscore(self.data["TotalPrice"])) < 3)]
        fig, ax = plt.subplots()
        ax.boxplot(no_outliers_df["TotalPrice"])
        plt.show()

    def EDA_thaythe(self):
        self.flat = 4

    def EDA_roiRac(self):
        self.flat = 5

    def Lay_zcore(self, text):
        self.z = int(text.get())
        print(self.z)

    def EDA_DauVao(self, parent):
        self.flat = 8
        child = child_window(parent)
        child.mainloop()

    def EDA_data(self, parent):
        if self.flat == 0:
            self.text.insert(
                cdd_tk.END, "Kich thuoc cua DataFrame: {}\n".format(self.data.shape)
            )
            self.text.insert(cdd_tk.END, f"{self.data.head(5)}\n")

            self.text.insert(cdd_tk.END, str(self.data.count().sort_values()) + "\n")
        if self.flat == 1:
            self.data = self.data.drop(columns=parent.dropcolum, axis=1)
            self.text.insert(
                cdd_tk.END,
                "Kich thuoc cua DataFrame sau khi xu li cot NULL: {}\n".format(
                    self.data.shape
                ),
            )
            self.text.insert(cdd_tk.END, str(self.data.count().sort_values()) + "\n")
        if self.flat == 2:
            value = int(self.spin.get())
            self.data = self.data.dropna(thresh=value)
            self.data = self.data.dropna(subset=parent.dropcolum)
            self.text.insert(
                cdd_tk.END,
                "Kich thuoc cua DataFrame sau khi xu li dong null bằng cách cách loại bỏ giá trị NULL: {}\n".format(
                    self.data.shape
                ),
            )
            self.text.insert(cdd_tk.END, str(self.data.count().sort_values()) + "\n")

            self.text.insert(
                cdd_tk.END,
                "Thay the các giá trị null trong 3 cột Lịch sử, Đia Ly, GDCD bằng giá trị trung bình của từng côt \n",
            )
            for col in ["Dia Ly", "Lich Su", "GDCD"]:
                mean = self.data[col].mean()
                self.data[col].fillna(mean, inplace=True)
            self.text.insert(
                cdd_tk.END,
                "Kich thuoc cua DataFrame sau khi xu li thay the NULL: {}\n".format(
                    self.data.shape
                ),
            )
            self.text.insert(cdd_tk.END, str(self.data.count().sort_values()) + "\n")
            self.text.insert(cdd_tk.END, "Xử lý Z core \n")
            z = np.abs(stats.zscore(self.data._get_numeric_data()))
            self.zcore = z
            self.text.insert(cdd_tk.END, "MA TRAN Z-SCORE:\n")
            self.text.insert(cdd_tk.END, str(z) + "\n")
        if self.flat == 3:
            self.data = self.data[(self.zcore < self.z).all(axis=1)]
            self.text.insert(
                cdd_tk.END,
                "Kich thuoc cua DataFrame sau khi xu li cac gia tri ngoai le: {}\n".format(
                    self.data.shape
                ),
            )
        if self.flat == 4:
            self.text.insert(cdd_tk.END, "Thay thế các giá trị từ N1..N6 bằng 0..5 \n")
            self.data["Ma Ngoai Ngu"].replace(
                {"N1": 0, "N2": 1, "N3": 2, "N4": 3, "N5": 4, "N6": 5}, inplace=True
            )
            self.text.insert(cdd_tk.END, "Sau khi Thay the cac gia tri:\n")
            self.text.insert(cdd_tk.END, self.data.head(5))
            self.text.insert(cdd_tk.END, "\n")

        if self.flat == 5:
            self.text.insert(cdd_tk.END, "Chuẩn hóa rời rạc \n")
            rr = preprocessing.MinMaxScaler()  # xác định thang đo rr.fit(df)
            rr.fit(self.data)
            self.data = pd.DataFrame(
                rr.transform(self.data),
                index=self.data.index,
                columns=self.data.columns,
            )
            self.text.insert(cdd_tk.END, "\n")
            self.text.insert(cdd_tk.END, self.data.iloc[4:10])
            self.text.insert(cdd_tk.END, "\n")
            self.text.insert(
                cdd_tk.END,
                f"Độ lớn của bảng [frame] dữ liệu SAU KHI CHUẨN HÓA DL: {self.data.shape}\n",
            )
        if self.flat == 6:
            a = self.data.loc[:, self.data.columns != "Toan Hoc"]
            b = self.data[["Toan Hoc"]]
            binarizer = Binarizer(threshold=0.5)
            b = binarizer.fit_transform(b)
            selector = SelectKBest(chi2, k=self.k)
            selector.fit(a, b)
            a_new = selector.transform(a)
            selected_columns = a.columns[selector.get_support(indices=True)]
            self.text.insert("end", "Các đặc trưng quan trọng: \n")
            for col in selected_columns:
                self.text.insert("end", "-{}\n".format(col))
            self.text.insert(cdd_tk.END, str(a_new))
            self.text.insert(cdd_tk.END, "\n")
            self.data = self.data[selected_columns]
            parent.data = self.data
        if self.flat == 7:
            a = self.data.loc[:, self.data.columns != "Toan Hoc"]
            b = self.data["Toan Hoc"].ravel()
            selector = SelectKBest(f_classif, k=self.k)
            selector.fit(a, b)
            a_new = selector.transform(a)
            selected_columns = a.columns[selector.get_support(indices=True)]
            self.text.insert("end", "Các đặc trưng quan trọng: \n")
            for col in selected_columns:
                self.text.insert("end", "-{}\n".format(col))
            self.text.insert(cdd_tk.END, str(a_new))
            self.text.insert(cdd_tk.END, "\n")
            self.data = self.data[selected_columns]
            parent.data = self.data
        if self.flat == 8:
            self.text.insert("end", "Các thuộc tính đầu vào: \n")
            self.text.insert(cdd_tk.END, f"{str(parent.dropcolum)} \n")
            for col in parent.dropcolum:
                self.text.insert("end", "-{}\n".format(self.data[[col]]))


class Cut_Frame(cdd_tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("G337TranThanhCDD Cut Frame")
        self.geometry("380x350")
        self.resizable(cdd_tk.FALSE, cdd_tk.FALSE)
        self.buttonFolder = cdd_tk.Button(
            self, text="open", width=10, command=self.open_file
        )
        self.buttonFolder.place(x=140, y=20)
        self.lblFolder = cdd_tk.Label(
            self, text="Mở Folder", width=10, font="Arial 13", anchor=cdd_tk.CENTER
        )
        self.lblFolder.place(x=10, y=20)
        self.fileName = None
        self.txtFolderName = cdd_tk.Label(self, width=30, text="", relief=SUNKEN)
        self.txtFolderName.place(x=140, y=70)
        self.LableName = cdd_tk.Label(
            self, width=10, text="Ten folder", font="Arial 13", anchor=cdd_tk.CENTER
        )
        self.LableName.place(x=10, y=70)
        self.LableCatFrame = cdd_tk.Label(
            self,
            text="Cắt khi video đang chạy: ",
            font="Arial 13",
        )
        self.LableCatFrame.place(x=15, y=120)
        self.btnXulyAnh = cdd_tk.Button(
            self, text="Xử lý", width=10, command=self.capture_frames
        )
        self.btnXulyAnh.place(x=240, y=120)
        self.btnCatYMuon = cdd_tk.Button(
            self, text="Cắt ảnh", width=10, command=self.cut_frame
        )
        self.LableCatFrameTime = cdd_tk.Label(
            self,
            text="Cắt khi video tại thời điểm: ",
            font="Arial 13",
        )
        self.LableCatFrameTime.place(x=15, y=250)
        self.btnCatYMuon.place(x=110, y=300)
        self.spinbox = cdd_tk.Spinbox(self, from_=0, to=100, width=5)
        self.spinbox.place(x=20, y=303)
        self.lablespin = cdd_tk.Label(self, text="giây")
        self.lablespin.place(x=70, y=300)
        self.entr = cdd_tk.Entry(self, width=10, relief=cdd_tk.SUNKEN)
        self.btnfd = cdd_tk.Button(
            self, text="Chọn đường dẫn", command=self.Chon_duong_Dan
        )
        self.labelfd = cdd_tk.Label(self, text="Nhập tên")
        self.labelfd.place(x=10, y=180)
        self.entr.place(x=70, y=180)
        self.btnfd.place(x=160, y=180)
        # ...

    def Get_value(self):
        self.value = int(self.spinbox.get())

    def cut_frame(self):
        self.Get_value()
        cap = cv2.VideoCapture(self.fileName)
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        time_to_cut = self.value  # Giây
        frame_to_cut = int(time_to_cut * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_to_cut)
        ret, frame = cap.read()
        if not ret:
            print("Không thể đọc frame.")
            return
        cv2.imshow("Frame", frame)
        cv2.imwrite(self.savepath, frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Mở file",
            filetypes=(("mp4 file(.mp4)", "*.mp4"), ("mov file(.mov)", "*.mov")),
        )
        self.fileName = file_path
        self.txtFolderName.config(text=self.fileName)

    def Chon_duong_Dan(self):
        self.savepath = filedialog.askdirectory(title="Chọn folder lưu ảnh")
        self.savepath += f"/{self.entr.get()}.jpg"
        cdd_tk.Label(self, text=self.savepath).place(x=10, y=230)

    def capture_frames(self):
        # mở cửa sổ chọn file
        file_path = self.fileName
        # kiểm tra file có tồn tại không
        if not file_path:
            return
        # khởi tạo đối tượng VideoCapture
        cap = cv2.VideoCapture(file_path)
        # khởi tạo biến lưu frame số
        frame_count = 0
        # đọc frame từ video
        while True:
            # Đọc frame tiếp theo
            ret, frame = cap.read()

            # Kiểm tra nếu đọc hết video
            if not ret:
                break

            # Hiển thị frame
            cv2.imshow("frame", frame)

            # Chờ sự kiện từ bàn phím
            key = cv2.waitKey(25)

            # Kiểm tra nếu nhấn space
            if key == ord(" "):
                # Hiển thị hộp thoại để chọn vị trí và đặt tên file
                root = tk.Tk()
                root.withdraw()
                save_path = filedialog.asksaveasfilename(
                    defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")]
                )
                root.destroy()

                if save_path:
                    # Lưu frame vào file
                    cv2.imwrite(save_path, frame)
                    frame_count += 1

            # Kiểm tra nếu nhấn phím 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


class Do_Thi(cdd_tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Đồ thị z-core")
        self.geometry("300x300")
        self.frame = cdd_tk.Frame(self, width=400, height=400, relief=cdd_tk.SUNKEN)
        self.frame.place(x=10, y=10)
        self.button = cdd_tk.Button(
            self, text="Vẽ biểu đồ theo quốc gia", width=20, command=self.VeDoThi
        )
        self.button.place(x=10, y=10)
        self.button1 = cdd_tk.Button(
            self, text="Vẽ biểu đồ theo từng tháng", width=20, command=self.VeDoThi2
        )
        self.button1.place(x=10, y=40)
        self.dict_tinh = {
            "United Kingdom",
            "France",
            "Australia",
            "Portugal",
        }
        self.combobox = ttk.Combobox(self, values=list(self.dict_tinh), width=10)
        self.label1 = cdd_tk.Label(self, text="Chọn quốc gia")

        self.label1.place(x=200, y=10)
        self.combobox.place(x=200, y=50)

        self.data = pd.read_csv(
            ".\G308CDD_DAHP_OnlineRetail.csv", encoding="unicode_escape"
        )

    def VeDoThi(self):
        country = self.combobox.get()
        tx_country = self.data.query(f"Country == '{country}'").reset_index(drop=True)

        # create monthly active customers dataframe
        tx_country["InvoiceDate"] = pd.to_datetime(tx_country["InvoiceDate"])
        tx_country["InvoiceYearMonth"] = tx_country["InvoiceDate"].map(
            lambda date: 100 * date.year + date.month
        )
        tx_monthly_active = (
            tx_country.groupby("InvoiceYearMonth")["CustomerID"].nunique().reset_index()
        )

        # create bar plot of monthly active customers
        plot_data = [
            go.Bar(
                x=tx_monthly_active["InvoiceYearMonth"],
                y=tx_monthly_active["CustomerID"],
            )
        ]
        plot_layout = go.Layout(
            xaxis={"type": "category"}, title=f"Monthly Active Customers in {country}"
        )
        fig = go.Figure(data=plot_data, layout=plot_layout)
        img_bytes = pio.to_image(fig, format="png")
        img = plt.imread(io.BytesIO(img_bytes))
        plt.imshow(img)
        plt.show()

    def VeDoThi2(self):
        self.data["InvoiceDate"] = pd.to_datetime(self.data["InvoiceDate"])

        self.data["InvoiceYearMonth"] = self.data["InvoiceDate"].map(
            lambda date: 100 * date.year + date.month
        )

        self.data["Revenue"] = self.data["UnitPrice"] * self.data["Quantity"]
        tx_revenue = (
            self.data.groupby(["InvoiceYearMonth"])["Revenue"].sum().reset_index()
        )

        self.data["InvoiceDate"] = pd.to_datetime(self.data["InvoiceDate"])

        self.data["InvoiceYearMonth"] = self.data["InvoiceDate"].map(
            lambda date: 100 * date.year + date.month
        )

        self.data["Revenue"] = self.data["UnitPrice"] * self.data["Quantity"]
        tx_revenue = (
            self.data.groupby(["InvoiceYearMonth"])["Revenue"].sum().reset_index()
        )
        tx_revenue

        plot_data = [
            go.Scatter(
                x=tx_revenue["InvoiceYearMonth"],
                y=tx_revenue["Revenue"],
            )
        ]

        plot_layout = go.Layout(xaxis={"type": "category"}, title="Montly Revenue")
        fig = go.Figure(data=plot_data, layout=plot_layout)
        img_bytes = pio.to_image(fig, format="png")

        # Display the image using plt.imshow()
        img = plt.imread(io.BytesIO(img_bytes))
        plt.imshow(img)
        plt.show()


myWindow = Window()
myWindow.mainloop()
