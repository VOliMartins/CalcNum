'''
    Método da Bissecção
    Raiz de função em um intervalo determinado
    Saída no cmd
'''
def method():
    import numpy as np
    import matplotlib.pyplot as plt
    from astropy.table import Table, Column

    table = Table(names=('k', 'a', 'b', '(a-b)', 't', 'f(t)'), dtype=('i4', 'f4', 'f4', 'f4', 'f4', 'f4'))

    #a = 2
    a = 3.68
    #b = 4
    b = 3.73
    t = 0
    e = 0.00000000001
    k = 1

    x = np.arange(a, b, 0.00001)

    #Função a ser analisada
    def f(z):
        #return np.sin(z) - np.log10(z)
        return z - 5 + np.log(z)

    while abs(a - b) >= e:
        t = (a + b) / 2
    #Garante a existência da raiz
        if f(a)*f(t) < 0:
            b = t
        elif f(a)*f(t) > 0:
            a = t
        else:
            break

        k += 1
        table.add_row((k, a, b, (a-b), t, f(t)))

    #Print dos dados da raiz
    #print(f'{k:2.0f} {a:11.10f} {b:11.10f} {(a-b):11.10f} {t:11.10f} {f(t):11.10f}')

    print(table)

    #Plot da função f com a raiz

    F = str('x - 5 + log(x)')

    plt.plot(x, f(x), 'b', t, f(t), 'ro')
    plt.title(f'Zero da função {F}', {'color': 'b', 'fontsize': 16})
    plt.xlabel('x', {'color': 'k', 'fontsize': 12})
    plt.ylabel('f(x)', {'color': 'k', 'fontsize': 12})
    plt.text(t, f(t), f'Raiz \n ({t:.3f},0)',
             {'color': 'r', 'fontsize': 12},
             horizontalalignment='left',
             verticalalignment='bottom',
             multialignment='center'
             )
    plt.grid(True)
    plt.show()
