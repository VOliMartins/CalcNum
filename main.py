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

print('*************** C�lculo Num�rico ***************')
print('\n')

while True:
	print('Tipos de m�todos dispon�veis: ')
	print('''	(1)Zero reais de fun��es
		 	(2)Sistemas lineares
			(3)Sistemas n�o lineares
			(4)Equa��es diferenciais
			(5)M�nimos quadrados
			(6)Interpola��o
						''')
	t = int(input('Escolha o tipo desejado (c�digo): ')
	print('***********************************************')

	if t == 1:
		print('''Zero reais de fun��es
			 	(1)Bisse��o
				(2)Newton
				(3)Secante
						''')
		m = int(input('Escolha o m�todo desejado (c�digo): ')
		break
	elif t == 2:
		print('''Sistemas lineares
			 	(1)Elimina��o de Gauss
				(2)Fatora��o LU
				(3)Gauss-Seidel
				(4)Gauss-Jacobi
						''')
		m = int(input('Escolha o m�todo desejado (c�digo): ')
		break
	elif t == 3:
		print('************* Sistemas n�o lineares ************')
		break
	elif t == 4:
		print('''Equa��es diferenciais
			 	(1)M�todo de Euler e variantes
				(2)Range-Kutta e variantes
				(3)PVC
						''')
		m = int(input('Escolha o m�todo desejado (c�digo): ')
		break
	elif t == 5:
		print('*************** M�nimos quadrados **************')
		break
	elif t == 6:
		print('''Interpola��o
			 	(1)Polinomial
				(2)Splines
						''')
		m = int(input('Escolha o m�todo desejado (c�digo): ')
		break
	else:
		print('Sua escolha n�o � valida')
		print('\n')

print('************** Programa finalizado *************')

