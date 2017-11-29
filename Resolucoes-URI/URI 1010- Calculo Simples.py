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