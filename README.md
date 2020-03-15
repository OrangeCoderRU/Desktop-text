# Desktop-text
## Программа позволяющая писать количество дней до введённого события на фоне рабочего стола с помощью win32api.

- timer.py - логика программы(наложение текста на изображение, установка нового фона и тд)

- timer_conf.py - графическая оболочка на Tkinter, позволяет выбирать файл, на который будет нанесён текст.
Также можно выбирать размер шрифта, то о чём напоминать и дату события.

- data_dump.json - данные приложения, а также служебная информация, которой обмениваются два .py файла.

### Также есть вариант выбора белого изображения, размер которого определяется автоматически по разрешению экрана

![alt text](screenshots/screenshot_2.png)

- Запуск timer_conf.py - для настройки: сначала выбор даты, текста, шрифта и файла - click "применить".

- Запуск timer.py - прогоняет логику заново, за счёт чего происходит перерасчёт даты и времени.
### Статья о том как писалось:
https://vk.com/@78369065
