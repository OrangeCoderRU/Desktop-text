import numpy as np
import ctypes
from PIL import Image, ImageDraw, ImageFont
import scipy.misc
import os
import datetime
from win32api import GetSystemMetrics
import json

dict = {}

def read_file():
    with open("data_file.json", "r") as read_file: # read data file
        dict = json.load(read_file)
    return dict

dict = read_file()

def data_dump(dict):
    date = datetime.datetime(int(dict.get("Год")), int(dict.get("Месяц")), int(dict.get("День")), 0, 0, 0)
    today = datetime.datetime.now()
    date = date - today #datetime.timedelta
    string_day = " дней"
    string_hour = " часов"
    if ((date.days % 10) == 0) and (not (date.days % 10) == 10):
        string_day = " дней"
    elif (date.days) == 1:
        string_day = " день"
    elif (date.days) in range(10, 21, 1):
        string_day = " дней"
    elif (date.days % 10) in range(2, 5, 1):
        string_day = " дня"
    elif (date.days % 10) in range(5, 10, 1):
        string_day = " дней"
    if int((date.seconds / 3600)) == 21:
        string_hour = " час"
    elif int((date.seconds / 3600)) == 1:
        string_hour = " час"
    elif int((date.seconds / 3600)) in range(2, 5, 1):
        string_hour = " часа"
    elif int((date.seconds / 3600)) in range(22, 25, 1):
        string_hour = " часа"
    elif int((date.seconds / 3600)) in range(5, 10, 1):
        string_hour = " чаcов"
    elif int((date.seconds / 3600)) in range(10, 21, 1):
        string_hour = " чаcов"
    return str(date.days) + string_day + " " + str(int(date.seconds / 3600)) + string_hour + "\n"

def create_image():
    #определение разрешения экрана
    monitor_width = GetSystemMetrics(0)
    monitor_heitgh = GetSystemMetrics(1)

    # создадим белое изображение
    img = np.zeros((monitor_heitgh, monitor_width, 3), np.uint8)
    img[:, :, :] = 255
    return img

def default_image():
    #if dict["path"] == "Здесь пока ничего нет":
        #img = Image.open(r'D:\Photo\IMG_4021-1920.jpg')
    #D:\Photo\IMG_4021.jpg
    #else:
        #path = dict.get("path")
        #img = Image.open(path)
    #img = Image.open(r'D:\Photo\IMG_4021-1920.jpg')
    #img.show()
    path = dict.get("path")
    img = Image.open(path)
    arr = np.asarray(img, dtype='uint8')
    return arr

print(dict["status"])

if dict["status"] == 0:
    img = default_image()
else:
    img = create_image()

#img = create_image()
#img = default_image()

def put_text_pil(img: np.array, txt: str):
    im = Image.fromarray(img)

    font_size = dict["font"]
    font = ImageFont.truetype("ofont.ru_Clear Sans Thin.ttf", size=font_size)

    draw = ImageDraw.Draw(im)
    # здесь узнаем размеры сгенерированного блока текста
    w, h = draw.textsize(txt, font=font)

    draw = ImageDraw.Draw(im)
    width, height = im.size
    #x, y = (width-700, height-1050)
    x, y = ((width / 1.5) + 150, height / 100)
    #x, y = (width - 500, height - 600)
    # теперь можно центрировать текст
    #draw.text((int((img.shape[1] - w)/2) + 100, y_pos), txt, fill='rgb(0, 0, 0)', font=font)
    draw.text((x, y), txt, fill='rgb(0, 0, 0)', font=font)
    img = np.asarray(im)

    return img

def date_time():
    date = datetime.datetime(2019, 11, 16, 0, 0, 0)
    today = datetime.datetime.today()
    date = date - today
    return date

def now_time():
    today = datetime.datetime.now()
    today_month = ""
    if today.month == 1:
        today_month = "января"
    elif today.month == 2:
        today_month = "февраля"
    elif today.month == 3:
        today_month = "марта"
    elif today.month == 4:
        today_month = "апреля"
    elif today.month == 5:
        today_month = "мая"
    elif today.month == 6:
        today_month = "июня"
    elif today.month == 7:
        today_month = "июля"
    elif today.month == 8:
        today_month = "августа"
    elif today.month == 9:
        today_month = "сентября"
    elif today.month == 10:
        today_month = "октября"
    elif today.month == 11:
        today_month = "ноября"
    elif today.month == 12:
        today_month = "декабря"
    return str(today.day) + " " + today_month

def set_wallpaper():
    SPI_SETDESKWALLPAPER = 20 # константа, всегда = 20
    p = os.path.abspath('my.jpg')
    arg = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, p , 0)
    # SystemParametersInfoW - 64 bit системы
    # SystemParametersInfoA - 32 bit системы


task_text = " до " + str(dict['Задача'])
text = " " + "Сегодня " + str(now_time()) + "\n" + " " + (str(data_dump(dict))) + task_text
#sep = " " + (int(len(text) / 2)) * "-"

#main_string = string + "\n" + string_task

img = put_text_pil(img, text)
image = Image.fromarray(img, 'RGB')
image.save('my.jpg')

set_wallpaper()
