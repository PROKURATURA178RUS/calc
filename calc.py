num = input('Введите операцию:')
def add(a,b): 
    c = (a + b)
    return c


def mul(a,b):
    c = (float(a)*float(b))
    return c


def rem(a,b):
        c = (float(a)-float(b))
        return c


def div(a,b):
        c = (float(a)/float(b))
        return c



if '+' in num:
    list_numbers = num.split('+')
    res = float(list_numbers[0])
    for i in range(1,len(list_numbers)):
        list_numbers[i] = float(list_numbers[i])      
        res = add(res , list_numbers[i])
    print(res)
elif '*' in num:
    list_numbers = num.split('*')
    res = float(list_numbers[0])
    for i in range(1,len(list_numbers)):
        list_numbers[i] = float(list_numbers[i])      
        res = mul(res , list_numbers[i])
print(res)


