'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada

O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída

A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
'''

n_peca1,quant1,v_peca1 = input().split()
n_peca2,quant2,v_peca2 = input().split()
n_peca1 = int(n_peca1)
quant1 = int(quant1)
v_peca1 = float(v_peca1)
n_peca2 = int(n_peca2)
quant2 = int(quant2)
v_peca2 = float(v_peca2)

total = ((quant1 * v_peca1) + (quant2 * v_peca2))

print("VALOR A PAGAR: R$ %.2f"%total)