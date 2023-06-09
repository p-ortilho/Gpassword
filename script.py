import random

def oito():
    lista_numero = []
    lista_letra = []
    letras = "abcdefghijklmnopqrstuvwyz"
    caracter = [33, 35, 36, 38, 63, 64]
    caracter_especial = []
    senha = []

    while len(lista_numero) < 5:
        numero = random.randint(0, 9)
        lista_numero.append(numero)

    letra_minuscula = random.choice(letras)
    letra_maiuscula = random.choice(letras)
    letra_maiuscula = letra_maiuscula.upper()

    lista_letra.append(letra_minuscula)
    lista_letra.append(letra_maiuscula)

    caracter_especial.append(chr(random.choice(caracter))) 
    
    senha =lista_letra + lista_numero + caracter_especial

    random.shuffle(senha)

    senha = str(senha).strip("[]").replace(",", "").replace("'", "").replace(" ", "")

    return senha

def doze():
    lista_numero = []
    lista_letra = []
    letras = "abcdefghijklmnopqrstuvwyz"
    caracter = [33, 35, 36, 38, 63, 64]
    caracter_especial = []
    senha = []
    letra_maiuscula = []

    while len(lista_numero) < 7:
        numero = random.randint(0, 9)
        lista_numero.append(numero)

    while len(lista_letra) < 3:
        lista_letra.append(random.choice(letras))
    
    letra_maiuscula.append(random.choice(letras.upper()))
    caracter_especial.append(chr(random.choice(caracter)))

    senha = lista_letra + lista_numero + letra_maiuscula + caracter_especial

    random.shuffle(senha)

    senha = str(senha).strip("[]").replace(",", "").replace("'", "").replace(" ", "")

    return senha

def word():
    senha = []

    with open("wordlist.txt", "r") as arquivo:
        wordlist = arquivo.readlines()

        while len(senha) <= 5:
            palavra = random.choice(wordlist)
            senha.append(palavra)

        for item in range(len(senha)):
            senha[item] = senha[item].replace("\n", "")
        
        senha = str(senha).replace("'", "").replace("[", "").replace("]", "").lower().replace(" ", " - ").replace(",", "")
        senha_copia = senha.replace(" ", "").replace("-", "")
    return f"\nPalavras da sua senha\n\n\t{senha}\n\nSenha para copia: {senha_copia}\n"