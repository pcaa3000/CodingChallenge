import random

options={"Rock":1,"Paper":2,"Scissors":3}
players={"Player1":0,"Player2":0}

def play_yankenpo(player1,player2):
    global players
    global options
    if (player1==player2):
        for player in players:
            players[player]+=1
        return "Empataste!!"
    else:
        #Scissors->Paper->Rock->Scissors
        player1=player1-1
        if player1==options["Rock"]-1:
            player1=options["Scissors"]

        if player2==player1:
            players["Player1"]+=1
            return "Ganaste!!"
        else:
            players["Player2"]+=1
            return "Perdiste!!"

title="Juego YAN-KEN-PO  -  Piedra-Papel-Tijera"
print(f' {"*"*len(title)}')
print(f'*{title}*')
print(f' {"*"*len(title)}\n')
game=0
condition=True
match=not condition
while condition:
    flag_option=True
    print(f'{"*"*6}Ingrese su opcion{"*"*6}\n\t(1) Piedra\n\t(2) Papel\n\t(3) Tijera\n\t(0) Salir\n{"_"*30}')
    while flag_option:
        try:
            option=int(input(f'\n\tSu Opción: '))
            flag_option=(option<0 or option>3)
        except Exception as e:
            flag_option=True
            continue
        finally:
            if flag_option:
                print('\tOpcion No valida!!')
        
    if option==0:
        break
    option_machine=random.randrange(1,3)
    
    message=" Escogiste  : "
    message+=list(options.keys())[list(options.values()).index(option)]
    print(f'\n\t {"-"*(len(message)+1)}')
    print(f'\t|{message} |')
    message=" Computadora: "
    message+=list(options.keys())[list(options.values()).index(option_machine)]
    print(f'\t|{message} |')
    print(f'\t {"-"*(len(message)+1)}\n')

    message=play_yankenpo(option,option_machine)
    print(f'\t{message}, el juego.')    

    if (match):        
        condition=(game<3)
        game+=1
        if condition:
            print(f'\n\t\tJuego N°{game}')
    else:
        match=input("Deseas Jugar una partida de 2/3 (S/n): ")
        condition=(match.lower()=='s')
        match=condition
        for player in players:
            players[player]=0
        game+=1
        print(f'\n\t\tJuego N°{game}')

if match:
    if players["Player1"]> players["Player2"]:
        print("\t\tGanaste la partida, Felicidades!!")
    elif players["Player1"]< players["Player2"]:
        print("\t\tLo Siento!!!, Perdiste la partida")
    else:
        print("\t\tEmpate!!, Buena Partida.")
    print(f'\t\tResultado: tú:{players["Player1"]} / Computador:{players["Player2"]}')