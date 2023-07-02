######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Vacinação CoronaVac
# Nome: Gustavo Vieira de Mattos
# RA: 250369
######################################################################

N = int(input())
D1 = 0
D2A = 0
D1A = 0
TOTAL = 0
for i in range(N):
    a = int(input())
    TOTAL = TOTAL + a
    if D1A > 0:
        if a < D1A:
            D1A = D1A - a
            D2A = D2A + a
            a = 0
        if a >= D1A:
            a = a - D1A
            D2A = D2A + D1A
            D1A = 0
            if a < D1:
                D1 = D1 - a
                D1A = D1A + D1
                a = 0
            if a > D1:
                a = a - D1
                D1 = a
                a = 0
    elif D1A == 0 and a < D1:
        D1 = D1 - a
        D1A = D1A + D1
        D1 = 0
        a = 0
    elif D1A == 0 and a >= D1:
        a = a - D1
        D1 = a
        a = 0

D1 = D1 + D1A
D2 = int((TOTAL - D1)/2)

print(f"Pessoas completamente imunizadas: {D2}")
print(f"Pessoas imunizadas apenas com uma dose: {D1}")
print(f"Pessoas que tomaram a segunda dose com atraso: {D2A}")
print(f"Pessoas esperando a segunda dose com atraso: {D1A}")
