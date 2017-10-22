import numpy as np

A = np.array([
    [1, 2], 
    [3, 4]
])

B = np.array([
    [1, 1, 2],
    [4, 5, 7]
])

def calc_terms(line, col):

    term = 0   

    for i, _ in enumerate(line):

        term += line[i] * col[i]
        i+=1

    return term
    
#fato: o número de elementos em uma linha, é o número de colunas de uma matriz
#bem pythonico mas a segunda coluna está sobrescrevendo a primeira, sem numpy
#cols.append([row[i] for i, row in enumerate(matrix)])
def get_cols(matrix):
    cols = []

    for i,_ in enumerate(matrix[0]):
        cols.append(matrix.transpose()[i])

    return cols
 

def matrix_prod(a, b):
    
    b_cols = get_cols(b)
    c = []
    
    for line in a:

        ax = []
	
	#paralelizar calc_terms, cada loop manda um trabalho pra sacola
        for col in b_cols:
            ax.append(calc_terms(line, col))

        c.append(ax)

    return c

print(matrix_prod(A, B))

