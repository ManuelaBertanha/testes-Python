# Exercício 2:
'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá, então, exibir o valor a ser pago na tela.
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para
a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações
pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma: para pagamentos sem atraso, cobrar o valor da prestação; quando houver atraso,
cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

def valorPagamento(valorPrest, atraso):
  pagamento = valorPrest
  if (atraso > 0):
    pagamento = (1.03*valorPrest) + ((atraso) * (0.001*valorPrest))
  return pagamento


valorPrest = 0.1
qtdPrest = 0
totalDiario = 0.0
while (valorPrest != 0):  # Existe o encadeamento <while...else>
  valorPrest = float(input('Informe o valor da prestação que será paga: '))
  if (valorPrest == 0):
    break
  else:
    atraso = int(input('Informe a quantidade de dias em atraso: '))
    print('Valor a pagar: R$ %.2f \n' % valorPagamento(valorPrest, atraso))
    qtdPrest += 1
    totalDiario += valorPagamento(valorPrest, atraso)

print('\n** Relatório do dia **')
print(f'Quantidade de prestações pagas: {qtdPrest}')
print('Valor total das prestações: R$ %.2f' % totalDiario)
