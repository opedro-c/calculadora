from tkinter import messagebox as msg

def formatar_expressao(expressao):
    if '**' in expressao:
        return expressao.replace('**', '^')
    elif '*' in expressao:
        return expressao.replace('*', 'x')
    elif 'abs' in expressao:
        return f'|{("".join(filter(lambda x: x.isnumeric(), map(lambda x: x, expressao))))}|'
    elif 'sin' in expressao:
        return expressao.replace('i', 'e')
    else:
        return expressao


def expressao_ok(expressao):
    return True if not expressao.replace('.', '').isnumeric() else False
        


def verificar_colar(texto):
    if texto.isnumeric():
        return texto
    else: 
        msg.showinfo(title='Calculadora', message='Só pode colar números!')