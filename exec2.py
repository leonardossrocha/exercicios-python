while True:
    comando = input("Digite 'sair' para desligar o motor: ")

    if comando.lower() == 'sair':
        print("Desligando o motor...")
        break   
    else: print("O motor continua a rodar!")