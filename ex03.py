# Manuela de Caria Bertanha | TIA 32152851
# Michele Ramos Borowski | TIA 32166052

# Exercício 3:

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
