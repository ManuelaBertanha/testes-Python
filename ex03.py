# Exercício 3:
'''Faça um programa que gere cartas de baralho aleatoriamente (valor e naipe). Para isso, crie uma função que sorteie um valor entre 1 e 13,
sendo: 1 = Às, 11 = J, 12 = Q e 13 = K. Para os naipes, faça o sorteio de um valor entre 1 e 4, sendo: 1 = PAUS, 2 = ESPADAS, 3 = OUROS e 4 = COPAS.
A função deverá retornar uma combinação correspondente à uma carta sorteada. Para um determinado jogo, são necessárias 5 cartas para um jogador.
Crie uma lista com 5 cartas aleatórias e exiba essas cartas. Lembre-se de que não é possível ter duas cartas iguais, já que estamos usando apenas um baralho.'''

import random

def gerarCartas():
  valor = random.randint(1,13)
  naipe = random.randint(1,4)
  return valor, naipe  # Retorna uma tupla


lista = []
carta = gerarCartas()
lista.insert(0,carta)

while (len(lista) < 5):
  carta = gerarCartas()
  if (lista.count(carta) == 0):
    lista.append(carta)

print('Cartas geradas: \n')

for i in range(len(lista)):
  if (lista[i][1] == 1):
    print(f'> {lista[i]} \t {lista[i][0]} de paus')
  elif (lista[i][1] == 2):
    print(f'> {lista[i]} \t {lista[i][0]} de espadas')
  elif (lista[i][1] == 3):
    print(f'> {lista[i]} \t {lista[i][0]} de ouros')
  else:
    print(f'> {lista[i]} \t {lista[i][0]} de copas')
