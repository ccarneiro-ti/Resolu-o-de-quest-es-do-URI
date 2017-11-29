'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada

O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída

Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''
N = int(input())
print(N)
cem = N/100
resto1 = N%100
print("%d nota(s) de R$ 100,00"% cem)
cinquenta = resto1/50
resto2 = resto1%50
print("%d nota(s) de R$ 50,00"% cinquenta)
vinte = resto2/20
resto3 = resto2%20
print("%d nota(s) de R$ 20,00"% vinte)
dez = resto3/10
resto4 = resto3%10
print("%d nota(s) de R$ 10,00"% dez)
cinco = resto4/5
resto5 = resto4%5
print("%d nota(s) de R$ 5,00"% cinco)
dois = resto5/2
resto6 = resto5%2
print("%d nota(s) de R$ 2,00"% dois)
um = resto6/1
resto7 = resto6%1
print("%d nota(s) de R$ 1,00"% um)