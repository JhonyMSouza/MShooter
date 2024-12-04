class BST:
    def __init__(self, dado=None):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def inserir(self, dado):
        if (self.dado == None):
            self.dado = dado
        else:
            if (dado < self.dado):
                if (self.esquerda): #self.esquerda == None:
                    self.esquerda.inserir(dado)
                else:
                    self.esquerda = BST(dado)
            else:
                if(self.direita): #self.direita == None:
                    self.direita.inserir(dado)
                else:
                    self.direita = BST(dado)

    def emOrdem(self, lst):
        if (self.esquerda):
            self.esquerda.emOrdem(lst)
        lst.append(self.dado) #root
        if (self.direita):
            self.direita.emOrdem(lst)
        return lst

    def preOrdem(self, lst):
        lst.append(self.dado) #root
        if (self.esquerda):
            self.esquerda.preOrdem(lst)
        if (self.direita):
            self.direita.preOrdem(lst)
        return lst

    def posOrdem(self, lst):
        if (self.esquerda):
            self.esquerda.posOrdem(lst)
        if (self.direita):
            self.direita.posOrdem(lst)
        lst.append(self.dado) #root
        return lst

    def emNivel(self):
        nodoAtual = self
        lst = []
        fila = []
        fila.insert(0,nodoAtual)
        while(len(fila) > 0):
            nodoAtual = fila.pop()
            lst.append(nodoAtual.dado)
            if(nodoAtual.esquerda):
                fila.insert(0,nodoAtual.esquerda)
            if(nodoAtual.direita):
                fila.insert(0,nodoAtual.direita)

        return lst

#            Jader
#        /           \
#      /              \
#   Camila           Maria
#    / \             /     \
#  Ana   Eduardo   Leonardo   Yago

Teste = BST()

while True:
  print('1 - Inserir na árvore binária')
  print('2 - Remover da árvore binária')
  print('3 - Imprimir a árvore binária')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))
  if op == 1:
    dado = input('Qual nome deseja inserir?')
    Teste.inserir(dado)
  #elif op == 2:
    # dado = input('Qual nome deseja remover?')
    # Teste.deletar(dado)
  elif op == 3:
    print('Em ordem: ', Teste.emOrdem([]))
  elif op == 4:
    print('Encerrando...')
    break
  else:
    print("Selecione outra opção!\n")