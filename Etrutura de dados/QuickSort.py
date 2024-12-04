import time
import random

#Versão clássica
def quickSort(dados,inicio,fim):
  if inicio < fim:
    posicao_de_particionamento = partition(dados,inicio,fim)
    quickSort(dados,inicio,posicao_de_particionamento - 1)
    quickSort(dados,posicao_de_particionamento + 1,fim)

def partition(dados,inicio,fim):
  pivo = dados[inicio]
  esq = inicio + 1
  dir = fim
  flag = False
  while not flag:
    while esq <= dir and dados[esq] <= pivo:
      esq = esq + 1
    while dir >= esq and dados[dir] >= pivo:
      dir = dir -1
    if dir < esq:
      flag = True
    else:
      temp = dados[esq]
      dados[esq] = dados[dir]
      dados[dir] = temp
  temp = dados[inicio]
  dados[inicio] = dados[dir]
  dados[dir] = temp
  return dir

#Programa Principal
dados = []
for i in range(0,100000):
  n = random.randint(1,9999)
  dados.append(n)
#print(dados)

tic = time.perf_counter()
quickSort(dados,0,len(dados)-1)
toc = time.perf_counter()

print(f"Tempo: {toc - tic:0.4f} s")
#print(dados)