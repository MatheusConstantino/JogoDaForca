from bs4 import BeautifulSoup
from urlib.request import urlopen
html = urlopen("https://www.dicionariodenomesproprios.com.br/top-brasil/")
bsObj = BeuatifulSoup(html.read(), 'html.parser')
lista = bsObj.find('li')
for x in lista:
    if '<span>' in str(x):
        print(x.find('a').get_text())
        
def desenha(erros,letras,palavra):
    forca = '\n    +-----+\n    |     |\n          |\n          |\n          |\n          |\n============','\n    +-----+\n    |     |\n    O     |\n          |\n          |\n          |\n============','\n    +-----+\n    |     |\n    O     |\n   /      |\n          |\n          |\n============','\n    +-----+\n    |     |\n    O     |\n   /|     |\n          |\n          |\n============','\n    +-----+\n    |     |\n    O     |\n   /|\    |\n          |\n          |\n============','\n    +-----+\n    |     |\n    O     |\n   /|\    |\n   /      |\n          |\n============','\n    +-----+\n    |     |\n    O     |\n   /|\    |\n   / \    |\n          |\n============'
    print(forca[erros])
    traços = ''
    cont = 0
    i = 0
    while (i < len(palavra)):
        if palavra[i] in letras:
            traços = traços + palavra[i] + ' '
            cont+=1
        else:
            traços = traços + '_ '
        i+=1 
    print(traços)
def sorteia():
    import random
    palavra = random.choice(html)
    palavra = palavra.replace("á","a")
    palavra = palavra.replace("é","e")
    palavra = palavra.replace("í","i")
    palavra = palavra.replace("ó","o")
    palavra = palavra.replace("ú","u")
    palavra = palavra.replace("à","a")
    palavra = palavra.replace("è","e")
    palavra = palavra.replace("ì","i")
    palavra = palavra.replace("ò","o")
    palavra = palavra.replace("ù","u")
    palavra = palavra.replace("â","a")
    palavra = palavra.replace("ê","e")
    palavra = palavra.replace("î","i")
    palavra = palavra.replace("ô","o")
    palavra = palavra.replace("û","u")
    palavra = palavra.replace("ã","a")
    palavra = palavra.replace("õ","o")
    palavra = palavra.replace("ä","a")
    palavra = palavra.replace("ë","e")
    palavra = palavra.replace("ï","i")
    palavra = palavra.replace("ö","o")
    palavra = palavra.replace("ü","u")
    x=0
    vogal=0
    while x < len(palavra):
        if palavra[x] in 'aeiou':
            vogal+=1
        x+=1
    if (len(palavra)>4) and vogal>=2:
        return palavra
    else:
        return sorteia()
def again():
    while True:
        retry = ''
        retry = str(input('Deseja jogar novamente? '))
        if (retry.lower() == 'sim') or (retry.lower() == 's') or (retry.lower() == 'yes') or (retry.lower() == 'y'):
            return True
        else:
            if (retry.lower().replace("ã","a") == 'nao') or (retry.lower() == 'n') or (retry.lower() == 'no'):
                return False
            else:
                print('Informação inválida. Tente novamente.')
def win(letras,palavra):
    erros = 0
    cont = 0
    y = 0
    certas = ''
    erradas = ''
    while (y < len(letras)):
        if letras[y] in palavra:
            certas = certas + letras[y]
            cont+=1
        else:
            erradas = erradas + letras[y]
            erros+=1
        y+=1
    if (cont == len(set(palavra))):
        print('Parabéns ' + '''"Você Venceu!"''')
        return True
    else:
        return False
def chute(letras,palavra):
    erros = 0
    cont = 0
    y = 0
    certas = ''
    erradas = ''
    while (y < len(letras)):
        if letras[y] in palavra:
            certas = certas + letras[y]
            cont+=1
        else:
            erradas = erradas + letras[y]
            erros+=1
        y+=1
    if (erros >= 6):
        desenha(erros,letras,palavra)
        print('Que Pena, Você Perdeu!')
        print('Palavra: ' + palavra)
        if again():
            return 'gg'
        else:
            import sys
            sys.exit()
    desenha(erros,letras,palavra)
while True:
    palavra = ''
    letras = ''
    erros = 0
    palavra = sorteia()
    desenha(erros,letras,palavra)
    traços = ''
    z=0
    while True:
        letra = ''
        letra = str(input('Chute uma letra: ')).lower()
        if (len(letra)==1) and (letra in 'abcdefghijklmnopqrstuvxwyzç'):
            if (letra in letras):
                print('Letra já utilizada.')
            else:
                letras = letras + letra
                if chute(letras,palavra) == 'gg':
                    break
                if win(letras,palavra):
                    print('Palavra: ' + palavra)
                    if again():
                        break
                    else:
                        import sys
                        sys.exit()
        else:
            print('Letra inválida. Tente novamente.')
