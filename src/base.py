"""
Módulo teste para a revisão do GitHub
"""
import random

# Classes


class Elfa:
    """
    Docstring da classe 'Elfa', a esposa do Lucas deus da guerra.
    """

    def __init__(self):
        """
        Método inicializador da classe Elfa.
        """
        self.nome = "Elfa"

    def qualidades(self):

        v = 10

        """
        Método que mostra as qualidades da Elfa.
        """
        return "Calma, Carinhosa e muito doce e bonita."


class Astride:
    """
    Docstring for Astride
    """

    def __init__(self):
        self.nome = "Astride Hofferson"

    def qualidades(self):
        """
        Docstring for qualidades

        :param self: Description
        """
        return "Muito linda e gostosa!"

    def caracteristicas(self):
        return "Muito inteligente, e carinhosa tambem!"


# Função Main


def main():
    a = Astride()
    print(a.caracteristicas())


if __name__ == "__main__":
    main()
