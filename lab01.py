###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: Gustavo Vieira de Mattos
# RA: 250369
###################################################

# Leitura de dados
t = float(input())
dist_a = int(input())
vel_a = float(input())
t_pit_stop = float(input())
dist_b = int(input())
vel_b = float(input())

# Cálculo do tempo total gasto para realizar o pit stop
vel_a2 = vel_a/3.6
vel_b2 = vel_b/3.6
tt = dist_a/vel_a2 + t_pit_stop + dist_b/vel_b2

print(tt)
print(t)
# Impressão da resposta
if tt < t:
    print("True")
else:
    print("False")
