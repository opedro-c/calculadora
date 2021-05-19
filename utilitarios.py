from tkinter import messagebox as msg


def formatar_expressao(expressao):
    if '**' in expressao:
        return expressao.replace('**', '^')
    elif '*' in expressao:
        return expressao.replace('*', 'x')
    else:
        return expressao


def expressao_ok(expressao):
    return not expressao.replace('.', '').isnumeric()
        

def verificar_colar(texto):
    texto_tratado = texto.replace('.','').strip()
    if texto_tratado.isnumeric():
        return texto_tratado
    else: 
        msg.showinfo(title='Calculadora', message='Só pode colar números!')