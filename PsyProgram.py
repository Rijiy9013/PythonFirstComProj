import tkinter as tk
from tkinter import *


class PsyProgram:
    window = tk.Tk()
    numb_image = 3
    canvas = Canvas(window, width=1000, height=1000)
    canvas.pack()
    background_obj = PhotoImage(file=r'background\startBackgr.png')
    canvas.create_image(20, 20, anchor="nw", image=background_obj)

    def __init__(self):
        self.window.title('Тестирование')
        self.window.geometry("1500x1300")
        self.menubar = tk.Menu(self.window)
        self.window.config(menu=self.menubar)
        settings_menu = tk.Menu(self.menubar, tearoff=0)
        settings_menu.add_command(label='Старт', command=self.start_test)
        settings_menu.add_command(label='Изображения', command=self.create_settings_win)
        settings_menu.add_command(label='Результаты', command=self.show_results)
        self.menubar.add_cascade(label='Настройки', menu=settings_menu)

    def start(self):
        PsyProgram.window.mainloop()

    def start_test(self):
        if self.numb_image != 0:
            self.print_instruction()
        else:
            self.print_error()

    def create_settings_win(self):
        win_settings = tk.Toplevel(self.window)
        win_settings.wm_title('Количество изображений')
        win_settings.geometry("350x100")
        tk.Label(win_settings, text='Количество изображений').grid(row=0, column=0)
        image_entry = tk.Entry(win_settings)
        image_entry.grid(row=0, column=1, padx=20, pady=20)
        image_entry.insert(0, PsyProgram.numb_image)
        tk.Button(win_settings, text='Применить', command=lambda: self.change_settings(image_entry)).grid(
            row=1, column=0, columnspan=2)

    def change_settings(self, image: tk.Entry):
        PsyProgram.numb_image = int(image.get())

    def show_results(self):
        pass

    def print_instruction(self):
        instr1 = PhotoImage(file=r'instruction\1.png')
        # self.canvas.delete("all")
        self.canvas.update()
        self.canvas.create_image(20, 20, anchor="nw", image=instr1)
        self.canvas.update()
        # instr2 = PhotoImage(file='instruction/second.png')
        # instr3 = PhotoImage(file='instruction/third.png')
        # instr4 = PhotoImage(file='instruction/forth.png')
        # instr5 = PhotoImage(file='instruction/fifth.png')
        # instr6 = PhotoImage(file='instruction/sixth.png')
        # instr7 = PhotoImage(file='instruction/seventh.png')
        # instr8 = PhotoImage(file='instruction/eighth.png')

    def print_error(self):
        error_win = tk.Toplevel(self.window)
        error_win.wm_title('Ошибка')
        error_win.geometry("200x50")
        tk.Label(error_win, text='Укажите количество картинок!').grid(row=0, column=1)


program = PsyProgram()
program.start()
