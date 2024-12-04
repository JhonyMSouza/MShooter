class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero  # Inicializa o atributo número do nodo
        self.cor = cor  # Inicializa o atributo cor do nodo
        self.proximo = None  # Inicializa o ponteiro para o próximo nodo como None

class ListaEncadeada:
    def __init__(self):
        self.head = None  # Inicializa a cabeça da lista como None

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo  # Se a lista estiver vazia, o nodo se torna a cabeça da lista
        else:
            atual = self.head  # Começa a percorrer a lista a partir da cabeça
            while atual.proximo is not None:
                atual = atual.proximo  # Percorre até o último nodo
            atual.proximo = nodo  # Insere o novo nodo no final da lista

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo  # Se a lista estiver vazia, o nodo se torna a cabeça da lista
        elif self.head.cor == "V":
            nodo.proximo = self.head  # Insere o novo nodo antes da cabeça atual se for verde
            self.head = nodo
        else:
            atual = self.head  # Começa a percorrer a lista a partir da cabeça
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo  # Percorre até o último nodo com cor "A"
            nodo.proximo = atual.proximo  # Insere o novo nodo após todos os nodos amarelos
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A / V): ").upper()
        if cor not in ["A", "V"]:
            print("Cor inválida! Digite 'A' / 'V'.")
            return
        try:
            numero = int(input("Digite o número do cartão: "))
        except ValueError:
            print("Número inválido! Digite um número inteiro.")
            return

        nodo = Nodo(numero, cor)  # Cria um novo nodo com a cor e o número fornecidos

        if self.head is None:
            self.head = nodo  # Se a lista estiver vazia, o novo nodo se torna a cabeça da lista
        else:
            if cor == "V":
                self.inserirSemPrioridade(nodo)  # Se a cor do nodo é verde, insere sem prioridade
            else:
                self.inserirComPrioridade(nodo)  # Se a cor do nodo é amarela, insere com prioridade

    def imprimirListaEspera(self):
        atual = self.head
        if atual is None:
            print("A lista de espera está vazia.")
            return
        print("lista -> ", end="")
        while atual is not None:
            print(f"[{atual.cor},{atual.numero}]", end=" ")  # Imprime cada nodo no formato [cor,numero]
            atual = atual.proximo
        print()  # Adiciona uma nova linha ao final da lista

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na fila de espera.")
        else:
            paciente = self.head  # Remove a cabeça da lista e chama o paciente
            self.head = self.head.proximo
            print(f"Chamando paciente com cartão número: {paciente.numero}")


def menu():
    lista = ListaEncadeada()
    while True:
        print("\nMenu:")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            lista.inserir()  # Chama a função inserir() para adicionar um paciente à fila
        elif opcao == '2':
            lista.imprimirListaEspera()  # Chama a função imprimirListaEspera() para mostrar a fila
        elif opcao == '3':
            lista.atenderPaciente()  # Chama a função atenderPaciente() para chamar um paciente
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Escolha novamente.")


if __name__ == "__main__":
    menu()  # Inicia o programa chamando a função menu()
