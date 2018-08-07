'''
    Newton para sistemas não lineares
    Único chute inicial
    Saída no cmd
'''
def method():
    import numpy as np
    from mpmath import *
    from sympy import *
    from sympy import var
    from sympy import sympify
    from sympy import lambdify

    def newton(X, Y, E):

        k = 0
        F = np.array([[(-1)*F1(X, Y)], [(-1)*F2(X, Y)]])

        while np.absolute(F).max() > E:

            J = np.array([[J11(X, Y), J12(X, Y)], [J21(X, Y), J22(X, Y)]])
            S = np.linalg.solve(J, F)

            X = X + S[0][0]
            Y = Y + S[1][0]

            F = np.array([[(-1)*F1(X, Y)], [(-1)*F2(X, Y)]])

            k = k + 1

            print(f'----------\n {k-1} \n S:{S} \n x{k}: {X:.3f} {Y:.3f} \n F(x{k}):{(-1)*F} \n\n')

    #Declaração das variáveis
    x1 = var('x1')
    x2 = var('x2')
    #Leitura do chute inicial e teste de parada
    x = float(input('X do chute inicial: '))
    y = float(input('Y do chute inicial: '))
    e = float(input('Teste de parada: '))
    #Leitura das equações do sistema
    f1 = sympify(input('f1(x1, x2): '))
    F1 = lambdify((x1, x2), f1)
    f2 = sympify(input('f2(x1, x2): '))
    F2 = lambdify((x1, x2), f2)
    #Derivação para a matriz Jacobiana
    j11 = diff(f1, x1)
    J11 = lambdify((x1, x2), j11)
    j12 = diff(f1, x2)
    J12 = lambdify((x1, x2), j12)
    j21 = diff(f2, x1)
    J21 = lambdify((x1, x2), j21)
    j22 = diff(f2, x2)
    J22 = lambdify((x1, x2), j22)

    print('\n')

    s = newton(x, y, e)

    print(s)
