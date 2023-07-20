#nome = input('Qual o seu nome: ')
#print(f'O seu nome é {nome=}') #para ver o valor que entrou na variavel coloque um = dps da variável no f(string) EX: {nome=}
#print(f'O seu nome é {nome}') 

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ') 

'''é melhor fazer o input sem definir o tipo de dado que está entrand
pois assim se pode fazer a checagem do que o usuário digitou antes de fazer
qualquer manipulação no código.'''


int_n1 = int(numero_1) 
int_n2 = int(numero_2)

print(f'A soma dos números é: {int_n1 + int_n2} ')
