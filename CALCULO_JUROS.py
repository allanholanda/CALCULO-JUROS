#Exercício 4

C = float(input('Digite o capital inicial: '))
i = float(input('Digite a taxa de juros em porcentagem: '))
i = i / 100
t = int(input('Digite o prazo em meses da aplicação: '))
Ci = C

# Fórmula pro montante total
MT = C * (1 + i) ** t
print('O montante após ',t,' meses é = R$ {}' .format(round(MT,2)))

# Fórmula pra calcular mês a mês
for x in range (1, t + 1):
    Mm = C * (1 + i)
    C = Mm
    print('O montante do mês ',x,' é = R$ {}' .format(round(Mm,2)))

#Ganho com juros no período
J = MT - Ci
print ('O ganho com juros no final dos ',x,' meses é = R$ {}' .format(round(J,2)))

print('Fim do programa')
