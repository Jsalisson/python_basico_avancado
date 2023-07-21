'''
Operadores Logicos
and (e) or (ou) not(não)
and - Todas as condições precisam ser verdadeiras.


Também existe o tipo None que é usado para representar um não valor 
'''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'


if (entrada == 'E' or entrada == 'e')and senha_digitada == senha_permitida:
	print('Entrar')
else:
	print('Sair')


'''Se qualquer valor for considerado falso
a expressão inteira será avaliada naquele valor
são considerados falsy (que vc ja viu) 0 0.0 '' False'''

'''print(True and True and True)
print(bool(True and 0 and True))'''

''' 
or - Qualquer condição verdadeira avalia toda a expressão como verdadeira,
a expressçao inteira será avaliada naquele valor.
'''
