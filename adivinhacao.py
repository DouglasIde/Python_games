import random

def jogar():
    print("********************************")
    print("Bem vindo no jogo de Adivinhação")
    print("********************************")


    numero_secreto = round(random.randrange(1,101))
    total_tentativas = 0
    pontos = 1000


    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5



    for rodada in range(1, total_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada,total_tentativas))
        chute_str = input("Digite um numero entre 1 a 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 a 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Seu chute foi maior que o número")
            elif(menor):
                print("Seu chute foi menor que o número")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            rodada = rodada + 1

if(__name__ == "__main__"):
    jogar()
