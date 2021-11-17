class Fatorial:
    def fatorial(self, calculo=1, show=False):
        """
        -> Calcule o fatorial de um numero.
        :param calculo: o sumero a ser calculado
        :param show: (opcional) mostrar ou não a conta
        :return: valor fatorial
        """
        f = 1
        for i in range(calculo, 0, -1):
            if show:
                print(i, end='')
                if i > 1:
                    print(" x ", end='')
                else:
                    print(" = ", end='')
            f *= i
        return f


n = Fatorial()
print(n.fatorial(5, True))
