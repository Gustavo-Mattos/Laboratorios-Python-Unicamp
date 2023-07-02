###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome: Gustavo Vieira de Mattos
# RA: 250369
###################################################

# Inicialização das variáveis
w = 0
f = 0
e = 0
a = 0

# Leitura da sequência de treinamento
while True:
    Z = input()
    if Z != 'X':
        p = int(input())
        if Z == 'W':
            w = w + p
            f = f - p/2
            if f < 0:
                f = 0
        if Z == 'F':
            w = w - p/2
            f = f + p
            if w < 0:
                w = 0
        if Z == 'E':
            e = e + p
            a = a - p/2
            if a < 0:
                a = 0
        if Z == 'A':
            a = a + p
            e = e - p/2
            if e < 0:
                e = 0
    if Z == 'X':
        break

# Impressão das informações de saída

print("Pontuacao Final")
print("Agua: {:.1f}".format(w))
print("Terra: {:.1f}".format(e))
print("Fogo: {:.1f}".format(f))
print("Ar: {:.1f}".format(a))

lista = [w, f, e, a]
if 0 in lista:
    print("Realize mais treinamentos.")
else:
    print("Treinamento realizado com sucesso.")
