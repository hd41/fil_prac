from decorator_module import *

@div_deco
@p_deco
@strong_deco
def getText(name):
     return name

print (getText("himanshu"))

@outer
def getFact(n):
    if n==0:
        return 1
    else:
        return n*getFact(n-1)

print(getFact(6))
