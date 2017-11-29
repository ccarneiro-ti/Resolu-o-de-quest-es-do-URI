'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Entrada

O arquivo de entrada contém três valores inteiros.

Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
'''
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
MaiorAB = ((a+b+abs(a-b))/2)
MaiorABC = ((MaiorAB+c+abs(MaiorAB-c))/2)
print("%0.f"%MaiorABC,"eh o maior")