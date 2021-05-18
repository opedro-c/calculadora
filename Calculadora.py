class Calculadora:
    expressao = ''
    historico = {}
    mudar_numero = False
    
    @classmethod
    def click_number(cls, current_number, new_number):
        if current_number['text'] == '0' or Calculadora.mudar_numero:
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
    def mostrar_resultado(cls, current_number):
        try:
            Calculadora.expressao = Calculadora.expressao + current_number['text']
            current_number.config(text=str(eval(Calculadora.expressao)))
            Calculadora.mudar_numero = True
        except SyntaxError:
            print('Erro de sintaxe ao mostrar resultado')
    
    @classmethod
    def somar(cls, current_number):
        Calculadora.mostrar_resultado(current_number)
        Calculadora.expressao = current_number['text'] + '+'
        
    
    @classmethod
    def subtrair(cls, current_number):
        Calculadora.mostrar_resultado(current_number)
        Calculadora.expressao = current_number['text'] + '-'
    
    
    @classmethod
    def multplicar(cls, current_number):
        Calculadora.mostrar_resultado(current_number)
        Calculadora.expressao = current_number['text'] + '*'
        
    
    @classmethod
    def dividir(cls, current_number):
        Calculadora.mostrar_resultado(current_number)
        Calculadora.expressao = current_number['text'] + '/'
    
    
    @classmethod
    def igual(cls, current_number):
        from utilitarios import formatar_expressao
        
        
        Calculadora.mostrar_resultado(current_number)
        expressao_formatada = formatar_expressao(Calculadora.expressao)
        try:
            Calculadora.historico[f'{expressao_formatada}'] = eval(Calculadora.expressao)
        except SyntaxError:
            print('Erro em igual')
        print(Calculadora.historico)
        Calculadora.expressao = ''
