def strong_deco(func):
    def wrapper_func(name):
        return "<strong>{0}</strong>".format(func(name))
    return wrapper_func

def p_deco(func):
    def wrapper_func(name):
        return "<p>{0}</p>".format(func(name))
    return wrapper_func

def div_deco(func):
    def wrapper_func(name):
        return "<div>{0}</div>".format(func(name))
    return wrapper_func

def outer(func):
    def wrapper_func(n):
        if n<1:
            return 1
        else:
            print("mza aa rha h",n)
            return func(n)
    return wrapper_func
