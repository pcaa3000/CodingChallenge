def sum(val1,val2):
    return val1+val2
def substraccion(val1,val2):
    return val1-val2
def multiplication (val1,val2):
    return val1*val2
def division (val1,val2):
    return val1/val2

operators={
    '/': division,
    '*': multiplication,
    '-': substraccion,
    '+': sum
    }

def math_operation(operator, val1,val2):
    operation=operators.get(operator,"nothing")
    return operation(val1,val2)

print('Calculadora\n')
print(f'Ingrese su operación Mátemática Ej. \n\t10\n\t  +\n\t2\n{"_"*20}\n')
try:
    value=float(input('\t'))    
    operator=input('\t  ')
    while(operators.get(operator,"Invalid")!="Invalid"):
        try:            
            value2=float(input('\t'))
            value=math_operation(operator,value,value2)
            print(f'\t{"_"*5}')
            print(f'\n\t{value}\n')
            operator=input('\t  ')
        except ValueError as e:
            print(e)
            break
except ValueError as e:
    print(e)
  

# result=input('Ingrese su operación Mátemática Ej. 10+2\n\t')
# try:
#     result=eval(result)
#     print(f'\t= {result}\n')
# except ValueError as e:
#     print(e)