from tkinter import messagebox as msg


def formatar_expressao(expressao):
    if '**' in expressao:
        return expressao.replace('**', '^')
    elif '*' in expressao:
        return expressao.replace('*', 'x')
    return expressao


def expressao_ok(expressao):
    if expressao.find('-') == 0:
        somente_num_negativo = expressao.replace('-', '', 1).replace('.', '').isnumeric()
        return not somente_num_negativo
    somente_num = expressao.replace('.', '').isnumeric()
    return not somente_num


def verificar_colar(texto):
    texto_tratado = texto.replace('.','').strip()
    if texto_tratado.isnumeric():
        return texto_tratado
    msg.showinfo(title='Calculadora', message='Só pode colar números!')
