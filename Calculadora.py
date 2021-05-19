class Calculadora:
    from math import sin, cos, tan, radians

    expressao = ''
    historico = {}
    mudar_numero = False
    graus = True
    
    @classmethod
    def click_number(cls, current_number, new_number):
        if (current_number['text'] == '0') or Calculadora.mudar_numero:
            if new_number == '.' and Calculadora.mudar_numero:
                current_number.config(text='0')
            else:
                current_number.config(text='')
            Calculadora.mudar_numero = False
        elif new_number=='.' and '.' in current_number['text']:
            return
        current_number.config(text=current_number['text'] + new_number)
    
    
    @classmethod
    def setGraus(cls, ativado):
        Calculadora.graus = ativado
    
    
    @classmethod
    def backspace(cls, current_number):
        if len(current_number['text']) > 1:
            current_number.config(text=current_number['text'][:-1])
        else:
            current_number.config(text='0')
    
    
    @classmethod
    def c(cls, current_number):
        Calculadora.expressao = ''
        current_number.config(text='0')

    
    # Expressões Binárias
    @classmethod
    def somar(cls, current_number):
        Calculadora.igual(current_number)
        Calculadora.expressao = current_number['text'] + '+'
        
    
    @classmethod
    def subtrair(cls, current_number):
        Calculadora.igual(current_number)
        Calculadora.expressao = current_number['text'] + '-'
    
    
    @classmethod
    def multplicar(cls, current_number):
        Calculadora.igual(current_number)
        Calculadora.expressao = current_number['text'] + '*'
        
    
    @classmethod
    def dividir(cls, current_number):
        Calculadora.igual(current_number)
        Calculadora.expressao = current_number['text'] + '/'
    
    
    @classmethod
    def potencia(cls, current_number):
        Calculadora.igual(current_number)
        Calculadora.expressao = current_number['text'] + '**'
    
    @classmethod
    def mostrar_resultado(cls, current_number):
        try:
            Calculadora.expressao = Calculadora.expressao + current_number['text']
            current_number.config(text=str(eval(Calculadora.expressao)))
            Calculadora.mudar_numero = True
        except SyntaxError:
            print(f'Erro de sintaxe ao mostrar resultado {Calculadora.expressao}')
    
    
    @classmethod
    def gravar_expressao(cls):
        from utilitarios import formatar_expressao, expressao_ok
        expressao_formatada = formatar_expressao(Calculadora.expressao)
        try:
            if expressao_ok(expressao_formatada):
                Calculadora.historico[f'{expressao_formatada}'] = eval(Calculadora.expressao)
        except SyntaxError:
            print(f'Erro de sintaxe ao gravar expressão {Calculadora.expressao}')
        print(Calculadora.historico)
        
        
    @classmethod
    def igual(cls, current_number):
        Calculadora.mostrar_resultado(current_number)
        Calculadora.gravar_expressao()
        Calculadora.expressao = ''
    
    
    # Expressões Unitárias
    @classmethod
    def absoluto(cls, current_number):
        resultado = abs(float(current_number['text']))
        Calculadora.gravar_mostrar_limpar(current_number, f"|{current_number['text']}|", resultado)
    
    @classmethod
    def seno(cls, current_number):
        if Calculadora.graus:
            resultado = Calculadora.sin(Calculadora.radians(float(current_number['text'])))
        else:
            resultado = Calculadora.sin(float(current_number['text']))
        Calculadora.gravar_mostrar_limpar(current_number, f"sen({current_number['text']})", resultado)
    
    
    @classmethod
    def cosseno(cls, current_number):
        if Calculadora.graus:
            resultado = Calculadora.cos(Calculadora.radians(float(current_number['text'])))
        else:
            resultado = Calculadora.cos(float(current_number['text']))
        Calculadora.gravar_mostrar_limpar(current_number, f"cos({current_number['text']})", resultado)
    
    
    @classmethod
    def tangente(cls, current_number):
        if Calculadora.graus:
            resultado = Calculadora.tan(Calculadora.radians(float(current_number['text'])))
        else:
            resultado = Calculadora.tan(float(current_number['text']))
        Calculadora.gravar_mostrar_limpar(current_number, f"tan({current_number['text']})", resultado)
        
        
    @classmethod
    def gravar_mostrar_limpar(cls, current_number, expressao_formatada, resultado):
        Calculadora.historico[expressao_formatada] = resultado
        current_number.config(text=str(resultado))
        Calculadora.expressao = ''
        Calculadora.mudar_numero = True
        
