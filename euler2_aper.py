'''
    Método de Euler aperfeiçoado
    Solução de PVI de ordem 2
    Saída em documento excel
'''
def method():
    ﻿import numpy as np
    import matplotlib.pyplot as plt
    from mpmath import *
    from sympy import *
    from sympy import var
    from sympy import sympify
    from sympy import lambdify
    from astropy.table import Table, Column
    from xlwt import Workbook

    N = 'Exercício 11.b'

    x, y, z = symbols('x, y, z')
    x = var('x')
    y = var('y')
    z = var('z')
    print('Equação diferencial y´´ = f(x, y, z = y´):')
    dy = sympify(input('y´´ = '))
    Dy = lambdify((x, y, z), dy)
    print('\n')
    print('Intervalo [a, b]: ')
    a = float(input('a: '))
    b = float(input('b: '))
    e = float(input('Espaçamento: '))
    print('\n')
    print('Valores iniciais y(x0) = y0 e z(x0) = z0: ')
    Xo = float(input('x0: '))
    Yo = float(input('y0: '))
    Zo = float(input('z0: '))

    h = ((b-a)/e)
    X = np.linspace(a, b, h+1)
    Y = np.array([Yo])
    Z = np.array([Zo])

    for i in X[:int(h)]:
        f = 2*Zo + e*(Dy(i, Yo, Zo))
        g = Dy(i, Yo, Zo) + Dy(i + e, Yo + e*Zo, Zo + e*Dy(i, Yo, Zo))
        Yk = Yo + (e/2)*(f)
        Zk = Zo + (e/2)*(g)

        Y = np.append(Y, [Yk])
        Yo = Yk
        Z = np.append(Z, [Zk])
        Zo = Zk

    wb = Workbook()
    sheet1 = wb.add_sheet('Dados de iteração')

    sheet1.write(1, 1, 'k')
    sheet1.write(1, 2, 't')
    sheet1.write(1, 3, 'y(t)')
    sheet1.write(1, 4, 'z(t)')

    for i in range(int(h)+1):
            sheet1.write(i + 1, 1, (i))
            sheet1.write(i + 1, 2, X[i])
            sheet1.write(i + 1, 3, Y[i])
            sheet1.write(i + 1, 4, Z[i])

    sheet1.write(int(h) + 2, 1, int(h)+1)
    sheet1.write(int(h) + 2, 2, X[int(h)+1])
    sheet1.write(int(h) + 2, 3, Y[int(h)+1])
    sheet1.write(int(h) + 2, 4, Z[int(h)+1])

    wb.save(f'{N}.xls')

    print('Um arquivo .xls foi gerado com alguns dos dados de iteração.')

    A = np.linspace(a, b, 200)

    plt.subplot(211)
    plt.plot(X, Y, 'r.', label='Posição angular', markersize=4)
    plt.ylabel(r'$\theta(t)$ (rad)')
    plt.xlabel('t (s)')
    plt.legend(loc='best')
    plt.grid(True)

    plt.subplot(212)
    plt.plot(X, Z, 'b.', label='Velocidade angular', markersize=4)
    plt.xlabel('t (s)')
    plt.ylabel(r'$\theta\prime$(t) (rad)')
    plt.legend(loc='best')
    plt.grid(True)
    '''
    plt.plot(Y, Z, 'g.-', markersize=5, linewidth=1)
    plt.xlabel(r'$\theta(t)$ (rad)')
    plt.ylabel(r'$\theta\prime$(t) (rad)')
    plt.grid(True)
    '''
    plt.subplots_adjust(hspace=0.3)

    plt.suptitle(N, fontsize=14)
    plt.show()
