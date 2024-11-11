# Imagine que você está desenvolvendo uma aplicação de notas escolares
# onde os resultados das avaliações de cada aluno são armazenados em
# uma pilha, de modo que as últimas notas lançadas ficam no topo.
# Para gerar um relatório de desempenho, é necessário exibir as notas
# em ordem crescente, o que permite visualizar facilmente a evolução
# e as tendências de desempenho do aluno.  

# Sua tarefa é criar uma função que ordene os valores dessa pilha
# em ordem crescente.

class Pilha:
    def __init__(self):
        self.itens = []
        
    def is_empty(self):
        return len(self.itens) == 0
        
    def push(self, item):
        self.itens.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def ordem_crescente(self):
        itens = []
        while self.itens:
            itens.append(self.pop())
            
        itens.sort()
    
        for item in itens:
            self.push(item)

    def display(self):
        print("Pilha:", self.itens)

pilha = Pilha()
pilha.push(10)
pilha.push(60)
pilha.push(30)

pilha.display()

pilha.ordem_crescente()

pilha.display()

