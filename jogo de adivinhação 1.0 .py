import random
computador = random.randint(0, 5)
print('-=-' * 30)
print(' Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 30)
jogador = int(input('Em que nº eu pensei ? '))
if jogador == computador:
    print('Parabéns!Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no nº {} e não no nº {} !'.format(computador, jogador))


