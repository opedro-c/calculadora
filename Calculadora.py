class Calculadora:
    expressao = ''
    historico = {}
    mudar_numero = False
    
    @classmethod
    def click_number(cls, current_number, new_number):
        if (current_number['text'] == '0') or Calculadora.mudar_numero:
            if new_number == '.' and Calculadora.mudar_numero:
                current_number.config(text='0')
            else:
                current_number.config(text='')
            Calculadora.mudar_numero = False
        current_number.config(text=current_number['text'] + new_number)
    
    
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
    def absoluto(cls, current_number):
        Calculadora.expressao = f"abs({current_number['text']})"
        current_number.config(text='')
        Calculadora.igual(current_number)
    
    @classmethod
    def seno(cls, current_number):
        pass
    
    
    @classmethod
    def cosseno(cls, current_number):
        pass
    
    
    @classmethod
    def tangente(cls, current_number):
        pass
    
    
        
    @classmethod
    def mostrar_resultado(cls, current_number):
        try:
            Calculadora.expressao = Calculadora.expressao + current_number['text']
            current_number.config(text=str(eval(Calculadora.expressao)))
            Calculadora.mudar_numero = True
        except SyntaxError:
            print(f'Erro de sintaxe ao mostrar resultado {Calculadora.expressao}')
    
    
    @classmethod
    def igual(cls, current_number):
        from utilitarios import formatar_expressao, expressao_ok
        Calculadora.mostrar_resultado(current_number)
        expressao_formatada = formatar_expressao(Calculadora.expressao)
        try:
            if expressao_ok(expressao_formatada):
                Calculadora.historico[f'{expressao_formatada}'] = eval(Calculadora.expressao)
        except SyntaxError:
            print(f'Erro de sintaxe em igual {Calculadora.expressao}')
        print(Calculadora.historico)
        Calculadora.expressao = ''
