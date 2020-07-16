vowels=('a','e','i','o','u','á','é','í','ó','ú')

Text=input('Ingrese un Texto:\n')
for vocal in vowels:
    Text=Text.replace(vocal,"")
    Text=Text.replace(vocal.upper(),"")

print(f'\n{"-"*30}')
print(Text)
print(f'{"-"*30}\n')