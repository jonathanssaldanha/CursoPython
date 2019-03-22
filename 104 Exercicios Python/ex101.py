print('===============Primeiro programa de contas do jonathan============')

salario = float(input('\nDigite seu salario: R$ '))

contaProduto = float(input('Digite o valor recebido dos produtos: \t\t\t\tR$ '))
somaSaldo = salario + contaProduto
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaServiço = float(input('Digite o valor recebido dos serviços: \t\t\t\tR$ '))
somaSaldo = somaSaldo + contaServiço
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaHelp = float(input('Digite o valor recebido por doação: \t\t\t\tR$ '))
somaSaldo = somaSaldo + contaHelp
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaEmprestimo = float(input('Digite o valor recebido pelo emprestimo: \t\t\tR$ '))
somaSaldo = somaSaldo + contaEmprestimo
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaFixa = float(input('\nDigite o valor total das suas contas Fixas: \t\tR$ '))
somaSaldo = somaSaldo - contaFixa
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaVariavel = float(input('Digite o valor total das suas contas Variaveis: \tR$ '))
somaSaldo = somaSaldo - contaVariavel
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
investimento = float(input('Quanto do seu dinheiro vc investio esse mes: \t\tR$ '))
somaSaldo = somaSaldo - investimento
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaLuz = float(input('valor da conta da luz: \t\t\t\t\t\t\t\tR$ '))
somaSaldo = somaSaldo - contaLuz
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaAgua = float(input('Valor da conta de agua: \t\t\t\t\t\t\tR$ '))
somaSaldo = somaSaldo - contaAgua
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaMercado = float(input('Valor total gasto no mercado: \t\t\t\t\t\tR$ '))
somaSaldo = somaSaldo - contaMercado
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaPostoCombustivel = float(input('Valor gasto com gasolina: \t\t\t\t\t\t\tR$ '))
somaSaldo = somaSaldo - contaPostoCombustivel
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))
contaPadaria = float(input('Valor gasto na padaria: \t\t\t\t\t\t\tR$ '))
somaSaldo = somaSaldo - contaPadaria
print('\t\t\t\t\t\t\t\t\t\t\t\t\tSaldo: R$ {}'.format(somaSaldo))


saldo = somaSaldo

print('\nO saldo em seu bolso é : R$ {:.2f} , disponivel para passar o mes.'.format(saldo))

print('\n\n===============Primeiro programa de contas do jonathan============')

