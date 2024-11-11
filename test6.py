# Imagine que você está desenvolvendo uma aplicação para gerenciar pedidos de uma loja,
# onde cada pedido possui um número único de identificação que é armazenado em uma pilha
# (estrutura de dados que organiza os pedidos pela ordem de chegada).
# Sua equipe deseja analisar esses pedidos para encontrar quantos deles possuem um número de
# identificação ímpar, pois isso pode indicar um tipo especial de pedido para uma promoção. 

# Sua tarefa é criar uma função que retorne a quantidade de pedidos com número de identificação
# ímpar na pilha de pedidos. 
    
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
    
    def total_impares(self):
        i = 0
        itens = []
        
        while pilha.itens:
            pedido = pilha.pop()
            if pedido % 2 != 0: 
                i += 1
                itens.append(pedido)
        
        for item in itens:
            pilha.push(item)
        
        return i

pilha = Pilha()
pilha.push(10)
pilha.push(60)
pilha.push(30)
pilha.push(1)
pilha.push(3)

pilha.ordem_crescente()
pilha.display()
print(pilha.total_impares())
