import random
from random import choice

def imprime_mensagem_abertura():
    print("********************************")
    print("***Bem vindo no jogo da Forca***")
    print("********************************")

def selecione_dificuldade():

    dificuldade = input("Qual o nível da dificuldade? \n"
                        "(1) Fácil (2) Médio (3) Difícil \n")

    return dificuldade


def carrega_palavra_secreta(dificuldade):

    if dificuldade == "1":
        arquivo = "palavras.txt"
    elif dificuldade == "2":
        arquivo = "palavrasMedio.txt"
    elif dificuldade == "3":
        arquivo = "palavrasDificil.txt"
    else:
        print("Opção inválida. Escolha uma dificuldade de 1 a 3.")

        return None

    with open(arquivo, "r") as file:
        palavras = [linha.strip() for linha in file]

    palavra_secreta = random.choice(palavras).upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def jogar():

    imprime_mensagem_abertura()
    dificuldade = selecione_dificuldade()

    palavra_secreta = carrega_palavra_secreta(dificuldade)
    if not palavra_secreta:
        return

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
           marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)


        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do Jogo")

def imprime_mensagem_perdedor(palavra_secreta):
    def imprime_mensagem_perdedor(palavra_secreta):
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

def imprime_mensagem_vencedor():
    def imprime_mensagem_vencedor():
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

def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

if(__name__ == "__main__"):
    jogar()





