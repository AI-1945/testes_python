# 1º exemplo

def decorator_simples(funcao_chamada):
    return funcao_chamada(*args, **kwargs)
@decorator_simples
def diz_ola():
    print('Ola')

#  é preciso entender que decorators são apenas
#  um syntactic sugar (açúcar sintático) da linguagem. 
#  Na verdade, o interpretador do Python transforma o 
#  código do primeiro exemplo no seguinte código:

"""
#diz_ola = decorator_simples(diz_ola)
#$ diz_ola()
#>>> 'ola'
"""

# 2º exemplo
def imprime(funcao):
    def inner():
        print(funcao)
    return inner
@imprime
def diz_ola():
    return 'Ola'

"""
#$ diz_ola()
#>>> <function diz_ola ... >
"""
# OBS = decoradores sao clojures e clojures sao funções
# dentro de funcoes
# *args = argumentos listas posicionais
# **kwargs = argumentos dict


# 3º exemplo = Como combinar o usu do decorator
def timestamp(funcao_chamada):
    def inner(*args, **kwargs):
        from datetime import date time
        print('funcao_chamada em %s' % (datetime))
        return funcao_chamada(*args, **kwargs)
    return inner

def logger(funcao_chamada):
    def inner(*args, **kwargs):
        print(funcao_chamada)
        return funcao_chamada(*args, **kwargs)
    return inner

@timestamp
@logger
diz_ola():
    print('Ola')

# este codigo é interpretado da seguinte forma
#$ diz_ola = timestamp(logger(diz_ola))
#$ diz_ola()
#>>> chamado em 2015-04-12 14:31:50.548640
#>>> <function diz_ola at ... >

# Ou seja, o decorador logger, receberá a função retornada
# pelo decorator timestamp. Mas e se o objetivo fosse 
# que o decorator suportasse parâmetros? Veja como este
# objetivo pode ser atingido:
def usuario_valido(usuario, msg):
    def decorator(funcao_chamada):
        def inner(*args, **kwargs):
            if usuario:
                return funcao_chamada(*args, **kwargs)
            else:
                raise AttributeError, msg
        return inner
    return decorator
@usuario_valido(True, "usuario e valido")
def diz_ola()
    print('Ola')

# $ diz_ola()
# >>> usuario e valido

@usuario_valido(False, "usuario e valido")
def diz_ola():
    print('Ola')

# $ diz_ola()
# >>> AttributeError: usuario nao e valido

# 4º exemplos imcompletos
def logger(funcao):
    def inner(*a, **k):
        return funcao(*a, **k)
    return inner
@logger
def diz_ola():
    """O doc desta funcao retorna no metodo __doc__"""

def logger(funcao):
    def inner(*a, **k):
        return funcao(*a, **k)
    inner.__name__, inner.__doc__ = funcao.__name__
    return inner

# SEM O DECORATOR
def diz(msg):
    print(msg)

# $ import inspect
# $ inspect.getargspec(diz)

# COM DECORATOR
@logger
def diz(msg):
    print(msg)

##################################################
# APLICAÇÂO REAL DOS DECORADORES

rotas = []

def rota(endereco):
    def wrapper(fn):
        rotas.append((endereco, fn))

    return wrapper

@rota('/index/')
def home_view():
    return 'Pagina inicial'

@rota('/contato/')
def contato_view():
    return 'Pagina de contato'

print rotas[0][1]()  # Pagina inicial
print rotas[1][1]()  # Pagina de contato
print rotas
# [('/index/', < function home_view at 0xb736580c >),
#  ('/contato/', < function contato_view at 0xb7365b8c >)]

####################################################
