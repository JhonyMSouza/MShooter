class ElementoDaListaSimples:
    def __init__(self, sigla=None, nomeEstado=None):
        self.sigla = sigla  # Inicializa a sigla do estado
        self.nomeEstado = nomeEstado  # Inicializa o nome do estado
        self.proximo = None  # Inicializa o ponteiro para o próximo nodo como None

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None  # Inicializa a cabeça da lista encadeada como None

    def inserir(self, sigla, nomeEstado):
        nodo = ElementoDaListaSimples(sigla, nomeEstado)  # Cria um novo nodo com a sigla e o nome do estado
        if self.head is None:
            self.head = nodo  # Se a lista está vazia, o novo nodo se torna a cabeça
        else:
            nodo.proximo = self.head  # Caso contrário, o novo nodo aponta para a cabeça atual
            self.head = nodo  # E a cabeça é atualizada para o novo nodo

    def imprimir(self):
        temp = self.head  # Começa da cabeça da lista
        while temp:  # Percorre a lista até o final
            print(f"{temp.sigla}", end=" -> ")  # Imprime a sigla do nodo atual
            temp = temp.proximo  # Move para o próximo nodo
        print("None")  # Indica o final da lista

class TabelaHash:
    def __init__(self):
        self.tam = 10  # Define o tamanho da tabela hash como 10
        self.h = [ListaEncadeadaSimples() for _ in range(self.tam)]  # Inicializa a tabela com 10 listas encadeadas

    def hashFunc(self, k):
        if k == "DF":
            return 7  # Se a sigla é "DF", retorna 7 por superstição
        i1, i2 = ord(k[0]), ord(k[1])  # Obtém os valores ASCII das duas letras
        return (i1 + i2) % self.tam  # Calcula o hash usando a soma dos valores ASCII e o tamanho da tabela

    def inserir(self, sigla, nomeEstado):
        pos = self.hashFunc(sigla)  # Calcula a posição na tabela hash para a sigla
        self.h[pos].inserir(sigla, nomeEstado)  # Insere o estado na lista encadeada na posição calculada

    def imprimir(self):
        for i in range(self.tam):  # Percorre todas as posições da tabela hash
            print(f"{i}: ", end="")  # Imprime o índice da posição atual
            self.h[i].imprimir()  # Imprime a lista encadeada na posição atual

# Programa principal
Teste = TabelaHash()  # Cria uma nova tabela hash

print("Tabela vazia")
Teste.imprimir()  # Imprime a tabela hash vazia

estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
]

for sigla, nome in estados:
    Teste.inserir(sigla, nome)  # Insere cada estado na tabela hash

print("\nTabela com os 26 estados e o Distrito Federal:")
Teste.imprimir()  # Imprime a tabela hash após inserir todos os estados

estadoFicticio = ("JS", "Jhony Max de Souza")  # Define o estado fictício
Teste.inserir(*estadoFicticio)  # Insere o estado fictício na tabela hash

print("\nTabela com os 26 estados, Distrito Federal e o estado fictício:")
Teste.imprimir()  # Imprime a tabela hash após inserir o estado fictício
