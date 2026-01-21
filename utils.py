"""
Docstring para o módulo 'utils.py'.
"""


# Funções Auxiliares


def retorna_n(string:str) -> int:
    return len(string)


def parser_arquivo(abs_path:str) -> str:

    """
    Módulo para realizar o parsing de caminhos absolutos e retirar o nome do arquivo.

    Args:
        abs_path(str): Caminho absoluto do arquivo.

    Returns:
        str: Nome do arquivo.
    
    Raises:
        ValueError: Exceção levantada quando o caminho absoluto não aponta para um arquivo.
    """

    ### Variáveis ###

    # Nome do arquivo retirado do caminha absoluto 
    nome_arquivo = ""

    ### Código ###

    # Retirando ultimo valor do caminho absoluto
    nome_arquivo = abs_path.split("/")[::-1][0]

    # Verificando se é um arquivo
    if "." in nome_arquivo:
        return nome_arquivo
    else:
        raise ValueError ("Valor passado não é um arquivo")


def cria_matriz(colunas:int,linhas:int) -> list[list[int]]:
    """
    Docstring da função cria_matriz.

    Args:
        colunas(int): Valor das colunas da matriz.
        linhas(int): Valor das linhas da matriz.

    Returns:
        list: Matriz gerada com a quantidade de colunas e linhas especificada pelo usuário.
    """

    ### Variáveis ###

    #Valor que sera incrementado
    valor = 0

    #Lista da Matriz
    lista_matriz = []

    ### Código ###

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

    # Depuração simples da função 'parser_arquivo'
    a = parser_arquivo("dir1/dir2/texto.txt")
    print(a)
    
    # Depuração simples da função 'cria_matriz'
    matriz = cria_matriz(3,3)
    for linha in matriz:
        print(linha)


if __name__ == "__main__":
    main()


