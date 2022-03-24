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
                
    def is_empty(self):
        if len(self._vet) > 0:
            return False
        return True
        
    def __len__(self):
        return len(self._vet)

    def __str__(self):
        return str(self._vet)
p = Pilha()

def ledec(n):
    while True:
        try:
            b = int(input(n))
        except(ValueError, TypeError):
                print("Só pode colocar números inteiros!")
                continue
        else:
                return b 

dec = ledec("digite um número para conversão:")
while dec > 0:
    (dec, resto) = divmod(dec, 2)
    p.push(resto)

if len(p) > 0:
    b = p.pop()
    print(str(p))
