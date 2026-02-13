"""
Docstring do módulo 'revisao_github'
"""

import base

# String que se refere ao Lucas
print("Ola meu nome é Lucas")

# String que se refere a Astride
print("A Astride é gata!")


def request_handler():
    """
    Docstring da função request_handler
    """
    return "Ola eu sou o request handler"


def main():
    a = base.Astride()
    a.qualidades()


if __name__ == "__main__":
    main()
