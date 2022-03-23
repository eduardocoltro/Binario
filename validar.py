class Pilha:
    def __init__(self):
        self._vet = [] # lista interna

    def peek(self): # retorna qual item esta no topo
        return self._vet[-1]
       
    def push(self, item): # metodo de inserir item
        self._vet.append(item)
        
    def pop(self): # remover o topo e retornar item para usuario
        # tratar caso de underflow
        if self.is_empty():
            print("Lista Vazia!")
            return None
        return self._vet.pop()
                
    def is_empty(self): # teste se é vazia
        if len(self._vet) > 0:
            return False
        return True
        
    def __len__(self): # retorna o total de itens
        return len(self._vet)

    def __str__(self): # representacao da pilha como string
        return str(self._vet)

__name__ == "__main__"
expressao = str(input("Digite a expressao para validar:"))
p = Pilha()
sI = ["(", "{", "["]
sF = [")", "}", "]"]

for i in range(len(expressao)):
        if expressao[i] in sI:
            p.push(expressao[i])
        elif expressao[i] in sF:
            if p.is_empty():
             print("sua expressão está inválida")
            break
        else:
            if expressao[i] == ")" and p.peek() == "(":
                p.pop()
            elif expressao[i] == "[" and p.peek() == "]":
                p.pop()
            elif expressao[i] == "{" and p.peek() == "}":
                p.pop()
            else:
                print("expressao invalida!")
                break
            if len(p) == 0:
                print("expressao valida!")
                break
if p.is_empty():
    print("expressao valida!")










        
