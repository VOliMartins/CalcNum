'''
    Método de Euler aperfeiçoado
    Solução de sistema de eq dif
    Duas equações
    Saída em documento excel
'''
def method():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpmath import *
    from sympy import *
    from sympy import var
    from sympy import sympify
    from sympy import lambdify
    from astropy.table import Table, Column
    from xlwt import Workbook

    N = 'Presa-predador'

    t, y, z = symbols('t, y, z')
    t = var('t')
    y = var('y')
    z = var('z')
    print('Sistema de equações diferenciais :')
    df = sympify(input('y´ = '))
    Df = lambdify((t, y, z), df)
    dg = sympify(input('z´ = '))
    Dg = lambdify((t, y, z), dg)
    print('\n')
    print('Intervalo [a, b]: ')
    a = float(input('a: '))
    b = float(input('b: '))
    e = float(input('Espaçamento: '))
    print('\n')
    print('Valores iniciais y(t0) = y0 e z(t0) = z0: ')
    Xo = float(input('t0: '))
    Yo = float(input('y0: '))
    Zo = float(input('z0: '))

    h = ((b-a)/e)
    T = np.linspace(a, b, h+2)
    Y = np.array([Yo])
    Z = np.array([Zo])

    for i in T[:int(h)+1]:
        f = Df(i, Yo, Zo) + Df((i + e), (Yo + e*Df(i, Yo, Zo)), (Zo + e*Dg(i, Yo, Zo)))
        g = Dg(i, Yo, Zo) + Dg((i + e), (Yo + e*Df(i, Yo, Zo)), (Zo + e*Dg(i, Yo, Zo)))
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

    for i in range(int(h/100)+1):
        if i==0:
            sheet1.write(i + 2, 1, 1)
            sheet1.write(i + 2, 2, T[1])
            sheet1.write(i + 2, 3, Y[1])
            sheet1.write(i + 2, 4, Z[1])
        else:
            sheet1.write(i + 2, 1, (i*100))
            sheet1.write(i + 2, 2, T[i*100])
            sheet1.write(i + 2, 3, Y[i*100])
            sheet1.write(i + 2, 4, Z[i*100])

    sheet1.write(int(h/100) + 3, 1, int(h)+1)
    sheet1.write(int(h/100) + 3, 2, T[int(h)+1])
    sheet1.write(int(h/100) + 3, 3, Y[int(h)+1])
    sheet1.write(int(h/100) + 3, 4, Z[int(h)+1])

    wb.save(f'{N}.xls')

    print('Um arquivo .xls foi gerado com alguns dos dados de iteração.')

    A = np.linspace(a, b, 200)

    plt.subplot(211)
    plt.plot(T, Y, 'r.', label='Número de presas', markersize=4)
    plt.ylabel(r'Y(t)')
    plt.xlabel('t (dias)')
    plt.legend(loc='best')
    plt.grid(True)

    plt.subplot(212)
    plt.plot(T, Z, 'b.', label='Número de predadores', markersize=4)
    plt.xlabel('t (dias)')
    plt.ylabel(r'Z(t)')
    plt.legend(loc='best')
    plt.grid(True)
    '''
    plt.plot(Y, Z, 'go-', markersize=5)
    plt.xlabel(r'y(t)')
    plt.ylabel(r'z(t)')
    plt.grid(True)
    '''
    plt.subplots_adjust(hspace=0.3)

    plt.suptitle(N, fontsize=14)
    plt.show()
