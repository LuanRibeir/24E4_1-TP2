# Imagine que você está desenvolvendo uma aplicação para 
# processar uma lista com 5 milhões de registros. 
# Sua tarefa é implementar uma função para ordenar esses 
# registros de maneira eficiente.

# - Implemente uma função para ordenar a lista.
# - Determine a complexidade de tempo do algoritmo de ordenação escolhido usando a notação Big O.

# R: Implementação do Merge Sort, dividir e conquistar. O(n * log(n))

# 1 - Dividir
# 2 - Chamar Merge Sort pra cara metade recursivamente.
# 3 - Juntar as duuas metades em uma array

lista = [1, 3, 5, 6, 2, 4, 7, 9, 8, 10] 


def MergeSort(array):
    # Já está organizada?
    if len(array) > 1:
        
        # Dividir array
        meio = len(array) // 2
        esquerda = array[:meio]
        direita = array[meio:]
    
        # Chamadas recursivas
        MergeSort(esquerda)
        MergeSort(direita)
        
        e = 0 # id esquerda
        d = 0 # id direita
        m = 0 # id merge
        
        # Combina as duas metades ordenadas
        while e < len(esquerda) and d < len(direita):
            if esquerda[e] < direita[d]:
                array[m] = esquerda[e]
                e += 1
            else:
                array[m] = direita[d]
                d += 1
            m += 1
        
        # Adiciona os elementos restantes da metade esquerda
        while e < len(esquerda):
            array[m] = esquerda[e]
            e += 1
            m += 1
        
        # Adiciona os elementos restantes da metade direita
        while d < len(direita):
            array[m] = direita[d]
            d += 1
            m += 1
            
            
MergeSort(lista)
print(lista)