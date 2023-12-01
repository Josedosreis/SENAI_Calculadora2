# Interface grafica da calculadora

from calc2 import soma
from calc2 import sub
from calc2 import mult
from calc2 import div

# Apresentaçao !
print('\n\t\t\t -- Calculadora 2 --\n')

print('\n\t -- Soma --\n')

# Entrada !
num1 = int(input('Informe n1: '))
num2 = int(input('Informe n2: '))

# Processamento !
total_soma = soma(num1, num2)

# Saída !
print(f'{num1} + {num2} = {total_soma}')


# Próxima Operação !
print('\n\t -- Subtração --\n')

# Entrada !
num3 = int(input('Informe n3: '))
num4 = int(input('Informe n4: '))

# Processamento !
total_sub = sub(num3, num4)

# Saída !
print(f'{num3} - {num4} = {total_sub}')

# Próxima Operação !
print('\n\t -- Multiplicação --\n')

# Entrada !
num5 = int(input('Informe n5: '))
num6 = int(input('Informe n6: '))

# Processamento !
total_mult = mult(num5, num6)

# Saída !
print(f'{num5} * {num6} = {total_mult}')

# Próxima Operação !
print('\n\t -- Divisão --\n')

# Entrada !
num7 = int(input('Informe n7: '))
num8 = int(input('Informe n8: '))

# Processamento !
total_div = div(num7, num8)

# Saída !
print(f'{num7} / {num8} = {total_div}')

print('========================================================================')
