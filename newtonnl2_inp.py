'''
    Newton para sistemas não lineares
    Diversos chutes iniciais
    Saída por documento excel
'''
def method():
    import numpy as np
    from mpmath import *
    from sympy import *
    from sympy import var
    from sympy import sympify
    from sympy import lambdify
    from xlwt import Workbook

    x1, x2 = symbols('x1, x2')

    wb = Workbook()

    def newton(X, Y, E, A, B):

        B.write(0, (A*7)+1, f'({X};{Y})')
        B.write(1, (A*7)+1, 'k')
        B.write(1, (A*7)+2, 'S')
        B.write(1, (A*7)+3, 'S')
        B.write(1, (A*7)+4, 'Xk')
        B.write(1, (A*7)+5, 'Yk')
        B.write(1, (A*7)+6, 'f(Xk)')
        B.write(1, (A*7)+7, 'f(Yk)')

        k = 0
        F = np.array([[(-1)*F1(X, Y)], [(-1)*F2(X, Y)]])

        while np.absolute(F).max() > E:

            J = np.array([[J11(X, Y), J12(X, Y)], [J21(X, Y), J22(X, Y)]])
            S = np.linalg.solve(J, F)

            X = X + S[0][0]
            Y = Y + S[1][0]

            F = np.array([[(-1)*F1(X, Y)], [(-1)*F2(X, Y)]])

            k = k + 1

            B.write(k+1, (A*7)+1, k)
            B.write(k+1, (A*7)+2, S[0][0])
            B.write(k+1, (A*7)+3, S[1][0])
            B.write(k+1, (A*7)+4, X)
            B.write(k+1, (A*7)+5, Y)
            B.write(k+1, (A*7)+6, F[0][0])
            B.write(k+1, (A*7)+7, F[1][0])

            print(f'----------\n {k-1} \n S:{S} \n x{k}: {X:.3f} {Y:.3f} \n F(x{k}):{(-1)*F} \n\n')


    x1 = var('x1')
    x2 = var('x2')

    e = float(input('Teste de parada: '))

    f1 = sympify(input('f1(x1, x2): '))
    F1 = lambdify((x1, x2), f1)
    f2 = sympify(input('f2(x1, x2): '))
    F2 = lambdify((x1, x2), f2)

    j11 = diff(f1, x1)
    J11 = lambdify((x1, x2), j11)
    j12 = diff(f1, x2)
    J12 = lambdify((x1, x2), j12)
    j21 = diff(f2, x1)
    J21 = lambdify((x1, x2), j21)
    j22 = diff(f2, x2)
    J22 = lambdify((x1, x2), j22)

    print('\n')
    a = 0
    b = 0
    for x in range(50, 550, 50):
        b = b+1
        B = str(b)
        B = wb.add_sheet(f'Dados de iteração{b}')
        for y in range(50, 550, 50):
            s = newton(x, y, e, a, B)
            a = a + 1
        a = 0

    wb.save('Equilíbrio entre as espécies.xls')
