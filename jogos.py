import adivinhacao
import forca

def escolha_jogo():
    print("*********************************")
    print("Escolha seu jogo")
    print("*********************************")
    print("(1) Forca (2) Adivinhação")
    jogo = input("Escolha o jogo: ")
    jogo = int(jogo)
    if(jogo == 1):
        print("Jogando forca")
        forca.jogar_forca ()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolha_jogo();