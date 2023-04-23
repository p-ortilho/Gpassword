from art import *
import script

tprint("Gpassword")

print("Gpassword gera senhas de alto nível de segurança contendo letras, numeros, simbolos especiais e palavras.\n")

print("1. Senhas com 8 caracteres\n2. Senhas com 12 caracteres\n3. Senhas com palavras\n99. Para sair\n")

senha_gerada = False
while senha_gerada == False:

    escolha = int(input("Escolha uma das opões: "))

    if escolha == 1:
        senha = script.oito()
        print(f"{senha}")
    elif escolha == 2:
        senha = script.doze()
        print(f"{senha}")
    elif escolha == 3:
         senha = script.word()
         print(f"{senha}")
    elif escolha == 99:
        print("Você saiu!")
        exit()  
    elif escolha != 1 and escolha != 2:
            print("Entrada invalida!")
