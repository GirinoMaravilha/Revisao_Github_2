"""
Módulo teste para a revisão do GitHub
"""


# Classes

class Elfa:
    def __init__(self):
        self.nome = "Elfa"
    
    def qualidades(self):
        return "Calma, Carinhosa e muito doce e bonita."


class Astride:
    def __init__(self):
        self.nome = "Astride Hofferson"

    def qualidades(self):
        return "Muito linda e gostosa!"
    
    def caracteristicas(self):
        return "Muito inteligente, e carinhosa tambem!"
    

# Função Main

def main():
    a = Astride()
    print(a.caracteristicas())


if __name__ == "__main__":
    main()