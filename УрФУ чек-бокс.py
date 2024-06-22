# импорт необходимых библиотек
import tkinter
from tkinter import *
from tkinter import ttk

# настройки окна
root = Tk()
root.title("УрФУ Осипов чек-бокс")
root.geometry("550x550")
 
variants = ["выполнено", "выполнено частично", "не прикасался еще", "оставить на пересдачу"] # спикок для выпадающего окна

# функция перебора уловий для переменных
def select():
    result = "Проверено: "
    if SQL.get() == 1: result = f"{result} SQL, "
    if python.get() == 1: result = f"{result} Углубленное программирование на Python, "
    if english.get() == 1: result = f"{result} Business English II, "
    if MLOps.get() == 1: result = f"{result} Автоматизация администрирования MLOps, "
    if engeneer.get() == 1: result = f"{result} Программная инженерия, "
    if math_base.get() == 1: result = f"{result} Математические основы анализа данных, "
    if ML_base.get() == 1: result = f"{result} Математические основы машинного обучения, "
    if practicum.get() == 1: result = f"{result} Цифровые компетенции в научной деятельности, "
    subjects.set(result)
# настройки окна
position = {"padx":1, "pady":1, "anchor":NW}
 
subjects = StringVar()
subjects_label = ttk.Label(textvariable=subjects)
subjects_label.pack(**position)

# блок переменных
SQL = IntVar()
SQL_checkbutton = ttk.Checkbutton(text="курс по SQL", variable=SQL, command=select)
SQL_checkbutton.pack(**position)
combobox = ttk.Combobox(values=variants)
combobox.pack(anchor=NW, padx=6, pady=6)
 
python = IntVar()
python_checkbutton = ttk.Checkbutton(text="Углубленное программирование на Python", variable=python, command=select)
python_checkbutton.pack(**position)
combobox = ttk.Combobox(values=variants)
combobox.pack(anchor=NW, padx=6, pady=6)
 
english = IntVar()
english_checkbutton = ttk.Checkbutton(text="Business English II", variable=english, command=select)
english_checkbutton.pack(**position)
combobox = ttk.Combobox(values=variants)
combobox.pack(anchor=NW, padx=6, pady=6)

MLOps = IntVar()
MLOps_checkbutton = ttk.Checkbutton(text="Автоматизация администрирования MLOps", variable=MLOps, command=select)
MLOps_checkbutton.pack(**position)
combobox = ttk.Combobox(values=variants)
combobox.pack(anchor=NW, padx=6, pady=6)

engeneer = IntVar()
engeneer_checkbutton = ttk.Checkbutton(text="Программная инженерия II", variable=engeneer, command=select)
engeneer_checkbutton.pack(**position)
combobox = ttk.Combobox(values=variants)
combobox.pack(anchor=NW, padx=6, pady=6)

math_base = IntVar()
math_base_checkbutton = ttk.Checkbutton(text="Математические основы анализа данных II", variable=math_base, command=select)
math_base_checkbutton.pack(**position)
combobox = ttk.Combobox(values=variants)
combobox.pack(anchor=NW, padx=6, pady=6)

ML_base = IntVar()
ML_base_checkbutton = ttk.Checkbutton(text="Математические основы машинного обучения II", variable=ML_base, command=select)
ML_base_checkbutton.pack(**position)
combobox = ttk.Combobox(values=variants)
combobox.pack(anchor=NW, padx=6, pady=6)

practicum = IntVar()
practicum_checkbutton = ttk.Checkbutton(text="Практикум II", variable=practicum, command=select)
practicum_checkbutton.pack(**position)
combobox = ttk.Combobox(values=variants)
combobox.pack(anchor=NW, padx=6, pady=6)

# запуск программы
root.mainloop()
