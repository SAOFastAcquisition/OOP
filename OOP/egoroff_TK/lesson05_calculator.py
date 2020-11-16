import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image as pilImage
from PIL import ImageTk, ImageOps


class Wind:

    def __init__(self, width, height, title='Calculator', resize=(False, False), icon=None, ):
        self.wind = tk.Tk()
        self.wind.geometry(f'{width}x{height}+200+400')
        self.wind['bg'] = 'cyan'
        self.wind.title(title)
        self.wind.resizable(resize[0], resize[1])
        if icon:
            photo_icon = tk.PhotoImage(file=icon)
            self.wind.iconphoto(False, photo_icon)

        self.calc = tk.Entry(self.wind, width=15, borderwidth=5, justify='right',
                             font=('consolas', 18))  # .grid(column=0, row=0, columnspan=4)

        # Buttons
        but = [0] * 11
        for i in range(10):
            if i == 0:
                but[i] = CalcButton(self, self.wind, i, 7 - (i + 2) // 3, column=i)
            else:
                but[i] = CalcButton(self, self.wind, i, 7 - (i + 2) // 3, column=(i - 1) % 3)

        self.btn_del = tk.Button(self.wind, text='Quit', font=('consolas', 20), height=1, relief='groove', command=quit)
        self.btn_clear = tk.Button(self.wind, text='C', font=('consolas', 20), width=3, height=1, relief='groove',
                                   command=self.del_entry)

    def ins_num(self, i):
        num = self.calc.get()
        num = num + str(i)
        if len(num) > 1:
            if (num[0] == '0') & (num[1] != '.'):
                num = num[1:len(num)]
        self.calc.delete(0, tk.END)
        self.calc.insert(0, num)

    def widget_draw(self):
        self.calc.grid(column=0, row=0, columnspan=4, stick='we')
        # Buttons
        self.btn_clear.grid(column=1, row=7, columnspan=2, stick='wens', padx=5, pady=5)
        self.btn_del.grid(column=0, row=8, columnspan=3, stick='wens', padx=5, pady=5)
        self.wind.mainloop()

    def del_entry(self):
        self.calc.delete(0, tk.END)


class CalcButton:
    def __init__(self, obj, wind, digit, row, column):
        # self.button = tk.Tk()
        self.button = tk.Button(wind, text=f'{digit}', font=('consolas', 20), width=3, height=1, relief='groove',
                                command=lambda: obj.ins_num(digit))
        self.button.grid(row=row, column=column, padx=5, pady=5)


if __name__ == '__main__':
    wndw = Wind(500, 400, icon='ghost.gif')
    wndw.widget_draw()
