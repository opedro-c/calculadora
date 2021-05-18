def aux():
    pass

def formatar_expressao(expressao):
    if '**' in expressao:
        return expressao.replace('**', '^')
    elif '*' in expressao:
        return expressao.replace('*', 'x')
    else:
        return expressao
