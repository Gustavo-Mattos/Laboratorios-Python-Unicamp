###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome: Gustavo Vieira de Mattos
# RA: 250369
###################################################

def str_panquecas(lista):
  return(" ".join(map(str, lista)))

inversao = []
inversao1 = []
inversao2 = []
controle = []
sequencia = [int(i) for i in input().split()]
inversao2.extend(sequencia)
inversao.extend(sequencia)
x = []
y = []
x.extend(sequencia)
numeros_em_ordem = []
numeros_em_ordem.extend(sequencia)
numeros_em_ordem.sort()
if sequencia == numeros_em_ordem:
    print('Panquecas ja ordenadas')

while sequencia != numeros_em_ordem:
    if sequencia == list(reversed(numeros_em_ordem)):
        print(f'Posicionando a panqueca {max(sequencia)}')
        print('Segunda inversao:', str_panquecas(numeros_em_ordem))
        break
    while True:
        print(f'Posicionando a panqueca {max(x)}')
        pos_max = inversao.index(max(x))
        for i in range(pos_max + 1):
            controle.append(sequencia[i])
        for i in range(pos_max + 1, len(sequencia)):
            y.append(sequencia[i])
        controle = list(reversed(controle))
        inversao1.extend(controle)
        inversao1.extend(y)
        inversao2 = list(reversed(inversao1))
        print('Primeira inversao:', str_panquecas(inversao1))
        print('Segunda inversao:', str_panquecas(inversao2))
        if inversao2 == numeros_em_ordem:
            break
        x.remove(max(x))
        inversao1.clear()
        inversao.clear()
        inversao.extend(inversao2)
        inversao2.clear()
    break
