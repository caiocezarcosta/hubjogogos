import random



def jogar_forca():

    menssagem_boas_vindas()

    palavra_secreta = importa_palavra()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    #Enquanto true enforcoue true acertou
    while(not enforcou and not acertou):

        chute = pede_chute()
        print("Jogando...")
        index = 0
        if(chute in palavra_secreta):
           marca_chute_certo(palavra_secreta,chute , letras_acertadas)
        else:
            erros +=1
            desenha_forca(erros)
            print("Você errou, ainda faltam {} tentativas".format(7 - erros))
        enforcou = erros == 7
        if("_" not in letras_acertadas):
            break
        print(letras_acertadas)

    if("_" not in letras_acertadas):
            menssagem_ganhador()

    else:
        menssagem_perdedor(palavra_secreta)
def marca_chute_certo(palavra_secreta , chute , letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra

        index += 1
def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute
def inicializa_letras_acertadas(palavra):
     lista = ["_" for letra in palavra]
     return lista
def menssagem_boas_vindas():
    #Menssagem de boas vindas
    print("*********************************")
    print("Bem vindo ao jogo da Forca")
    print("*********************************")
def importa_palavra():
    palavras = []
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta
def menssagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def menssagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar_forca()
    #Comparar pra ver se o usuario vai colocar letra repetida

