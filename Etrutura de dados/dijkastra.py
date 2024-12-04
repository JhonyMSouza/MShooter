#implementação com lista de adjacência
class Vertice:
    def __init__(self, n):
      self.nome = n
      self.vizinhos = list()
      self.pesos = list()

    def addVizinho(self, v, peso):
      if v not in self.vizinhos:
          self.vizinhos.append(v)
          self.vizinhos.sort()
          self.pesos.append(peso)

class Grafo:
    vertices = {}
    ordem = 0

    def __init__(self):
        self.totalVertices = 0

    def addVertice(self, vertice):
        #Verifique se o objeto é de fato um objeto de vértice e se ele ainda não existe
        if isinstance(vertice, Vertice) and vertice.nome not in self.vertices:
            #adiciona o vértice no dicionario
            self.vertices[vertice.nome] = vertice
            self.totalVertices += 1
            return True
        else:
            return False

    def addAresta(self, u, v, peso):
        #verifica se ambos vertices de fato existe para criar a aresta
        if u in self.vertices and v in self.vertices:
            for key, valor in self.vertices.items():
                #adiciona um na lista de vizinhos do outro
                if key == u:
                    valor.addVizinho(v, peso)
                if key == v:
                    valor.addVizinho(u, peso)
            return True
        else:
            return False

    #Imprime a lsita de adjacências
    def printGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].vizinhos) + ' ' + str(self.vertices[key].pesos))

    def Dijkstra(self, origem):
        distancias = [float('inf') for i in range(0, self.totalVertices)]
        visitados = [0 for i in range(0, self.totalVertices)]
        predecessor = [float('inf') for i in range(0, self.totalVertices)]
        nodos = [v for v in self.vertices]

        distancias[nodos.index(origem.nome)] = 0
        predecessor[nodos.index(origem.nome)] = origem

        for x in range(0, self.totalVertices):
            # Pega o próximo vértice com menor distância
            minDistancia = float('inf')
            for v in range(0, self.totalVertices):
                if(distancias[v] < minDistancia and visitados[v] == 0):
                    minDistancia = distancias[v]
                    idxProxVertice = v

            #Verifica se existe um melhor caminho prolo ProxVertice
            visitados[idxProxVertice] = 1
            nodoAtual = self.vertices[nodos[idxProxVertice]]
            idx = 0
            for vizinho in nodoAtual.vizinhos:
                if (visitados[nodos.index(vizinho)] == 0):
                    if(minDistancia + nodoAtual.pesos[idx] < distancias[nodos.index(vizinho)]):
                        distancias[nodos.index(vizinho)] = minDistancia + nodoAtual.pesos[idx]
                        predecessor[nodos.index(vizinho)] = nodoAtual
                idx += 1
        r = 1

        #print dos caminhos
        print('Vértice de Origem: {}'.format(origem.nome))
        for i in range(1, self.totalVertices):
            print('Distância para {} = {}'.format(nodos[i], distancias[i]))
            print('Caminho: {} '.format(nodos[i]), end = '')
            j = i
            atual = predecessor[j].nome
            while (atual != origem.nome):
                print('<- {} '.format(atual), end = '')
                atual = predecessor[nodos.index(atual)].nome
            print('<- {} '.format(origem.nome))



#Programa principal
G = Grafo()
origem = Vertice('A')
G.addVertice(origem)

for i in range(ord('A'), ord('G')):
    G.addVertice(Vertice(chr(i)))

arestas = ['AB','AD','BC','CD','CE','CF']
pesos = [10,3,4,1,2,2]
i = 0
for aresta in arestas:
    G.addAresta(aresta[:1], aresta[1:], pesos[i])
    i += 1

G.Dijkstra(origem)
#G.printGrafo()