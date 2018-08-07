'''
    Método de Euler aperfeiçoado
    Solução de PVI de ordem 1
    Saída no cmd
'''
def method() :
    import numpy as np
    import matplotlib.pyplot as plt
    from mpmath import *
    from sympy import *
    from sympy import var
    from sympy import sympify
    from sympy import lambdify

    x, y = symbols('x, y')
    x = var('x')
    y = var('y')
    print('Equação diferencial y´ = f(x, y):')
    dy = sympify(input('y´ = '))
    Dy = lambdify((x, y), dy)
    print('\n')
    print('Intervalo [a, b]: ')
    a = float(input('a: '))
    b = float(input('b: '))
    e = float(input('Espaçamento: '))
    print('\n')
    print('Valor inicial y(xo) = yo: ')
    Xo = float(input('x0: '))
    Yo = float(input('y0: '))

    h = ((b-a)/e)
    X = np.linspace(a, b, h+1)
    Y = np.array([Yo])

    for i in X[:int(h)]:
        f = (Dy(i, Yo) + Dy((i+e), (Yo + e*Dy(i, Yo))))/2
        Yk = Yo + e*(f)
        Y = np.append(Y, [Yk])
        Yo = Yk

    print(X)
    print(Y)

    A = np.linspace(a, b, 200)

    fig, ax =plt.subplots()

    line1, = ax.plot(A, 2/(-(A**2) + 2), label='Solução analítica')
    line2, = ax.plot(X, Y, 'r.', label='Método de Euler aperfeiçoado')

    ax.legend(loc='best')

    plt.grid(True)
    plt.show()
