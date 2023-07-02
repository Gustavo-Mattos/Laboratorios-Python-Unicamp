# Impressão do resumo final
###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 17 - Vacinação AstraZeneca
# Nome: Gustavo Vieira de Mattos
# RA: 250369
###################################################

N = int(input())
D1 = []
D2 = [0, 0, 0]
X = []
LISTA = []

def encurtar(m, n, o):
    X.append(m)
    D1.append(n)
    D2.append(o)

for i in range(N):
    LISTA.append(int(input()))
for i in range(N):
    if N < 6:
        if i < 3:
            D1.append(LISTA[i])
            X.append(0)
        elif D1[i - 3] > 0:
            z = LISTA[i] - D1[i - 3]
            encurtar(0, z, D1[i - 3])
    elif i < 3:
        if LISTA[i + 3] >= LISTA[i]:
            D1.append(LISTA[i])
            X.append(0)
        else:
            D1.append(LISTA[i + 3])
            X.append(LISTA[i] - LISTA[i + 3])
    elif 3 <= i <= (N - 4):
        if D1[i - 3] > 0:
            z = LISTA[i] - D1[i - 3]
            D2.append(D1[i - 3])
            if LISTA[i + 3] >= z:
                D1.append(z)
                X.append(0)
            else:
                D1.append(LISTA[i + 3])
                X.append(z - LISTA[i + 3])
        elif LISTA[i + 3] >= LISTA[i]:
            encurtar(0, LISTA[i], 0)
        else:
            encurtar(LISTA[i] - LISTA[i + 3], LISTA[i + 3], 0)
    elif i > (N - 4):
        z = LISTA[i] - D1[i - 3]
        encurtar(0, z, D1[i - 3])
for i in range(N):
    print(f"Mes {i + 1}:")
    print(f"Vacinados com a primeira dose: {D1[i]}")
    print(f"Vacinados com a segunda dose: {D2[i]}")
    print(f"Vacinas devolvidas: {X[i]}")
TD2 = sum(D2)
TD1 = sum(D1) - TD2
print('Total:')
print(f'Vacinados apenas com a primeira dose: {TD1}')
print(f'Vacinados com as duas doses: {TD2}')
print(f'Vacinas devolvidas: {sum(X)}')
