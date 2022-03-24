class Pilha:
    def __init__(self):
        self._vet = []

    def peek(self):
        if len(self._vet) > 0:
            return self._vet[-1]
       
    def push(self, item):
        self._vet.append(item)
        
    def pop(self):
        # tratar caso de underflow
        if self.is_empty():
            print("Lista Vazia!")
            return None
        return self._vet.pop()
                
    def is_empty(self):
        if len(self._vet) > 0:
            return False
        return True
        
    def __len__(self):
        return len(self._vet)

    def __str__(self):
        return str(self._vet)

__name__ == "__main__"
expressao = str(input("Digite a expressao para validar:"))
p = Pilha()
sI = ["(", "{", "["]
sF = [")", "}", "]"]

for i in range(len(expressao)):
    if expressao[i] in sI:
        p.push(expressao[i])
    if  expressao[i] in sF:
        if expressao[i] == ")" and p.peek() == "(":
            p.pop()
        elif expressao[i] == "]" and p.peek() == "[":
            p.pop()
        elif expressao[i] == "}" and p.peek() == "{":
            p.pop()    

print(p)

if p.is_empty():
    print("expressao válida!")
else:
    print("expressao inválida!")










        
