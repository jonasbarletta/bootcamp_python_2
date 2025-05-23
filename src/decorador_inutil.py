from functools import wraps


def nome_do_decorador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Essa funcionalidade inútil foi acrescentada à função.")
        return result

    return wrapper
