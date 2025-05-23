from decorador_inutil import nome_do_decorador
from time_decorator import time_measure_decorator


@nome_do_decorador
def soma(x, y):

    return x + y


@time_measure_decorator
def soma2(x, y):

    return x + y


if __name__ == "__main__":

    a = 5

    b = 10

    x = soma(a, b)

    print(x)

    y = soma2(a, b)

    print(y)
