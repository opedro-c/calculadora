from tkinter import *
from utilitarios import verificar_colar
from Calculadora import Calculadora as calc
from pyperclip import copy, paste


# Janela
app = Tk()
app.geometry('300x380')
app.title('Calculadora')


# Display
frame = Frame(app, bg='white', borderwidth=1, relief='solid', width=280, height=30)
frame.place(x=10, y=10)
current_number = Label(frame, text='0', bg='white', fg='black', width=34, anchor=E)
current_number.place(x=0, y=5)

# Barra de menus
barra_menus = Menu(app, bg='#dde', fg='black')

menu_arquivo = Menu(barra_menus, tearoff=0, bg='#dde', fg='black')
menu_arquivo.add_command(label='Fechar', command=app.quit)
barra_menus.add_cascade(label='Arquivo', menu=menu_arquivo)

menu_editar = Menu(barra_menus, tearoff=0, bg='#dde', fg='black')
menu_editar.add_command(label='Copiar', command=lambda: copy(current_number['text']))
menu_editar.add_command(label='Colar', command=lambda: current_number.config(text=verificar_colar(paste())))
barra_menus.add_cascade(label='Editar', menu=menu_editar)

app.config(bg='white', menu=barra_menus)

# Graus ou radianos
botoes_graus = BooleanVar()
botoes_graus.set(True)
Radiobutton(app, text='Graus', variable=botoes_graus, value=True, command=calc.setGraus(botoes_graus), 
            bg='white', fg='black', borderwidth=0).place(x=10, y=50)
Radiobutton(app, text='Radianos', variable=botoes_graus, value=False, command=calc.setGraus(botoes_graus),
            bg='white', fg='black', borderwidth=0).place(x=100, y=50)

# Números e ponto
Button(app, text='7', command=lambda: calc.click_number(current_number, '7')).place(x=10, y=140, width=45, height=45)
Button(app, text='8', command=lambda: calc.click_number(current_number, '8')).place(x=65, y=140, width=45, height=45)
Button(app, text='9', command=lambda: calc.click_number(current_number, '9')).place(x=120, y=140, width=45, height=45)
Button(app, text='4', command=lambda: calc.click_number(current_number, '4')).place(x=10, y=200, width=45, height=45)
Button(app, text='5', command=lambda: calc.click_number(current_number, '5')).place(x=65, y=200, width=45, height=45)
Button(app, text='6', command=lambda: calc.click_number(current_number, '6')).place(x=120, y=200, width=45, height=45)
Button(app, text='1', command=lambda: calc.click_number(current_number, '1')).place(x=10, y=260, width=45, height=45)
Button(app, text='2', command=lambda: calc.click_number(current_number, '2')).place(x=65, y=260, width=45, height=45)
Button(app, text='3', command=lambda: calc.click_number(current_number, '3')).place(x=120, y=260, width=45, height=45)
Button(app, text='0', command=lambda: calc.click_number(current_number, '0')).place(x=10, y=320, width=100, height=45)
Button(app, text='.', command=lambda: calc.click_number(current_number, '.')).place(x=120, y=320, width=45, height=45)

# Operações
Button(app, text='+', command=lambda: calc.somar(current_number)).place(x=10, y=90, width=35, height=35)
Button(app, text='-', command=lambda: calc.subtrair(current_number)).place(x=50, y=90, width=35, height=35)
Button(app, text='X', command=lambda: calc.multplicar(current_number)).place(x=90, y=90, width=35, height=35)
Button(app, text='÷', command=lambda: calc.dividir(current_number)).place(x=130, y=90, width=35, height=35)
Button(app, text='xʸ', command=lambda: calc.potencia(current_number)).place(x=170, y=90, width=35, height=35)
Button(app, text='|x|', command=lambda: calc.absoluto(current_number)).place(x=210, y=90, width=35, height=35)
Button(app, text='C', command=lambda: calc.c(current_number)).place(x=250, y=90, width=35, height=35)
Button(app, text='←', command=lambda: calc.backspace(current_number)).place(x=170, y=140, width=115, height=45)
Button(app, text='sen', command=lambda: calc.seno(current_number)).place(x=170, y=210, width=35, height=45)
Button(app, text='cos', command=lambda: calc.cosseno(current_number)).place(x=210, y=210, width=35, height=45)
Button(app, text='tan', command=lambda: calc.tangente(current_number)).place(x=250, y=210, width=35, height=45)
Button(app, text='-/+', command=lambda: None).place(x=170, y=260, width=35, height=45)
Button(app, text='x!', command=lambda: None).place(x=210, y=260, width=35, height=45)
Button(app, text='√', command=lambda: None).place(x=250, y=260, width=35, height=45)
Button(app, text='=', command=lambda: calc.igual(current_number)).place(x=170, y=320, width=115, height=45)


app.mainloop()
