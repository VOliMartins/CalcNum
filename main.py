import numpy as np
import bissecao as bs
import newton as nw
import secante as sc
import eligauss as eg
import fatlu as lu
import gaussseidel as gs
import gaussjacobi as gj
import newtonnl as nl
import euler as eu
import rangekutta as rk
import valorescontorno as pvc
import minimosquadrados as mq
import interpoli as ip
import intersplines as is

print('*************** Cálculo Numérico ***************')
print('\n')

while True:
	print('Tipos de métodos disponíveis: ')
	print('''(1)Zero reais de funções
		(2)Sistemas lineares
		(3)Sistemas não lineares
		(4)Equações diferenciais
		(5)Mínimos quadrados
		(6)Interpolação
						''')
	t = int(input('Escolha o tipo desejado (código): '))
	print('***********************************************')

	if t == 1:
		print('''Zero reais de funções
			(1)Bisseção
			(2)Newton
			(3)Secante
						''')
		m = int(input('Escolha o método desejado (código): '))
		break
	elif t == 2:
		print('''Sistemas lineares
			(1)Eliminação de Gauss
			(2)Fatoração LU
			(3)Gauss-Seidel
			(4)Gauss-Jacobi
						''')
		m = int(input('Escolha o método desejado (código): '))
		break
	elif t == 3:
		print('************* Sistemas não lineares ************')
		break
	elif t == 4:
		print('''Equações diferenciais
			(1)Método de Euler e variantes
			(2)Range-Kutta e variantes
			(3)PVC
						''')
		m = int(input('Escolha o método desejado (código): '))
		break
	elif t == 5:
		print('*************** Mínimos quadrados **************')
		break
	elif t == 6:
		print('''Interpolação
			(1)Polinomial
			(2)Splines
						''')
		m = int(input('Escolha o método desejado (código): '))
		break
	else:
		print('Sua escolha não é valida')
		print('\n')

print('************** Programa finalizado *************')

