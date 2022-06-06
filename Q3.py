def calc(x,operator,y):
    if (operator=='+'):
        print(x+y)
    elif (operator=='-'):
        print(x-y)
    elif (operator== '*'):
        print(x*y)
    elif (operator== '/'):
        print(x/y)
    elif (operator=='and'):
        print(x and y)
    elif (operator=='or'):
        print(x or y)
    # else:
    #     print("choose any one from (+,-,*,/,or,and)")

x=int(input())
op=input()
y=int(input())
calc(x,op,y)