class Calculadora:
    from math import sin, cos, tan, radians, sqrt, factorial
    
    
    seno, cosseno, tangente = sin, cos , tan
    raiz_quad, fatorial = sqrt, factorial
    expressao = ''
    historico = {}
    mudar_numero = False
    graus = 1
    
    @classmethod
    def getHistorico(cls): # Falta implementar
        return Calculadora.historico
    
    
    @classmethod
    def setGraus(cls, ativado):
        Calculadora.graus = ativado
    
    
    @classmethod
    def clicar_numero(cls, current_number, new_number):
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
    def inverter_valor(cls, current_number):
        current_number.config(text=f"-{current_number['text']}")

    
    # Expressões Binárias
    @classmethod
    def operacoes_binarias(cls, current_number, operacao):
        Calculadora.igual(current_number)
        Calculadora.expressao = current_number['text'] + operacao
    
    
    @classmethod
    def mostrar_resultado(cls, current_number):
        Calculadora.expressao = Calculadora.expressao + current_number['text']
        current_number.config(text=str(eval(Calculadora.expressao)))
        Calculadora.mudar_numero = True
        
    
    
    @classmethod
    def gravar_expressao(cls):
        from utilitarios import formatar_expressao, expressao_ok
        expressao_formatada = formatar_expressao(Calculadora.expressao)
        if expressao_ok(expressao_formatada):
            Calculadora.historico[f'{expressao_formatada}'] = eval(Calculadora.expressao)
        
        
        
    @classmethod
    def igual(cls, current_number):
        Calculadora.mostrar_resultado(current_number)
        Calculadora.gravar_expressao()
        Calculadora.expressao = ''
    
    
    # Expressões Unitárias
    @classmethod
    def operacoes_trigonometricas(cls, current_number, func, operacao):
        if Calculadora.graus:
            resultado = func(Calculadora.radians(float(current_number['text'])))
        else:
            resultado = func(float(current_number['text']))
        Calculadora.gravar_mostrar_limpar(current_number, f"{operacao}({current_number['text']})", resultado)
    
    
    @classmethod
    def operacoes_unitarias(cls, current_number, func, operacao):
        resultado = func(float(current_number['text']))
        Calculadora.gravar_mostrar_limpar(current_number, operacao, resultado)

    
    @classmethod
    def gravar_mostrar_limpar(cls, current_number, expressao_formatada, resultado):
        Calculadora.historico[expressao_formatada] = resultado
        current_number.config(text=str(resultado))
        Calculadora.expressao = ''
        Calculadora.mudar_numero = True
