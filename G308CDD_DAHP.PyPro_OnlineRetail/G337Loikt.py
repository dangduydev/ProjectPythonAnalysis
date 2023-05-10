import tkinter as tk37Loi
from tkinter import messagebox
import numpy as np
import speech_recognition as sr37Loi
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


class Window(tk37Loi.Tk):
    def __init__(self):
        super().__init__()
        self.G337Loi_FILE = os.path.abspath("") + "\G337Loi.mp3"
        self.title("Tran Thanh Loi 37")
        self.geometry("630x270")
        self.radio = tk37Loi.IntVar()
        self.btnExit = tk37Loi.Button(self,
                                      text="Exit",
                                      command=self.on_closing)
        self.btnExit.place(x=140, y=80, w=90, h=50)
        self.lb1 = tk37Loi.Label(self,
                                 text="Nhập yêu cầu cần xử lý: ",
                                 font=("Arial Bold", 10))
        self.lb1.place(x=10, y=30)
        self.txtIn = tk37Loi.Entry(self)
        self.txtIn.place(x=230, y=30, w=130, h=20)
        self.button = tk37Loi.Button(self,
                                     text="Voice",
                                     command=self.new_window)
        self.button.place(x=10, y=80, width=90, height=50)
        self.btnEDA = tk37Loi.Button(self,
                                     text="Thực Thi",
                                     command=self.ThucThi_text)
        self.btnEDA.place(x=270, y=80, w=90, h=50)
        self.lbVoice = tk37Loi.Label(self,
                                     text="Nơi hiện thứ vừa nói",
                                     font=("Arial Bold", 10))
        self.lbVoice.place(x=10, y=160)
        self.lbtxt = tk37Loi.Label(
            self,
            text=
            "\t  1. Phân tích dữ liệu thăm dò.\n\n2. Đóng ứng dụng.\n\n3. Xử lý ảnh video.\n\n  4. Game flappy Bird.",
            font=("Arial Bold", 10))
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
        subprocess.run(['python', 'flappy.py'])

    def set_up(self):
        self.child = child_window(self)
        self.child.mainloop()

    def new_window(self):
        form1 = tk37Loi.Toplevel()
        form1.title(
            "37  TRẦN THÀNH LỢI, 211103B_HCMUTE, ĐỒ ÁN HỌC PHẦN: LẬP TRÌNH PYTHON, T5.2023"
        )
        form1.geometry('400x400')
        form1.resizable(tk37Loi.FALSE, tk37Loi.FALSE)
        label1 = tk37Loi.Label(form1,
                               text="Chọn ngôn ngữ muốn nói: ",
                               relief=tk37Loi.SUNKEN,
                               font=("Arial Bold", 10),
                               borderwidth=3,
                               width=25,
                               height=2,
                               anchor="center")
        radio1 = tk37Loi.Radiobutton(form1,
                                     text="Tiếng Anh",
                                     variable=self.radio,
                                     value=1,
                                     font=("Arial Bold", 14))
        radio2 = tk37Loi.Radiobutton(form1,
                                     text="Tiếng Việt",
                                     variable=self.radio,
                                     value=2,
                                     font=("Arial Bold", 14))
        btnnoi = tk37Loi.Button(form1, text='Bắt đầu nói:', command=self.Noi)
        btnphat = tk37Loi.Button(form1, text='Phát lại', command=self.Phat)
        label1.place(x=95, y=70)
        radio1.place(x=120, y=130)
        radio2.place(x=120, y=160)
        btnnoi.place(x=150, y=230)
        btnphat.place(x=162, y=270)

    def new_window_panel(self):
        panel = new_panel(self)
        panel.mainloop()

    def Noi(self):
        r37Loi = sr37Loi.Recognizer()
        with sr37Loi.Microphone() as Source:
            if self.radio.get() == 1:
                lang = 'en'
            elif self.radio.get() == 2:
                lang = 'vi'
            messagebox.showinfo("Cảnh báo", "Bấm OK để bắt đầu, trong 5s")
            file_audio_data = r37Loi.record(Source, duration=5)
            try:
                v37Loilenh = r37Loi.recognize_google(file_audio_data,
                                                     language=lang)
                if (v37Loilenh == 'hài' or v37Loilenh == 'ai'
                        or v37Loilenh == 'hi'):
                    v37Loilenh = '2'
                self.number = self.convert(v37Loilenh)
                self.lbVoice.config(text=f"Bạn vừa nói là: {self.number}")
            except:
                self.lbVoice.config(text="Bạn nói gì tôi nghe không rõ....!")
            if os.path.isfile(f"G337Loi.mp3"):
                os.remove(f"G337Loi.mp3")
            self.G337Loi_FILE = "G337Loi.mp3"
            v37LoiText = gTTS(text=v37Loilenh, lang=lang)
            v37LoiText.save(self.G337Loi_FILE)
            self.Phat()
            self.ThucThi()

    def Phat(self):
        playsound.playsound(self.G337Loi_FILE)

    def eda_click(self):
        result = self.txtIn.get("1.0", tk37Loi.END)
        if result == "":
            result = self.lbVoice.cget("text")
        self.lbEDA.config(text=result)
        self.txtIn.delete("1.0", tk37Loi.END)

    def on_closing(self):
        if tk37Loi.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    def convert(self, text):
        t = text.upper()
        if t == 'MỘT' or t == '1':
            number = 1
        elif t == 'HAI' or t == '2':
            number = 2
        elif t == 'BA' or t == '3':
            number = 3
        elif t == 'BỐN' or t == '4':
            number = 4
        elif t == 'NĂM' or t == '5':
            number = 5
        elif t == 'SÁU' or t == '6':
            number = 6
        return number

    def Cut_frame(self):
        cutframe = Cut_Frame(self)
        cutframe.mainloop()

    def ThucThi(self):
        self.dict[self.number]()

    def ThucThi_text(self):
        self.number = self.convert(self.txtIn.get())
        self.dict[self.number]()


class child_window(tk37Loi.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("XỬ LÝ  & CHỌN CÁC GIÁ TRỊ CẦN XỬ LÝ")
        self.geometry("800x500")
        self.resizable(tk37Loi.FALSE, tk37Loi.FALSE)
        tk37Loi.Label(self, text="Các Thuộc tính").place(x=15, y=15)
        self.txtSource = tk37Loi.Entry(self,
                                       width=30)  # Entry = cho nhập DL vào
        self.txtSource.place(x=120, y=15)
        self.btnAdd = tk37Loi.Button(self,
                                     text="Add",
                                     width=10,
                                     command=self.insert)
        self.btnAdd.place(x=320, y=10)
        self.direction_var = tk37Loi.StringVar(value="Thuận")
        self.forward_radio = tk37Loi.Radiobutton(self,
                                                 text="Copy Forward",
                                                 variable=self.direction_var,
                                                 value="Thuận")
        self.backward_radio = tk37Loi.Radiobutton(self,
                                                  text="Copy Backward",
                                                  variable=self.direction_var,
                                                  value="Nghịch")
        self.forward_radio.place(x=400, y=10)
        self.backward_radio.place(x=500, y=10)
        self.listbox1 = tk37Loi.Listbox(self,
                                        height=25,
                                        width=40,
                                        font="Consolas 8",
                                        selectmode=tk37Loi.EXTENDED)
        self.listbox1.bind("<Button-3>", self.ShowPopupMenuA
                           )  #<Button-3> : đăng ký sự kiện cho chuột phải của
        self.listbox1.place(x=15, y=50)
        self.listbox2 = tk37Loi.Listbox(self,
                                        height=25,
                                        width=40,
                                        font="Consolas 8",
                                        selectmode=tk37Loi.EXTENDED)
        self.listbox2.place(x=450, y=50)
        self.listbox2.bind("<Button-3>", self.ShowPopupMenuB)
        tk37Loi.Label(self, text="Số lượng").place(x=15, y=420)
        self.lblSoLuong = tk37Loi.Label(self,
                                        relief=tk37Loi.SUNKEN,
                                        font="Times 8",
                                        borderwidth=3,
                                        width=15,
                                        height=1)
        self.lblSoLuong.place(x=100, y=420)
        self.btn1 = tk37Loi.Button(self,
                                   text="copy to left",
                                   width=10,
                                   command=self.CopyToLeft)
        self.btn2 = tk37Loi.Button(self,
                                   text="copy to right",
                                   width=10,
                                   command=self.CopyToRight)
        self.btn3 = tk37Loi.Button(self,
                                   text="move left",
                                   width=10,
                                   command=self.MoveToLeft)
        self.btn4 = tk37Loi.Button(self,
                                   text="move right",
                                   width=10,
                                   command=self.MoveToRight)
        self.btn5 = tk37Loi.Button(self,
                                   text="delete",
                                   width=10,
                                   command=self.Delete)
        self.btn1.place(x=320, y=70)
        self.btn2.place(x=320, y=110)
        self.btn3.place(x=320, y=150)
        self.btn4.place(x=320, y=190)
        self.btn5.place(x=320, y=230)
        self.btn_dropcolum = tk37Loi.Button(
            self, text="Chấp nhận", command=lambda: self.valueWasChose(parent))
        self.btn_dropcolum.place(x=700, y=420)
        self.data = parent.data.columns.tolist()

    def on_closing(self):
        if tk37Loi.messagebox.askokcancel("Đóng chương trình",
                                          "Bạn có chắc muốn thoát?"):
            self.destroy()

    def insert(self):
        for dt in self.data:
            self.listbox1.insert(tk37Loi.END, dt)

    def total(self):
        dem = 0
        a = self.txtSource.get().strip()
        kq = a.ljust(20)
        # kq = chuỗi <-từ- chuỗi a = canh chỉnh left & bên right là fillchar(space) -> chiều dài width
        if (a != ""):
            self.listbox1.insert(tk37Loi.END, kq)
        #Đếm số dòng trong listbox
        dem = self.listbox1.size()
        #Điền thông tin vào label
        self.lblSoLuong.configure(text=dem)
        self.txtSource.delete(0, tk37Loi.END)

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
            self.listbox2.insert(tk37Loi.END,
                                 *[self.listbox1.get(i) for i in selection])
        else:
            selection = self.listbox1.curselection()
            selection = sorted(selection,
                               reverse=True)  # sắp xếp theo thứ tự giảm dần
            self.listbox2.insert(0, *[self.listbox1.get(i) for i in selection])
        self.listbox1.select_clear(0, tk37Loi.END)  # b
        self.total()

    def MoveToRight(self):
        direction = self.direction_var.get()
        selection = self.listbox1.curselection()
        selection = sorted(selection, reverse=(direction == "Nghịch"))
        if selection:
            values = [self.listbox1.get(i) for i in selection]
            self.listbox2.insert(tk37Loi.END, *values)
        if direction == "Thuận":
            for i in reversed(selection):
                self.listbox1.delete(i)
        else:
            for i in selection:
                self.listbox1.delete(i)
        self.listbox1.selection_clear(0, tk37Loi.END)
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
                self.listbox1.insert(tk37Loi.END, *values)
        else:
            selection = self.listbox2.curselection()
            selection = sorted(selection, reverse=True)
            if len(selection) > 0:
                values = [self.listbox2.get(i) for i in selection]
                self.listbox1.insert(tk37Loi.END, *values)
        self.total()

    def MoveToLeft(self):
        direction = self.direction_var.get()
        selection = self.listbox2.curselection()
        selection = sorted(selection, reverse=(direction == "Nghịch"))
        if selection:
            values = [self.listbox2.get(i) for i in selection]
            self.listbox1.insert(tk37Loi.END, *values)
            if direction == "Thuận":
                for i in reversed(selection):
                    self.listbox2.delete(i)
            else:
                for i in selection:
                    self.listbox2.delete(i)
        self.listbox2.selection_clear(0, tk37Loi.END)
        self.total()

    def ShowPopupMenuA(self, e):
        if self.listbox1.size() > 0:
            popMenu = tk37Loi.Menu(self.listbox1, tearoff=tk37Loi.FALSE)
            popMenu.add_command(label="Copy To Right",
                                command=self.CopyToRight)
            popMenu.add_command(label="Move To Right",
                                command=self.MoveToRight)
            popMenu.add_command(label="Delete", command=self.Delete)
            popMenu.tk_popup(
                e.x_root,
                e.y_root)  #phải thiết lập x_root, y_root để showpopup

    def ShowPopupMenuB(self, e):
        if self.listbox1.size() > 0:
            popMenu = tk37Loi.Menu(self.listbox2, tearoff=tk37Loi.FALSE)
            popMenu.add_command(label="Copy To Left", command=self.CopyToLeft)
            popMenu.add_command(label="Move To Left", command=self.MoveToLeft)
            popMenu.add_command(label="Delete", command=self.Delete)
            popMenu.tk_popup(
                e.x_root,
                e.y_root)  #phải thiết lập x_root, y_root để showpopup


class new_panel(tk37Loi.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('EDA')
        self.geometry('1200x700')
        self.resizable(tk37Loi.FALSE, tk37Loi.FALSE)
        self.data = pd.read_csv('.\diemthi2019_update.csv')
        parent.data = self.data
        self.panel = tk37Loi.Frame(self,
                                   bg='white',
                                   bd=2,
                                   relief=tk37Loi.SUNKEN)
        self.panel.place(x=10, y=10, w=980, h=580)
        self.btn = tk37Loi.Button(self,
                                  text="Chọn Colum",
                                  command=lambda: self.EAD_column(parent),
                                  width=10)
        self.btn.place(x=1052, y=20)
        self.label = tk37Loi.Label(self, text='Chọn số cột lượng cột NULL:')
        self.label.place(x=1030, y=60)
        self.btn_data = tk37Loi.Button(self,
                                       text="Hiển thị",
                                       command=lambda: self.EDA_data(parent),
                                       width=10)
        self.btn_data.place(x=1052, y=550)
        self.text = tk37Loi.Text(self.panel)
        self.text.pack(fill=tk37Loi.BOTH, expand=True)
        self.flat = 0
        self.spin = tk37Loi.Spinbox(self, from_=1, to=8, width=10)
        self.spin.place(x=1052, y=100)
        self.btn_row = tk37Loi.Button(self,
                                      text="Xử Lý Row",
                                      command=lambda: self.EAD_row(parent),
                                      width=10)
        self.btn_row.place(x=1052, y=140)
        self.btn_dothi = tk37Loi.Button(self,
                                        text="Vẽ đồ thị",
                                        command=self.EDA_vedothi,
                                        width=10)
        self.btn_dothi.place(x=1052, y=180)
        self.btn_thaythe = tk37Loi.Button(self,
                                          text='Thay thế',
                                          command=self.EDA_thaythe,
                                          width=10)
        self.btn_thaythe.place(x=1052, y=220)
        self.btn_roirac = tk37Loi.Button(self,
                                         text="rời rạc",
                                         command=self.EDA_roiRac,
                                         width=10)
        self.btn_roirac.place(x=1052, y=260)
        self.method_label = tk37Loi.Label(self,
                                          text='Select method:',
                                          width=10)
        self.method_label.place(x=1052, y=300)
        method_list = ['Chi2', 'f_classif']
        self.method = ttk.Combobox(self,
                                   values=method_list,
                                   state='readonly',
                                   width=10)
        self.method.place(x=1052, y=340)
        self.spin2 = tk37Loi.Spinbox(self, from_=1, to=8, width=10)
        self.spin2.place(x=1052, y=380)
        self.btn_phantich = tk37Loi.Button(self,
                                           text="PT Thăm dò",
                                           command=self.EDA_Thamdo,
                                           width=10)
        self.btn_phantich.place(x=1052, y=420)
        self.method.current(0)
        self.btn_dauvao = tk37Loi.Button(
            self,
            text='Lấy đầu vào',
            command=lambda: self.EDA_DauVao(parent),
            width=10)
        self.btn_dauvao.place(x=1052, y=460)
        self.btn_csv = tk37Loi.Button(self,
                                      text="mở csv",
                                      width=10,
                                      command=self.open_csv)
        self.btn_csv.place(x=10, y=600)
        self.btn_reset = tk37Loi.Button(self,
                                        text="reset",
                                        command=self.reset,
                                        width=10)
        self.btn_reset.place(x=120, y=600)
        self.btn_vedothi = tk37Loi.Button(self,
                                          text="Vẽ Đồ thị",
                                          width=10,
                                          command=lambda: self.VeDoThi(parent))
        self.btn_vedothi.place(x=230, y=600)

    def open_csv(self):
        df = pd.read_csv('.\diemthi2019_update.csv')
        df = df.head(1000)
        self.text.delete('1.0', tk37Loi.END)
        self.text.insert(tk37Loi.END, df.to_string())
        self.panel.update()

    def reset(self):
        self.text.delete('1.0', tk37Loi.END)
        self.text.destroy()
        self.text = tk37Loi.Text(self.panel)
        self.text.pack(fill=tk37Loi.BOTH, expand=True)

    def VeDoThi(self, parent):
        form = Do_Thi(parent)
        form.mainloop()

    def EDA_Thamdo(self):
        text = self.method.get()
        if text == 'Chi2':
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
        self.flat = 3
        form3 = tk37Loi.Toplevel()
        form3.title("Đồ thị z-core")
        form3.geometry('670x420')

        # Tạo một đối tượng Frame để chứa cả đồ thị và nút Button
        frame = tk37Loi.Frame(form3, width=400, height=400)
        frame.place(x=10, y=10)
        # Tạo đồ thị
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        zcore = self.zcore
        x = np.array(zcore['Toan Hoc'].head(4000))
        y = np.arange(4000)
        ax.plot(y, x)

        ax.set_xlabel('SBD')
        ax.set_ylabel('Z-Score')
        canvas = FigureCanvasTkAgg(
            fig,
            master=frame,
        )
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Tạo nút Button
        button = tk37Loi.Button(form3,
                                text='TÍNH',
                                command=lambda: self.Lay_zcore(text),
                                width=10)
        button.place(x=550, y=40)

        text = tk37Loi.Entry(form3, text='', width=10)
        text.place(x=550, y=10)

        # Hiển thị Toplevel
        form3.mainloop()

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
                tk37Loi.END,
                "Kich thuoc cua DataFrame: {}\n".format(self.data.shape))
            self.text.insert(tk37Loi.END, f"{self.data.head(5)}\n")

            self.text.insert(tk37Loi.END,
                             str(self.data.count().sort_values()) + "\n")
        if (self.flat == 1):
            self.data = self.data.drop(columns=parent.dropcolum, axis=1)
            self.text.insert(
                tk37Loi.END,
                "Kich thuoc cua DataFrame sau khi xu li cot NULL: {}\n".format(
                    self.data.shape))
            self.text.insert(tk37Loi.END,
                             str(self.data.count().sort_values()) + "\n")
        if (self.flat == 2):
            value = int(self.spin.get())
            self.data = self.data.dropna(thresh=value)
            self.data = self.data.dropna(subset=parent.dropcolum)
            self.text.insert(
                tk37Loi.END,
                "Kich thuoc cua DataFrame sau khi xu li dong null bằng cách cách loại bỏ giá trị NULL: {}\n"
                .format(self.data.shape))
            self.text.insert(tk37Loi.END,
                             str(self.data.count().sort_values()) + "\n")

            self.text.insert(
                tk37Loi.END,
                'Thay the các giá trị null trong 3 cột Lịch sử, Đia Ly, GDCD bằng giá trị trung bình của từng côt \n'
            )
            for col in ['Dia Ly', 'Lich Su', 'GDCD']:
                mean = self.data[col].mean()
                self.data[col].fillna(mean, inplace=True)
            self.text.insert(
                tk37Loi.END,
                "Kich thuoc cua DataFrame sau khi xu li thay the NULL: {}\n".
                format(self.data.shape))
            self.text.insert(tk37Loi.END,
                             str(self.data.count().sort_values()) + "\n")
            self.text.insert(tk37Loi.END, 'Xử lý Z core \n')
            z = np.abs(stats.zscore(self.data._get_numeric_data()))
            self.zcore = z
            self.text.insert(tk37Loi.END, "MA TRAN Z-SCORE:\n")
            self.text.insert(tk37Loi.END, str(z) + "\n")
        if self.flat == 3:
            self.data = self.data[(self.zcore < self.z).all(axis=1)]
            self.text.insert(
                tk37Loi.END,
                "Kich thuoc cua DataFrame sau khi xu li cac gia tri ngoai le: {}\n"
                .format(self.data.shape))
        if self.flat == 4:
            self.text.insert(tk37Loi.END,
                             'Thay thế các giá trị từ N1..N6 bằng 0..5 \n')
            self.data['Ma Ngoai Ngu'].replace(
                {
                    'N1': 0,
                    'N2': 1,
                    'N3': 2,
                    'N4': 3,
                    'N5': 4,
                    'N6': 5
                },
                inplace=True)
            self.text.insert(tk37Loi.END, "Sau khi Thay the cac gia tri:\n")
            self.text.insert(tk37Loi.END, self.data.head(5))
            self.text.insert(tk37Loi.END, "\n")

        if self.flat == 5:
            self.text.insert(tk37Loi.END, 'Chuẩn hóa rời rạc \n')
            rr = preprocessing.MinMaxScaler()  # xác định thang đo rr.fit(df)
            rr.fit(self.data)
            self.data = pd.DataFrame(rr.transform(self.data),
                                     index=self.data.index,
                                     columns=self.data.columns)
            self.text.insert(tk37Loi.END, "\n")
            self.text.insert(tk37Loi.END, self.data.iloc[4:10])
            self.text.insert(tk37Loi.END, "\n")
            self.text.insert(
                tk37Loi.END,
                f"Độ lớn của bảng [frame] dữ liệu SAU KHI CHUẨN HÓA DL: {self.data.shape}\n"
            )
        if self.flat == 6:
            a = self.data.loc[:, self.data.columns != 'Toan Hoc']
            b = self.data[['Toan Hoc']]
            binarizer = Binarizer(threshold=0.5)
            b = binarizer.fit_transform(b)
            selector = SelectKBest(chi2, k=self.k)
            selector.fit(a, b)
            a_new = selector.transform(a)
            selected_columns = a.columns[selector.get_support(indices=True)]
            self.text.insert('end', 'Các đặc trưng quan trọng: \n')
            for col in selected_columns:
                self.text.insert('end', '-{}\n'.format(col))
            self.text.insert(tk37Loi.END, str(a_new))
            self.text.insert(tk37Loi.END, "\n")
            self.data = self.data[selected_columns]
            parent.data = self.data
        if self.flat == 7:
            a = self.data.loc[:, self.data.columns != 'Toan Hoc']
            b = self.data['Toan Hoc'].ravel()
            selector = SelectKBest(f_classif, k=self.k)
            selector.fit(a, b)
            a_new = selector.transform(a)
            selected_columns = a.columns[selector.get_support(indices=True)]
            self.text.insert('end', 'Các đặc trưng quan trọng: \n')
            for col in selected_columns:
                self.text.insert('end', '-{}\n'.format(col))
            self.text.insert(tk37Loi.END, str(a_new))
            self.text.insert(tk37Loi.END, "\n")
            self.data = self.data[selected_columns]
            parent.data = self.data
        if self.flat == 8:
            self.text.insert('end', 'Các thuộc tính đầu vào: \n')
            self.text.insert(tk37Loi.END, f"{str(parent.dropcolum)} \n")
            for col in parent.dropcolum:
                self.text.insert('end', '-{}\n'.format(self.data[[col]]))


class Cut_Frame(tk37Loi.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("G337TranThanhLoi Cut Frame")
        self.geometry("380x350")
        self.resizable(tk37Loi.FALSE, tk37Loi.FALSE)
        self.buttonFolder = tk37Loi.Button(self,
                                           text="open",
                                           width=10,
                                           command=self.open_file)
        self.buttonFolder.place(x=140, y=20)
        self.lblFolder = tk37Loi.Label(self,
                                       text="Mở Folder",
                                       width=10,
                                       font='Arial 13',
                                       anchor=tk37Loi.CENTER)
        self.lblFolder.place(x=10, y=20)
        self.fileName = None
        self.txtFolderName = tk37Loi.Label(self,
                                           width=30,
                                           text="",
                                           relief=SUNKEN)
        self.txtFolderName.place(x=140, y=70)
        self.LableName = tk37Loi.Label(self,
                                       width=10,
                                       text="Ten folder",
                                       font="Arial 13",
                                       anchor=tk37Loi.CENTER)
        self.LableName.place(x=10, y=70)
        self.LableCatFrame = tk37Loi.Label(
            self,
            text="Cắt khi video đang chạy: ",
            font="Arial 13",
        )
        self.LableCatFrame.place(x=15, y=120)
        self.btnXulyAnh = tk37Loi.Button(self,
                                         text='Xử lý',
                                         width=10,
                                         command=self.capture_frames)
        self.btnXulyAnh.place(x=240, y=120)
        self.btnCatYMuon = tk37Loi.Button(self,
                                          text="Cắt ảnh",
                                          width=10,
                                          command=self.cut_frame)
        self.LableCatFrameTime = tk37Loi.Label(
            self,
            text="Cắt khi video tại thời điểm: ",
            font="Arial 13",
        )
        self.LableCatFrameTime.place(x=15, y=250)
        self.btnCatYMuon.place(x=110, y=300)
        self.spinbox = tk37Loi.Spinbox(self, from_=0, to=100, width=5)
        self.spinbox.place(x=20, y=303)
        self.lablespin = tk37Loi.Label(self, text="giây")
        self.lablespin.place(x=70, y=300)
        self.entr = tk37Loi.Entry(self, width=10, relief=tk37Loi.SUNKEN)
        self.btnfd = tk37Loi.Button(self,
                                    text="Chọn đường dẫn",
                                    command=self.Chon_duong_Dan)
        self.labelfd = tk37Loi.Label(self, text="Nhập tên")
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
        cv2.imshow('Frame', frame)
        cv2.imwrite(self.savepath, frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Mở file",
                                               filetypes=(("mp4 file(.mp4)",
                                                           "*.mp4"),
                                                          ("mov file(.mov)",
                                                           "*.mov")))
        self.fileName = file_path
        self.txtFolderName.config(text=self.fileName)

    def Chon_duong_Dan(self):
        self.savepath = filedialog.askdirectory(title="Chọn folder lưu ảnh")
        self.savepath += f"/{self.entr.get()}.jpg"
        tk37Loi.Label(self, text=self.savepath).place(x=10, y=230)

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
            cv2.imshow('frame', frame)

            # Chờ sự kiện từ bàn phím
            key = cv2.waitKey(25)

            # Kiểm tra nếu nhấn space
            if key == ord(' '):
                # Hiển thị hộp thoại để chọn vị trí và đặt tên file
                root = tk.Tk()
                root.withdraw()
                save_path = filedialog.asksaveasfilename(
                    defaultextension='.jpg',
                    filetypes=[('JPEG files', '*.jpg')])
                root.destroy()

                if save_path:
                    # Lưu frame vào file
                    cv2.imwrite(save_path, frame)
                    frame_count += 1

            # Kiểm tra nếu nhấn phím 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # giải phóng tài nguyên
        cap.release()
        cv2.destroyAllWindows()


class Do_Thi(tk37Loi.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Đồ thị z-core")
        self.geometry('670x420')
        self.frame = tk37Loi.Frame(self,
                                   width=400,
                                   height=400,
                                   relief=tk37Loi.SUNKEN)
        self.frame.place(x=10, y=10)
        self.button = tk37Loi.Button(self,
                                     text='Vẽ',
                                     width=10,
                                     command=self.VeDoThi)
        self.button.place(x=550, y=390)
        self.dict_tinh = {
            "Hà Nội": 1,
            "TP Hồ Chí Mình": 2,
            "Hải Phòng": 3,
            "Đà Nẵng": 4,
            "Bình Dương": 44
        }
        self.combobox = ttk.Combobox(self,
                                     values=list(self.dict_tinh.keys()),
                                     width=10)
        self.label1 = tk37Loi.Label(self, text='Chọn tỉnh')
        self.dict_mon = {
            "Toán": "Toan Hoc",
            "Ngữ Văn": "Ngu Van",
            "Ngoại Ngữ": "Ngoai Ngu",
            "Vật Lý": "Vat Ly",
            "Hóa Học": "Hoa Hoc",
            "Sinh Học": "Sinh Hoc",
            "GDCD": "GDCD",
            "Địa Lý": "Dia Ly",
            "Lịch Sử": "Lich Su"
        }
        self.combobox2 = ttk.Combobox(self,
                                      values=list(self.dict_mon.keys()),
                                      width=10)
        self.label2 = tk37Loi.Label(self, text="Chọn môn học")
        self.label1.place(x=550, y=10)
        self.combobox.place(x=550, y=50)
        self.label2.place(x=550, y=90)
        self.combobox2.place(x=550, y=130)
        self.data = pd.read_csv('.\diemthi2019_update.csv')
        self.data = self.data.head(2000)
        self.DF_tinh = None
        self.DF_monhoc = None
        self.canvas = None

    def DFTinh(self, matinh):
        rowCnt, colCnt = self.data.shape
        DF_tinh = pd.DataFrame()
        DF_tinh["SBD"] = pd.Series([], dtype=int)
        for index, row in self.data.iterrows():
            SBD = row['SBD']
            maTinh = SBD // 1000000
            if maTinh == matinh:
                DF_tinh = DF_tinh.append(row)
        self.DF_tinh = DF_tinh

    def DFMon(self, monhoc):
        self.DF_monhoc = self.DF_tinh[monhoc]

    def VeDoThi(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        if isinstance(self.DF_tinh, pd.DataFrame) == False:
            self.DFTinh(self.dict_tinh[self.combobox.get()])
        self.DFMon(self.dict_mon[self.combobox2.get()])
        cnt = [0] * 205
        for i in range(self.DF_monhoc.size):
            try:
                num = float(self.DF_monhoc.iloc[i]) * 20
                num = int(num)
                cnt[num] += 1
            except:
                continue
        # Tạo biểu đồ
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(cnt)
        # Chuyển đổi Figure thành canvas
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.canvas.draw()
        # Hiển thị canvas
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


myWindow = Window()
myWindow.mainloop()
