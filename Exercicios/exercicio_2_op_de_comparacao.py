n_1 = input('informe um valor: ')
n_2 = input('informe outro valor: ')

if n_1 > n_2:
	print(f'O primeiro valor {n_1=} é maior que o segundo valor {n_2=}')
elif n_2 > n_1:
	print(f'O segundo valor {n_2=} é maior que o primeiro valor {n_1=}')
else:
	print('Os valores são iguais')