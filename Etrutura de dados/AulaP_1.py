# Exercício 1                     complexidade     T(n) = n/2 = O(n)
"""def Exercicio1 (dados):
    for i in range(0, len(dados) /2, 1):
        dados[i] = i * 2"""


# Exercício 2                        complexidade T(n) = n+n = O(n)
"""def Exercicio2 (dados):
    for i in range(0, len(dados), 1):
        dados[i] = i + 1
    for i in range(0, len(dados), 1):
        dados[i] = i -1"""


# Exercicio 3                       complexidade  T(n) = n*n = O(n**)   PA constante
"""def Exercicio3 (dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            dados[i] = dados[j] + 1"""


# Exercício 4                       complexidade (n**)   PA não constante
"""def Exercicio4 (dados):
    for i in range(0, len(dados), 1):
        for j in range(i, len(dados), 1):
            dados[i] = dados[j] + 1"""


# Exercício 5                       complexidade T(n) = 9000000*n*n =O(n**) """
"""def Exercicio5 (dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            for k in range(0, 9000000, 1):
                dados[i] = dados[j] + 1"""


# Exercício 6                   complexidade x** <= n  x >= *n T(n) = *n = O(*n)
"""def Exercicio6 (dados):
    for i in range(1, i * i, 1):
        print(i)"""


# Exercício 7               complexidade T(n) = log2n = O(logn)
"""def Exercicio7 (dados):                      
    if (n == 0):
        return
    Exercicio7(n/2)
    print(n)"""

# Exercício 8                       complexidade T(A,B) = O (B*logB) + A * O(logB) = O ((A+B).logB)
"""def Exercicio8  (dadosA = [], dadosB = []):
    sort(dadosB)
    for i in range(0, len(dadosA), 1)
        if (busca(dadosB, i ) >= 0)
            return i"""
