###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova York
# Nome: Gustavo Vieira de Mattos
# RA: 250369
###################################################
matriz = []
valor = ''
while not valor.isnumeric():
    valor = input()
    linhas = list(valor.replace(" ", ""))
    matriz.append(linhas)
num_linhas = len(matriz) - 1
num_colunas = len(matriz[0])
num_elementos = num_colunas * num_linhas
valor = int(valor)
for i in range(valor):
    j = 0
    a = input()
    b = []
    b.append(a.split())
    l = int(b[0][0])
    c = int(b[0][1])
    while True:
        if matriz[l][c] == 'N':
            if l == 0:
                print("Fuga pelo norte.")
                break
            l = l - 1
        if matriz[l][c] == 'S':
            if l == num_linhas - 1:
                print("Fuga pelo sul.")
                break
            l = l + 1
        if matriz[l][c] == 'O':
            if c == 0:
                print("Fuga pelo oeste.")
                break
            c = c - 1
        if matriz[l][c] == 'L':
            if c == num_colunas - 1:
                print("Fuga pelo leste.")
                break
            c = c + 1
        j = j + 1
        if j == num_elementos:
              print("Resgate aereo solicitado.")
              break
