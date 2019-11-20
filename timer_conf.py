import json
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import filedialog as fd
import subprocess
import sys
import os

window = Tk()
window.title('Desktop Text')
window.geometry('600x200') # window size

dict = {}

lbl = Label(window, text="дней до...", font=("Arial Bold", 12))
lbl.grid(row = 0, column = 0)
ent = Entry(window, width=30, bd=1)
ent.grid(row = 0, column = 1)

lbl2 = Label(window, text="число", font=("Arial Bold", 12))
lbl2.grid(row = 1, column = 0)

lbl3 = Label(window, text="месяц", font=("Arial Bold", 12))
lbl3.grid(row = 1, column = 1)

lbl5 = Label(window, text="год", font=("Arial Bold", 12))
lbl5.grid(row = 1, column = 2)

lbl4 = Label(window, text="Задание:", font=("Arial Bold", 10), width=10)
lbl4.grid(row = 4, column = 0)

task_listbox = Listbox(font = ('Arial Bold', 10), height = 4, width = 30)
task_listbox.grid(row = 4, column = 1)

dict_path = {}

def insertFile():
    """path to the selected file on screen"""
    file_name = fd.askopenfilename()
    f = open(file_name)
    p = os.path.abspath(file_name)
    print(p)
    dict_path = {"path": p}
    lbl5.configure(text = p)
    f.close()

def read_file():
    """reading data"""
    with open("data_file.json", "r") as read_file: # read data file
        dict = json.load(read_file)
    for tasks in dict:
        if tasks == "status":
            break
        else:
            task_listbox.insert(END, str(tasks) + " - " + str(dict[tasks]))

def clicked():
    """confirm task and data transfer timer.py"""
    dict = {"Задача": ent.get(), "День": int(combo_days.get()), "Месяц": int(combo_month.get()), "Год": int(combo_year.get()), "status": state.get(), "path": lbl5.cget("text"), "font": int(combo_font.get())}
    #dict.update(dict_path)
    save_file(dict)
    read_file()
    program = "timer.py"
    # start logic prog
    subprocess.Popen([sys.executable, program])

def save_file(dict):
    """Save data action"""
    with open("data_file.json", "w") as write_file: # write data file
        json.dump(dict, write_file, indent = 4)
    messagebox.showinfo("Ok", "The data was successfully saved")

read_file()

state = IntVar()
state.set(0)  # задайте проверку состояния чекбокса
chk = Checkbutton(window, text='Белый фон', var=state)
chk.grid(row = 3, column = 2)

combo_days = Combobox(window, width=10)
combo_days['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31)
combo_days.current(0)  # установите вариант по умолчанию
combo_days.grid(row = 2, column = 0)

combo_month = Combobox(window, width=10)
combo_month['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12)
combo_month.current(0)  # установите вариант по умолчанию
combo_month.grid(row = 2, column = 1)

combo_year = Combobox(window, width=10)
combo_year['values'] = (2019, 2020, 2021, 2022, 2023, 2024, 2025)
combo_year.current(0)  # установите вариант по умолчанию
combo_year.grid(row = 2, column = 2)

lbl5 = Label(window, text="Размер шрифта:", font=("Arial", 10))
lbl5.grid(row = 0, column = 2)

combo_font = Combobox(window, width=10)
combo_font['values'] = (10, 20, 30, 40, 50, 60, 70, 80, 90 , 100, 150, 200, 250, 300)
combo_font.current(0)  # установите вариант по умолчанию
combo_font.grid(row = 0, column = 3)

btn = Button(window, text="Применить", command = clicked)
btn.grid(row = 3, column = 1)

btn_open = Button(text="Открыть", command=insertFile, width=25)
btn_open.grid(row = 5, column = 2)

lbl5 = Label(window, text="Здесь пока ничего нет", font=("Arial", 10))
lbl5.grid(row = 4, column = 2)

window.mainloop()
