# Imagine que você está desenvolvendo uma aplicação de gerenciamento de tarefas,
# onde cada tarefa é armazenada em uma estrutura de dados do tipo "pilha". A cada
# nova tarefa adicionada, ela é empilhada no topo. Para facilitar a visualização e o
# gerenciamento das tarefas, você precisa de uma função que retorne qual é a tarefa
# mais recente (a que está no topo da pilha), pois essa é a próxima tarefa a ser concluída. 

# Implemente uma função tarefa_no_topo(pilha_de_tarefas) que:
    # Receba uma pilha de tarefas.
    # Retorne o elemento que está no topo da pilha, sem removê-lo.
    
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
        
    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"

pilha = Pilha()
pilha.push(10)
pilha.push(60)
pilha.push(30)



pilha.ordem_crescente()
pilha.display()
print(pilha.peek())
