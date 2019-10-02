# @decorator é uma técnica um açucar sintatico, que ajudam a melhorar o codigo.

# 1º - EXEMPLOS BASICOS

def decorator_simples(funcao_chamada):
    return funcao_chamada(*args, **kwargs)
@decorator_simples
def diz_ola():
    print('Ola')

"""
Como o python encherga o codigo acima?
diz_ola = decorator_simples(diz_ola)
$ diz_ola()
>>> 'Ola'
"""


# 2º - EXEMPLO 

def imprimi(funcao):
    def inner():
        print(funcao)
    return inner
@imprimi
def diz_ola():
    return 'Ola'
$ diz_ola()
>>> <function diz_ola...>

# isso é o que chamamos de clojures significa funcao dentro de funcao,

# 3º - EXEMPLO MAIS COMPLETO

def logger(funcao_chamada):
    def inner(*args, **kwargs):
        print(funcao_chamada)
        return funcao_chamada(*args, **kwargs)
    return inner
@logger
def diz(msg='ola'):
    print('ola')

$ diz()
>>> <function diz ...>
>>> 'ola' 

OBS : *args (sao argumentos em forma de listas)
OBS : **kwargs (sao argumentos passados em forma de dicionarios)
