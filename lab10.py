###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 19 - Busca em Imagens
# Nome: Gustavo Vieira de Mattos
# RA: 250369
###################################################
def averiguar(x, y):
    for i in range(len(x) - len(y) + 1):
        for j in range(len(x[0]) - len(y[0]) + 1):
            certo = 0
            for k in range(len(y)):
                if x[i + k][j:j+len(y[0])] == y[k]:
                    certo += 1
                    if certo == len(y):
                        return 'Contido'
                else:
                    break
    return 'Nao contido'
# leitura da imagem A
_ = input()  # P2 - linha a ser ignorada

m_A, n_A = [int(x) for x in input().split()]

_ = input()  # 255 - linha a ser ignorada

A = []
for i in range(n_A):
    linha = [int(x) for x in input().split()]
    A.append(linha)

# leitura da imagem B
_ = input()  # P2 - linha a ser ignorada

m_B, n_B = [int(x) for x in input().split()]

_ = input()  # 255 - linha a ser ignorada

B = []

for i in range(n_B):
    linha = [int(x) for x in input().split()]
    B.append(linha)

#HORIZONTAL----------------------------------

flip_horizontal_B = []
for i in range(len(B)):
    a = list(reversed(B[i]))
    flip_horizontal_B.append(a)

#VERTICAL------------------------------------

flip_vertical_B = list(reversed(B))

#90------------------------------------------

rotacao_90_B = [[0 for j in range(len(B))] for i in range(len(B[0]))]
def rodar_90(B):
    rotacao_90_B = [[0 for j in range(len(B))] for i in range(len(B[0]))]
    for linha in range(len(B)):
        for coluna in range(len(B[0])):
            rotacao_90_B[coluna][len(B) - 1 - linha] = B[linha][coluna]
    return rotacao_90_B

#180-----------------------------------------

def rodar_180(matriz):
    return rodar_90(rodar_90(B))

print(f'Original: {averiguar(A, B)}' )
print(f'Flip horizontal: {averiguar(A, flip_horizontal_B)}')
print(f'Flip vertical: {averiguar(A, flip_vertical_B)}')
print(f'Rotacao 90: {averiguar(A, rodar_90(B))}')
print(f'Rotacao 180: {averiguar(A, rodar_90(rodar_90(B)))}')
