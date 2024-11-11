# Você está desenvolvendo uma ferramenta de análise de dados que precisa 
# identificar números duplicados em uma lista grande de valores. 
# A lista pode ter milhões de elementos, e é necessário escolher um algoritmo 
# eficiente para encontrar esses duplicados.
# Implemente duas funções em Python que encontrem números duplicados em uma lista:

#  A primeira função deve verificar cada elemento 
#  comparando-o com todos os outros, uma abordagem de força bruta.

#  A segunda função deve utilizar uma estrutura de 
#  dados adequada para melhorar a eficiência da busca de duplicados.

# Força Bruta O(n²):
def Bruta(lista):
    duplicados = []
    
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
           if lista[i] == lista[j] and lista[i]:
                duplicados.append(lista[i])
                
    return duplicados


# Estrutura Eficiente O(n):
def Eficiente(lista):
        arr = [0] * (len(lista)+1)
        
        duplicados = []  

        for num in lista:
            arr[num] += 1 
            if arr[num] == 2: 
                duplicados.append(num)

        return duplicados

lista = [1, 3, 5, 6, 2, 4, 7, 9, 9, 8, 10, 10, 2] 


print(Bruta(lista))
print(Eficiente(lista))
