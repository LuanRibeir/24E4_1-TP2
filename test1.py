# Dado o código abaixo, identifique a complexidade de tempo de cada função
# usando a notação Big O e explique brevemente sua resposta.
# Qual é a complexidade de tempo de cada função (funcao1, funcao2, e funcao3)
# em termos de Big O? Justifique brevemente cada resposta.

# Função 1
def funcao1(n):
    for i in range(n):
        print(i)

# R: 0(n)

# Função 2
def funcao2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# R: 0(N²)

# Função 3
def funcao3(n):
    if n <= 1:
        return n
    return funcao3(n - 1) + funcao3(n - 2)

# R: O(2^n)