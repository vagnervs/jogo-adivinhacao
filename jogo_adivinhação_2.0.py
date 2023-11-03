import random
comp =  random.randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais! Tente mais uma vez.')
        else:
            print('Menos! Tente novamente. ')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))


