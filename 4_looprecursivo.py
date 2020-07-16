def loop_recursive(message,numbertimes):    
    if numbertimes>1: 
        numbertimes-=1        
        loop_recursive(message,numbertimes)    
    print(message)


message=input('Ingrese un mensaje: ')
numbertimes=int(input('¿Cuántas veces desea ver el mensaje? '))

print(f'\n{"*"*len(message)}')
#print(f'{loop_recursive(message,number_times)}')
loop_recursive(message,numbertimes)
print(f'{"*"*len(message)}\n')
