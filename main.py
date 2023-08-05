from art import *
from colorama import Fore
import random
import string
import pyperclip

def Menu():
    print(Fore.YELLOW + text2art('Gpassword') + Fore.RESET)
    print('Esolha uma opção:')
    print(Fore.YELLOW + '1. Senha Alfanumerica')
    print('2. Senha com palavras\n99. Sair' + Fore.RESET)

def SenhaAlfaNumericaInput():
    # Solicita ao usuário o tamanho da senha e as opções de caracteres
    try:
        tamanho = int(input('Digite o tamanho da senha: '))
        alfa = input('A senha vai conter letras?s/n ')
        while alfa not in ['S', 's', 'N', 'n']:
            alfa = input('A senha vai conter letras?s/n ')
        number = input('A senha vai conter números?s/n ')
        while number not in ['S', 's', 'N', 'n']:
            number = input('A senha vai conter números?s/n ')
        caracter = input('A senha vai conter caracteres especiais?s/n ')
        while caracter not in ['S', 's', 'N', 'n']:
            caracter = input('A senha vai conter caracteres especiais?s/n ')
    except:
        print(Fore.RED + 'Algo deu errado, tente novamente!' + Fore.RESET)
        SenhaAlfaNumericaInput()

    # Verifica se a configuração é válida
    if tamanho <= 5 or (alfa in ['n', 'N'] and number in ['n', 'N'] and caracter in ['n', 'N']):
        print(Fore.RED + 'Essa configuração não é possivel, tente novamente!' + Fore.RESET)
    elif alfa in ['n', 'N'] and number in ['n', 'N'] and caracter in ['s', 'S']:
        print(Fore.RED + 'Não é possivel gerar senhas apenas com caracteres especiais!Tente novamente' + Fore.RESET)
    else:
        # Cria a lista de caracteres que podem ser usados ​​para gerar a senha
        hash = ''
        if alfa in ['s', 'S']:
            hash += string.ascii_letters
        if number in ['s', 'S']:
            hash += string.digits
        if caracter in ['s', 'S']:
            hash += string.punctuation

        # Gera a senha
        senha = ''.join(random.choice(hash) for i in range(tamanho))
        print(Fore.GREEN + 'Essa é sua senha:\n'+ Fore.RESET, senha )
        pyperclip.copy(senha)
    option = ''
    print('O que gostaria de fazer?')
    print(Fore.YELLOW + '98. Voltar\n99. Sair' + Fore.RESET)
    while option not in ['98', '99']:
        option = input('Escolha uma opção: ')
    if option == '98':
        main()
    else:
        exit()

def word():
    senha = []

    number_word = int(input('Digite o número de palavras que a senha deve ter: '))
    try:
        with open('wordlist.txt', 'r') as arquivo:
            wordlist = arquivo.readlines()
    except:
        print(Fore.RED + 'Arquivo wordlist não encontrado ou vazio!' + Fore.RESET)
        exit()
    while len(senha) < number_word:
        palavra = random.choice(wordlist)
        senha.append(palavra)  

    senha = str(senha).replace('\\n', '').replace("'", "").replace("[", "").replace("]", "").lower().replace(" ", " - ").replace(",", "")
    senha_copy = senha.replace(" ", "").replace("-", "")
    
    print('As palavras que formam sua senha são:\n', Fore.YELLOW, senha, Fore.RESET)
    pyperclip.copy(senha_copy) 
    print(Fore.GREEN + 'Sua senha já está na area de transferencia!' + Fore.RESET)
    print('Você também pode copiar sua senha:\n', Fore.YELLOW, senha_copy, Fore.RESET)
    
    print('O que gostaria de fazer?')
    print(Fore.YELLOW + '98. Voltar\n99. Sair' + Fore.RESET)
    option = ''
    while option not in ['98', '99']:
        option = input('Escolha uma opção: ')
    if option == '98':
        main()
    elif option == '99':
        exit()

def main():
     
    Menu()
    option = ''
    while option not in ['1', '2', '99']:
        option = input('Digite uma opção: ')
    if option == '1':
        SenhaAlfaNumericaInput()
    elif option == '2':
        word()
    elif option == '99':
        exit()

main()