from functools import wraps


def arg_parser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        n = args[0].split('\n')
        for idx, el in enumerate(n):
            n[idx] = float(el) if '.' in el else int(el)
        n.extend(args[1:])
        return func(*n, **kwargs)
    return wrapper
