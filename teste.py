#1)

n = int(input('Insira um valor para saber se o mesmo esta presente na sequencia Fibonacci: '))

a = 0
b = 1

valoresSequencia = []

while(a <= n or b <= n):

    valoresSequencia.append(a)
    valoresSequencia.append(b)

    a = a + b
    b = a + b


if n in valoresSequencia:
    print(f'o numero {n} esta presente na sequencia Fibonacci {valoresSequencia}')
else:
    print(f'o numero {n} não esta presente na sequencia Fibonacci {valoresSequencia}')

#-------------------------------------------------------------------------------------------------------------------


#2)

recebeTexto = input('Insira uma frase para descobrir quantas vezes a letra "a" aparece: ')
str(recebeTexto)

converteEmMinuscula = recebeTexto.lower()

contador = converteEmMinuscula.count('a')

if(contador != 0):
    print(f'a letra "a" aparece: {contador} vezes')
else:
    print(f'a letra "a" aparece: {contador} vezes')

#-------------------------------------------------------------------------------------------------------------------


#3)

INDICE = 12
SOMA = 0
K = 1
while(K < INDICE):
    K += 1
    print('K', K)
    SOMA = SOMA + K
    print('SOMA', SOMA)

print(f'O resultado da soma eh: {SOMA}')

#-------------------------------------------------------------------------------------------------------------------


#4)

# a) 1, 3, 5, 7, ___ 9
# b) 2, 4, 8, 16, 32, 64, ____ 128
# c) 0, 1, 4, 9, 16, 25, 36, ____ 49
# d) 4, 16, 36, 64, ____ 100
# e) 1, 1, 2, 3, 5, 8, ____ 13
# f) 2, 10, 12, 16, 17, 18, 19, ____ 20


#5)

# Contando que eu possa encostar nas lâmpadas, eu ligaria o INTERRUPTOR1 e o deixaria ligado por uns minutos (o suficiente para que a lampâda
# ficasse quente), após esse tempo eu desligaria o INTERRUPTOR1 e ligaria o INTERRUPTOR2, e iria na SALA1, verificaria se a mesma esta com
# a lampâda acessa, caso estivesse então o INTERRUPTOR2 a controla, senão, verificaria se a lampâda esta quente, caso esteja então o INTERRUPTOR1
# a controla, caso nenhuma dessas opções ocorra, então o INTERRUPTOR3 seria responsável pela SALA1.

# Levando em consideração que o INTERRUPTOR3 controla a SALA1, então eu voltaria para os interruptores e ligaria o INTERRUPTOR1 e visitaria
# a SALA3, caso a lampâda estivesse acesa, então o INTERRUPTOR1 controla a SALA3, e o INTERRUPTOR2 controla a SALA2 e o INTERRUPTOR3 controla a SALA1.

# Caso a lampâda da SALA3 não estivesse acesa, então: o INTERRUPTOR1 controla a SALA2, INTERRUPTOR2 controla a SALA3 e o INTERRUPTOR3 controla a SALA1.