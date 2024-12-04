import time
import random
def bubbleSort(dados):
  #tamanho do conjunto de dados
  tam = len(dados)
  #laço que ocorre quantidade de vezes igual ao
  #tamanho do conjunto de dados
  for v in range(0, tam, 1):
    #laço interno que pega os valores em pares
    for i in range(0, tam-1, 1):
      #comparação
      if dados[i] > dados[i+1]:
        #troca os dados usando variável auxiliar
        aux = dados[i]
        dados[i] = dados[i+1]
        dados[i+1] = aux

#Programa Principal
dados = []
for i in range(0,10000):
    n = random.randint(1,9999)
    dados.append(n)
#print(dados)

tic = time.perf_counter()
bubbleSort(dados)
toc = time.perf_counter()

print(f"tempo: {toc - tic:0.4f} s")
#print(dados)