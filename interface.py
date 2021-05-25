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
current_number = Label(frame, text='0', bg='white', fg='black', anchor=E)
current_number.place(x=0, y=5, width=270)

# Barra de menus
barra_menus = Menu(app, bg='white', fg='black')

menu_arquivo = Menu(barra_menus, tearoff=0, bg='white', fg='black')
menu_arquivo.add_command(label='Fechar', command=app.quit)
barra_menus.add_cascade(label='Arquivo', menu=menu_arquivo)

menu_editar = Menu(barra_menus, tearoff=0, bg='white', fg='black')
menu_editar.add_command(label='Copiar', command=lambda: copy(current_number['text']))
menu_editar.add_command(label='Colar', command=lambda: current_number.config(text=verificar_colar(paste())))
barra_menus.add_cascade(label='Editar', menu=menu_editar)

menu_constantes = Menu(barra_menus, tearoff=0, bg='white', fg='black')
menu_constantes.add_command(label='Pi', command=lambda: current_number.config(text='3.14159265'))
menu_constantes.add_command(label='Euler', command=lambda: current_number.config(text='0.57721566'))
menu_constantes.add_command(label='Proporção Áurea', command=lambda: current_number.config(text='1,60217653'))
menu_constantes.add_command(label='Velocidade da luz (m\s)', command=lambda: current_number.config(text='299792458'))
barra_menus.add_cascade(label='Constantes', menu=menu_constantes)

app.config(bg='white', menu=barra_menus)

# Graus ou radianos
botoes_graus = IntVar()
botoes_graus.set(1)
Radiobutton(app, text='Graus', bg='white', fg='black', variable=botoes_graus, value=1, 
            command=lambda: calc.setGraus(botoes_graus.get()), borderwidth=0).place(x=10, y=50)
Radiobutton(app, text='Radianos', bg='white', fg='black', variable=botoes_graus, value=0, 
            command=lambda: calc.setGraus(botoes_graus.get()), borderwidth=0).place(x=100, y=50)

# Números e ponto
Button(app, text='7', command=lambda: calc.clicar_numero(current_number, '7')).place(x=10, y=140, width=45, height=45)
Button(app, text='8', command=lambda: calc.clicar_numero(current_number, '8')).place(x=65, y=140, width=45, height=45)
Button(app, text='9', command=lambda: calc.clicar_numero(current_number, '9')).place(x=120, y=140, width=45, height=45)
Button(app, text='4', command=lambda: calc.clicar_numero(current_number, '4')).place(x=10, y=200, width=45, height=45)
Button(app, text='5', command=lambda: calc.clicar_numero(current_number, '5')).place(x=65, y=200, width=45, height=45)
Button(app, text='6', command=lambda: calc.clicar_numero(current_number, '6')).place(x=120, y=200, width=45, height=45)
Button(app, text='1', command=lambda: calc.clicar_numero(current_number, '1')).place(x=10, y=260, width=45, height=45)
Button(app, text='2', command=lambda: calc.clicar_numero(current_number, '2')).place(x=65, y=260, width=45, height=45)
Button(app, text='3', command=lambda: calc.clicar_numero(current_number, '3')).place(x=120, y=260, width=45, height=45)
Button(app, text='0', command=lambda: calc.clicar_numero(current_number, '0')).place(x=10, y=320, width=100, height=45)
Button(app, text='.', command=lambda: calc.clicar_numero(current_number, '.')).place(x=120, y=320, width=45, height=45)

# Operações
Button(app, text='+',
       command=lambda: calc.operacoes_binarias(current_number, '+')).place(x=10, y=90, width=35, height=35)
Button(app, text='-', 
       command=lambda: calc.operacoes_binarias(current_number, '-')).place(x=50, y=90, width=35, height=35)
Button(app, text='X', 
       command=lambda: calc.operacoes_binarias(current_number, '*')).place(x=90, y=90, width=35, height=35)
Button(app, text='÷', 
       command=lambda: calc.operacoes_binarias(current_number, '/')).place(x=130, y=90, width=35, height=35)
Button(app, text='xʸ', 
       command=lambda: calc.operacoes_binarias(current_number, '**')).place(x=170, y=90, width=35, height=35)
Button(app, text='|x|', 
       command=lambda: calc.operacoes_unitarias(current_number, abs, f"|{current_number}|")).place(x=210, y=90, width=35, height=35)
Button(app, text='C', 
       command=lambda: calc.c(current_number)).place(x=250, y=90, width=35, height=35)
Button(app, text='←', 
       command=lambda: calc.backspace(current_number)).place(x=170, y=140, width=115, height=45)
Button(app, text='sen', 
       command=lambda: calc.operacoes_trigonometricas(current_number, calc.seno, 'sen')).place(x=170, y=200, width=35, height=45)
Button(app, text='cos', 
       command=lambda: calc.operacoes_trigonometricas(current_number, calc.cosseno, 'cos')).place(x=210, y=200, width=35, height=45)
Button(app, text='tan', 
       command=lambda: calc.operacoes_trigonometricas(current_number, calc.tangente, 'tan')).place(x=250, y=200, width=35, height=45)
Button(app, text='-/+', 
       command=lambda: calc.inverter_valor(current_number)).place(x=170, y=260, width=35, height=45)
Button(app, text='x!', 
       command=lambda: calc.operacoes_unitarias(current_number, calc.fatorial, f"{current_number}!")).place(x=210, y=260, width=35, height=45)
Button(app, text='√', 
       command=lambda: calc.operacoes_unitarias(current_number, calc.raiz_quad, f"√{current_number}")).place(x=250, y=260, width=35, height=45)
Button(app, text='=', 
       command=lambda: calc.igual(current_number)).place(x=170, y=320, width=115, height=45)


app.mainloop()
