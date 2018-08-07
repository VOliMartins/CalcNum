'''
    Método da Newton
    Raiz de função em um intervalo determinado
    Saída no cmd
'''
def method():
    from astropy.table import Table, Column
    from sympy import *
    import matplotlib.pyplot as plt
    import numpy as np
    import math

    X = np.linspace(0, 10, 100)

    t = Table(names=('k', 'Xk', 'fi(Xk)', 'f(Xk)'), dtype=('i4', 'f4', 'f4', 'f4'))

    x, y, z = symbols('x y z')
    init_printing(use_unicode=True)


    def f(x):
        return 3259.56*x**3 + 8654.03*x**2 + 6404.73*x - 114.39


    def fi(x):
        return x - f(x)/(9778.68*x**2 + 17308.06*x + 6404.73)


    plt.plot(X, fi(X), 'b')
    plt.plot(X, X, 'r')


    Xo = 1
    k = 0
    plt.plot((Xo, Xo), (-3, fi(Xo)), 'k-.')


    while math.fabs(f(Xo)) > 10**(-15) and math.fabs(Xo - fi(Xo)) > 10**(-15):
        plt.plot((Xo, fi(Xo)), (fi(Xo), fi(Xo)), 'k-.')
        Xo = fi(Xo)
        k = k + 1
        t.add_row((k, Xo, fi(Xo), f(Xo)))
        plt.plot((Xo, Xo), (Xo, fi(Xo)), 'k-.')

    print(t)
    print(f'\n x = {Xo}, f(x) = {f(Xo)}')

    ax = plt.gca()
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 6)
    plt.plot(Xo, fi(Xo), 'go')
    plt.xlabel('')
    plt.ylabel('')
    plt.title('Método de Newton', {'color': 'b', 'fontsize': 16})
    plt.text(Xo-0.5, fi(Xo)+0.25, f'Raiz \n ({Xo:.3f},0)',
             {'color': 'r', 'fontsize': 12},
             horizontalalignment='left',
             verticalalignment='bottom',
             multialignment='center'
             )
    plt.text(1.8, 5.5, f'f(x) = x^3 + 2x^2 + 10x - 20',
             {'color': 'k', 'fontsize': 12},
             horizontalalignment='left',
             verticalalignment='bottom',
             multialignment='center'
             )
    plt.text(1.8, 5, f'fi(x) = 3x^2 + 4x + 10',
             {'color': 'k', 'fontsize': 12},
             horizontalalignment='left',
             verticalalignment='bottom',
             multialignment='center'
             )
    plt.grid(False)
    plt.show()
