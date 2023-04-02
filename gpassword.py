from art import *
import main

tprint("Gpassword")

print("Gpassword gera senhas de alto nível de segurança contendo letras, numeros e simbolos especiais.\n")

print("1. Senhas com 8 caracteres\n2. Senhas com 12 caracteres\n99. Para sair\n")

senha_gerada = False
while senha_gerada == False:

    escolha = int(input("Escolha uma das opões: "))

    if escolha == 1:
        senha = main.oito()
        print(f"{senha}")
    elif escolha == 2:
        senha = main.doze()
        print(f"{senha}")
    elif escolha == 99:
        print("Você saiu!")
        exit()  
    elif escolha != 1 and escolha != 2:
            print("Entrada invalida!")
