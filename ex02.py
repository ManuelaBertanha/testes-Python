# Manuela de Caria Bertanha | TIA 32152851
# Michele Ramos Borowski | TIA 32166052

# Exercício 2:

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
