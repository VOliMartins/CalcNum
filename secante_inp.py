'''
    Método da Secante
    Raiz de função em um intervalo determinado
    Saída no cmd
'''
def method():
    from astropy.table import Table, Column
    import math
    from sympy import *
    import matplotlib.pyplot as plt
    import numpy as np

    X = np.linspace(-1, 1, 100)

    t = Table(names=('k', 'Jk-1', 'Jk', 'Jk+1', 'f(Jk+1)'), dtype=('i4', 'f4', 'f4', 'f4', 'f4'))

    x, y, z = symbols('x y z')
    init_printing(use_unicode=True)


    def f(x):
        return 2134.91*x**2 + 3145.17*x - 114.39


    def S(x, y):
        return (x*f(y)-y*f(x))/(f(y)-f(x))


    plt.plot(X, f(X), 'b')
    plt.plot(X, X, 'r')

    Xo = 0.01
    X1 = 0.015
    X2 = 0
    a = 0
    k = 0

    X2 = S(Xo, X1)
    #plt.plot(X, r(X, Xo, X1), 'r')
    plt.plot(X1, f(X1), 'ko')

    while math.fabs(f(X2)) > 10 ** (-12) and math.fabs(X1 - X2) > 10 ** (-12):
        a = X2
        Xo = X1
        X1 = a
        X2 = S(Xo, X1)
        k = k + 1
        t.add_row((k, Xo, X1, X2, f(X2)))
        #plt.plot(X, r(X, Xo, X1), 'r')
        plt.plot(X1, f(X1), 'ko')

    print(t)
    print(f'X* = {X2} -- f(X*) = {f(X2)}')

    ax = plt.gca()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Método da Secante', {'color': 'b', 'fontsize': 16})
    '''
    plt.text(Xo, psi(Xo), f'Raiz \n ({X1:.3f},0)',
             {'color': 'r', 'fontsize': 12},
             horizontalalignment='left',
             verticalalignment='bottom',
             multialignment='center'
             )
    '''
    plt.text(0, 8, f'f(x) = (x-2)^2',
             {'color': 'b', 'fontsize': 12},
             horizontalalignment='left',
             verticalalignment='bottom',
             multialignment='center'
             )
    '''
    plt.text(4, 9.4, f'fi(x) = x/2',
             {'color': 'b', 'fontsize': 12},
             horizontalalignment='left',
             verticalalignment='bottom',
             multialignment='center'
             )
    '''
    plt.grid(True)
    plt.show()
