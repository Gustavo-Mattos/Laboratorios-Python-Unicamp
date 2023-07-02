###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome: Gustavo Vieira de Mattos
# RA: 250369
###################################################

# Leitura de dados
a = 0
sequencia = [int(i) for i in input().split()]
numeros_em_ordem = []

numeros_em_ordem.extend(sequencia)
numeros_em_ordem.sort()

while True:
    if sequencia != numeros_em_ordem:
        a = a + 1
        sequencia.append(sequencia[0])
        del (sequencia[0])
        if a == 10:
            break
    else:
        print("Klift, Kloft, Still, a porta se abriu")
        break
if sequencia != numeros_em_ordem:
    print("Senha incorreta")
