from numpy.random import seed
from numpy.random import randint

from pystat.estatistica import Estatistica

def test_calcula_media_caso_teste_1():
    """
    Caso de teste 1:
        1-2-3-4-5-6-7...

    Entrada:
        valores: 10, 5, 15, -999
        minimo: 0
        maximo: 50
    Saída:
        media = 10
    """

    # Ambiente
    valores = [10, 5, 15, -999]
    minimo = 0
    maximo = 50
    esperado = 10

    # Ação
    retornado = Estatistica.calcula_media(valores, minimo, maximo)

    # Asserção
    assert esperado == retornado

def test_calcula_media_caso_teste_2():
    """
    Caso de teste 2:
        1-2-8-10

    Entrada:
        valores: 10, 25, 15, ...,20
        minimo: 0
        maximo: 5

    Saída:
        media = 0
    """

    # Ambiente
    seed(1)
    valores = randint(10, 150, 100)
    minimo = 0
    maximo = 5
    esperado = 0

    # Ação
    retornado = Estatistica.calcula_media(valores, minimo, maximo)

    # Asserção
    assert esperado == retornado

def test_calcula_media_caso_teste_3():
    """
    Caso de teste 3:
        1-2-3-8-10

    Entrada:
        valores: -999
        minimo: 0
        maximo: 50
    Saída:
        media = 0
    """

    # Ambiente
    valores = [-999]
    minimo = 0
    maximo = 50
    esperado = 0

    # Ação
    retornado = Estatistica.calcula_media(valores, minimo, maximo)

    # Asserção
    assert esperado == retornado

def test_calcula_media_caso_teste_4():
    """
    Caso de teste 4:
        1-2-3-4-7

    Entrada:
        valores: 5, 10, 20, -999
        minimo: 10
        maximo: 50
    Saída:
        media = 15
    """

    # Ambiente
    valores = [5, 10, 20, -999]
    minimo = 10
    maximo = 50
    esperado = 15

    # Ação
    retornado = Estatistica.calcula_media(valores, minimo, maximo)

    # Asserção
    assert esperado == retornado

def test_calcula_media_caso_teste_5():
    """
    Caso de teste 4:
        1-2-3-4-5-7...

    Entrada:
        valores: 10, 40, 100, -999
        minimo: 10
        maximo: 50
    Saída:
        media = 25
    """

    # Ambiente
    valores = [10, 40, 100, -999] # lista
    minimo = 10
    maximo = 50
    esperado = 25

    # Ação
    retornado = Estatistica.calcula_media(valores, minimo, maximo)

    # Asserção
    assert esperado == retornado

def test_calcula_media_caso_teste_6():
    """
    Caso de teste 4:
        1-2-8-9-10...

    Entrada:
        valores: 10, 25, 15,...,20
        minimo: 0
        maximo: 80
    Saída:
        media dos 100 números.
    """

        # Ambiente
    seed(1)
    valores = randint(0, 80, 100)
    minimo = 0
    maximo = 80
    esperado = sum(valores) / 100

    # Ação
    retornado = Estatistica.calcula_media(valores, minimo, maximo)

    # Asserção
    assert esperado == retornado