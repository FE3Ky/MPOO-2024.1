from controle import Controle
from televisao import Televisao

tv = Televisao()
controle = Controle()

def menu():
    while True:
        print("                 Controle                ")
        print("             [O] On | [X] Off            ")
        print("           [A] +Vol | [V] -Vol           ")
        print("           [M] Mute | [S] Unmute         ")
        print("               [1] [2] [3]               ")
        print("               [4] [5] [6]               ")
        print("               [7] [8] [9]               ")
        print("               [0] exit                  ")

        resp = input("Escolha: ").lower()
        if resp == "0":
            break
        elif resp.isdigit() and int(resp) in range(10):
            if tv.ligada:
                controle.mudarCanal(tv, int(resp))
            else:
                print("Televisão Desligada")
        else:
            chamarFuncoes(resp)

def chamarFuncoes(resp):
    match resp:
        case "o":
            return controle.ligarTv(tv)
        case "x":
            return controle.desligarTv(tv)
        case "a":
            return controle.aumentarVolume(tv)
        case "v":
            return controle.diminuirVolume(tv)
        case "m":
            return controle.silenciarVolume(tv)
        case "s":
            return controle.restaurarVolume(tv)
        case _:
            return print('Limite alcançado')

def interacaoTeclado(numero):
    match numero:
        case "o":
            return controle.ligarTv(tv)
        case "x":
            return controle.desligarTv(tv)
        case "a":
            return controle.aumentarVolume(tv)
        case "v":
            return controle.diminuirVolume(tv)
        case _:
            return print('Limite alcançado')

menu()