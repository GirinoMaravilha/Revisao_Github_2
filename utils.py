"""
Docstring para o módulo 'utils.py'.
"""


# Funções Auxiliares

def cria_matriz(colunas:int,linhas:int) -> list[list[int]]:

    ### Variáveis ###

    #Valor que sera incrementado
    valor = 0

    #Lista da Matriz
    lista_matriz = []

    ### Código ###

    #Vamos calcular a quantidade total de items da matriz
    total_valores = colunas * linhas

    #Vamos realizar a iteração para a criação da matriz
    for linha in range(linhas):
        lista_matriz.append([])

        for _ in range(colunas):
            valor += 1
            lista_matriz[linha].append(valor)
    
    #Retornando a matriz
    return lista_matriz


# Função Main

def main():
    
    matriz = cria_matriz(3,3)
    for linha in matriz:
        print(linha)


if __name__ == "__main__":
    main()


