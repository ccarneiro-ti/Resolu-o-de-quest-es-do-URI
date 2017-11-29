'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada

O arquivo de entrada contém um valor inteiro N.

Saída

Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''
N = int(input())

N_horas = N/3600
N = N%3600
N_min = N/60
N = N%60
N_seg = N

print("%d:%d:%d"%(N_horas,N_min,N_seg))