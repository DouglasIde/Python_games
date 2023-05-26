import adivinhacao
import forca

print("********************************")
print("********Escolha seu jogo********")
print("********************************")

print("(1) Jogo da Forca (2) Jogo de Adivinhação")

jogo = int(input("Qual o Jogo?: "))

if(jogo == 1):
    print("Jogar o jogo da Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogar o jogo da Adivinhação")
    adivinhacao.jogar()

