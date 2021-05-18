from tkinter import *
from utilitarios import aux
from Calculadora import Calculadora as calc

app = Tk()
app.geometry('300x340')
app.title('Calculadora')
app.config(bg='white')
frame = Frame(app, bg='white', borderwidth=1, relief='solid', width=280, height=30)
frame.place(x=10, y=10)
current_number = Label(frame, text='0', bg='white', fg='black', width=34, anchor=E)
current_number.place(x=0, y=5)

# Números e ponto
Button(app, text='7', command=lambda: calc.click_number(current_number, '7')).place(x=10, y=100, width=45, height=45)
Button(app, text='8', command=lambda: calc.click_number(current_number, '8')).place(x=65, y=100, width=45, height=45)
Button(app, text='9', command=lambda: calc.click_number(current_number, '9')).place(x=120, y=100, width=45, height=45)
Button(app, text='4', command=lambda: calc.click_number(current_number, '4')).place(x=10, y=160, width=45, height=45)
Button(app, text='5', command=lambda: calc.click_number(current_number, '5')).place(x=65, y=160, width=45, height=45)
Button(app, text='6', command=lambda: calc.click_number(current_number, '6')).place(x=120, y=160, width=45, height=45)
Button(app, text='1', command=lambda: calc.click_number(current_number, '1')).place(x=10, y=220, width=45, height=45)
Button(app, text='2', command=lambda: calc.click_number(current_number, '2')).place(x=65, y=220, width=45, height=45)
Button(app, text='3', command=lambda: calc.click_number(current_number, '3')).place(x=120, y=220, width=45, height=45)
Button(app, text='0', command=lambda: calc.click_number(current_number, '0')).place(x=10, y=280, width=100, height=45)
Button(app, text='.', command=lambda: calc.click_number(current_number, '.')).place(x=120, y=280, width=45, height=45)

# Operações
Button(app, text='+', command=lambda: calc.somar(current_number)).place(x=10, y=50, width=35, height=35)
Button(app, text='-', command=lambda: calc.subtrair(current_number)).place(x=50, y=50, width=35, height=35)
Button(app, text='X', command=lambda: calc.multplicar(current_number)).place(x=90, y=50, width=35, height=35)
Button(app, text='÷', command=lambda: calc.dividir(current_number)).place(x=130, y=50, width=35, height=35)
Button(app, text='xʸ', command=aux).place(x=170, y=50, width=35, height=35)
Button(app, text='|x|', command=aux).place(x=210, y=50, width=35, height=35)
Button(app, text='C', command=lambda: calc.c(current_number)).place(x=250, y=50, width=35, height=35)
Button(app, text='=', command=lambda: calc.igual(current_number)).place(x=170, y=280, width=115, height=45)
Button(app, text='←', command=lambda: calc.backspace(current_number)).place(x=170, y=100, width=115, height=45)

app.mainloop()
