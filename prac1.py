def filled_square():
    for i in range(5):
        for j in range(5):
            print('*',end=' ')
        print('')
    print('done')

def bordered_square():
    for i in range(5):
        if i==0 or i==4:
            for j in range(5):
                print('*',end=' ')
            print('')
        else:
            for j in range(5):
                if j==0:
                    print('*',end=' ')
                elif j==4:
                    print('*')
                else:
                    print(' ',end=' ')
    print('done')

def bordered_dia():
    for i in range(10):
        if i==0 or i==9:
            for j in range(10):
                print('*',end=' ')
            print('')
        else:
            for j in range(10):
                if i==j:
                    print('*',end=' ')
                elif i+j == 9:
                    print('*',end=' ')
                elif j==0:
                    print('*',end=' ')
                elif j==9:
                    print('*')
                else:
                    print(' ',end=' ')
    print('done')

def diagonals():
    for i in range(10):
        for j in range(10):
            if i==j:
                print('*',end=' ')
            elif i+j == 9:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('')
    print('done')

def diamond():
    for i in range(5):
        for j in range(5-(i+1)):
            print (" ",end=" ")
        for k in range(2*i+1):
            print('*',end=' ')
        print('')
    for i in range(4):
        for j in range(i+1):
            print (" ",end=" ")
        for k in range(2*(3-i)+1):
            print('*',end=' ')
        print('')

def bordered_diamond():
    for i in range(11):
        print('*',end=' ')
    print('')
    for i in range(5):
        print('*',end=' ')
        for j in range(5-(i+1)):
            print (" ",end=" ")
        for k in range(2*i+1):
            print('*',end=' ')
        for l in range(5-(i+1)):
            print (" ",end=" ")
        print('*')
    for i in range(4):
        print('*',end=' ')
        for j in range(i+1):
            print (" ",end=" ")
        for k in range(2*(3-i)+1):
            print('*',end=' ')
        for l in range(i+1):
            print (" ",end=" ")
        print('*')
    for i in range(11):
        print('*',end=' ')
    print('')

filled_square()
bordered_square()
bordered_dia()
diagonals()
diamond()
bordered_diamond()
