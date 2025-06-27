# Definindo a classe ListNode para representar os nós das listas ligadas
class NoLista:
    def __init__(self, valor=0, proximo=None):
        self.valor = valor  # Valor armazenado no nó
        self.proximo = proximo  # Ponteiro para o próximo nó na lista

class Solucao:
    def mesclarKListas(self, listas: list) -> NoLista:
        # Função para mesclar duas listas ligadas
        def mesclarDuasListas(l1, l2):
            # Nó fictício para facilitar a lógica de mesclagem
            dummy = NoLista()  
            atual = dummy  # Ponteiro que percorre a lista resultante
            while l1 and l2:
                # Comparando os valores das duas listas e adicionando o menor à lista resultante
                if l1.valor < l2.valor:
                    atual.proximo = l1  # Apontamos o próximo nó da lista resultante para o nó de l1
                    l1 = l1.proximo  # Avançamos para o próximo nó de l1
                else:
                    atual.proximo = l2  # Apontamos o próximo nó da lista resultante para o nó de l2
                    l2 = l2.proximo  # Avançamos para o próximo nó de l2
                atual = atual.proximo  # Avançamos para o próximo nó na lista resultante
            # Se sobrar algum nó em l1 ou l2, adicionamos na lista resultante
            atual.proximo = l1 if l1 else l2
            return dummy.proximo  # Retorna o primeiro nó da lista mesclada

        # Caso base: se a lista de listas estiver vazia, retornamos None
        if not listas:
            return None

        # Usamos a técnica de dividir e conquistar
        while len(listas) > 1:
            mescladas = []  # Lista para armazenar os resultados das mesclagens
            for i in range(0, len(listas), 2):
                # Pegamos dois elementos da lista de listas para mesclar
                l1 = listas[i]
                # Se houver um número ímpar de listas, o último item não terá par
                l2 = listas[i + 1] if i + 1 < len(listas) else None
                mescladas.append(mesclarDuasListas(l1, l2))  # Mescla os dois e adiciona à lista de resultados
            listas = mescladas  # Atualizamos a lista de listas com as mesclagens feitas

        # Quando restar apenas uma lista, ela será a lista final ordenada
        return listas[0]

# Função para criar uma lista ligada a partir de uma lista de valores
def criar_lista_ligada(valores):
    dummy = NoLista()  # Nó fictício para facilitar a criação
    atual = dummy
    for valor in valores:
        atual.proximo = NoLista(valor)  # Cria um novo nó e adiciona à lista
        atual = atual.proximo  # Avança para o próximo nó
    return dummy.proximo  # Retorna o primeiro nó da lista ligada

# Função para exibir uma lista ligada
def exibir_lista_ligada(no):
    valores = []
    while no:
        valores.append(str(no.valor))  # Adiciona o valor do nó à lista de valores
        no = no.proximo  # Avança para o próximo nó
    print(" -> ".join(valores))  # Exibe os valores no formato de lista ligada

# Função principal para obter as listas de entrada do usuário
def principal():
    # Obter o número de listas que o usuário deseja inserir
    k = int(input("Quantas listas você quer mesclar? "))
    
    listas = []
    for i in range(k):
        # Para cada lista, o usuário insere os valores separados por espaços
        input_valores = input(f"Digite os valores da lista {i + 1} (separados por espaço): ")
        valores = list(map(int, input_valores.split()))  # Converte os valores para inteiros
        lista_ligada = criar_lista_ligada(valores)  # Cria a lista ligada a partir dos valores
        listas.append(lista_ligada)  # Adiciona a lista ligada à lista de listas
    
    # Instanciando a classe Solucao
    solucao = Solucao()
    
    # Chamando o método mesclarKListas para mesclar as listas
    resultado = solucao.mesclarKListas(listas)
    
    # Exibindo o resultado
    print("Lista mesclada ordenada:")
    exibir_lista_ligada(resultado)  # Exibe a lista mesclada

# Chamando a função principal para rodar o programa
if __name__ == "__main__":
    principal()
