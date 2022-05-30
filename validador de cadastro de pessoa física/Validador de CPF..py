from math import ceil
import numpy as np

cpf = input("CPF:")
digitos = [int(a) for a in str(cpf)]
mult = [11,10,9,8,7,6,5,4,3,2]
x = ()
y = ()

if len(digitos) == 11:

    prod = np.multiply(digitos[0:9], mult[1:10])
    soma = sum(prod)
    resto = soma % 11

    if resto == 0 or 1:
        x = 0

    if resto >= 2:
        x = 11-resto

    prod = np.multiply(digitos[0:10], mult[0:])
    soma = sum(prod)
    resto = soma % 11

    if resto == 0 or 1:
        y = 0

    if resto >= 2:
        y = 11-resto

    if x == digitos[9] and y == digitos[10]:
        print("\033[0;36;40mCPF válido!\033[m")
    else:
        print("\033[0;31;40mCPF inválido!\033[m")
