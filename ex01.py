# Exercício 1

def verMaior(n1, n2, n3):
  maior = n1
  if (n2>n1):
    maior = n2
  if (n3>maior):  # Se usar elif nessa linha, a lógica muda
    maior = n3
  return maior


def verMaiorDeDois(n1, n2, n3):
  if (n1==n2):
    maior = n1
    if (n3>n1):
      maior = n3
  elif (n1==n3):
    maior = n1
    if (n2>n1):
      maior = n2
  elif (n2==n3):
    maior = n2
    if (n1>n2):
      maior = n1
  return maior


n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if (n1 == n2 == n3):
  print('\nOs três números são iguais!')
elif (n1==n2 or n1==n3 or n2==n3):
  print(f'\nNúmero de maior valor: {verMaiorDeDois(n1, n2, n3)}')
else:
  print(f'\nNúmero de maior valor: {verMaior(n1, n2, n3)}')
