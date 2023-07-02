#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 18 - Jogos Olímpicos
# Nome: Gustavo Vieira de Mattos
# RA: 250369
#####################################################

# Leitura da primeira linha

N, O, P, B = [int(x) for x in input().split()]

# Leitura e processamento das provas

pontuacao = {}
esportes_ouro = {}

for i in range(N):
    prova, primeiro, segundo, terceiro = input().split()
    if primeiro not in pontuacao.keys():
        pontuacao[primeiro] = 0
    if segundo not in pontuacao.keys():
        pontuacao[segundo] = 0
    if terceiro not in pontuacao.keys():
        pontuacao[terceiro] = 0
    if primeiro not in esportes_ouro.keys():
        esportes_ouro[primeiro] = []
    pontuacao[primeiro] += O
    pontuacao[segundo] += P
    pontuacao[terceiro] += B
    esportes_ouro[primeiro].append(prova)

a = list(pontuacao.values())
a = a.count(int(pontuacao[max(pontuacao, key=pontuacao.get)]))

paises_maxima = []
ponto = pontuacao[max(pontuacao, key=pontuacao.get)]

for i in range(a):
    paises_maxima.append(max(pontuacao, key=pontuacao.get))
    del pontuacao[max(pontuacao, key=pontuacao.get)]

paises_maxima = sorted(paises_maxima)

for i in range(len(paises_maxima)):
    print(paises_maxima[i], ponto)
    if paises_maxima[i] in esportes_ouro:
        for j in range(len(esportes_ouro[paises_maxima[i]])):
            print(esportes_ouro[paises_maxima[i]][j])
