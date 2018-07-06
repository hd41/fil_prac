def foo(bar):
    return bar+1

def foo2(a,b):
    return a*b

def ret_fun(x):
    def fun(x):
        return "fun"*x
    return fun

def call_foo_with_arg(foo, bar):
    return foo(bar)
def call_foo_with_arg1(x,y):
    return foo(x)

print(foo(3))
print(call_foo_with_arg(foo,3))
print(call_foo_with_arg1(2,3))

print(foo(3)== call_foo_with_arg(foo,3))

ding_ding = ret_fun(2)
print(ding_ding(3))

print (ding_ding)
