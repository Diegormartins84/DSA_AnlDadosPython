# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print('\nSelecione o número da operação desejada:  \n1-Soma \n2-Subtração \n3-Multiplicação \n4-Divisão ')

operacao = int(input('\nDigite sua opção (1/2/3/4): '))

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if operacao == 1:
    resultado = num1 + num2
    print(num1, '+', num2, '=', resultado)
elif operacao == 2:
    resultado = num1 - num2
    print(num1, '-', num2, '=', resultado)
elif operacao == 3:
    resultado = num1 * num2
    print(num1, '*', num2, '=', resultado)
elif operacao == 4:
    resultado = num1 // num2
    print(num1, '/', num2, '=', resultado)
else:
    print('Operação inválida!')