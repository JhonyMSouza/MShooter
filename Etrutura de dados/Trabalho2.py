class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.next = None


class HashTable:
    def __init__(self):
        self.table = [None] * 10  # Tabela hash com 10 posições inicialmente com valor None

    def hash_function(self, sigla):
        if sigla == 'DF':
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def insert(self, sigla, nomeEstado):
        index = self.hash_function(sigla)
        new_nodo = Nodo(sigla, nomeEstado)
        new_nodo.next = self.table[index]
        self.table[index] = new_nodo

    def print_table(self):
        for i in range(10):
            print(f"Posição {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"{current.sigla} -> ", end="")
                current = current.next
            print("None")


# Lista dos 26 estados e o Distrito Federal
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
]

# Estado fictício
estado_ficticio = ("JS", "Jhony Max de Souza")

# Criação da Tabela Hash
hash_table = HashTable()

# Impressão da tabela hash antes de inserir qualquer informação
print("Tabela Hash antes de inserir qualquer informação:")
hash_table.print_table()

# Inserção dos 26 estados e o Distrito Federal na tabela hash
for sigla, nome in estados:
    hash_table.insert(sigla, nome)

# Impressão da tabela hash após inserir os 26 estados e o Distrito Federal
print("\nTabela Hash após inserir os 26 estados e o Distrito Federal:")
hash_table.print_table()

# Inserção do estado fictício na tabela hash
hash_table.insert(estado_ficticio[0], estado_ficticio[1])

# Impressão da tabela hash após inserir o estado fictício
print("\nTabela Hash após inserir os 26 estados, Distrito Federal e o estado fictício:")
hash_table.print_table()
