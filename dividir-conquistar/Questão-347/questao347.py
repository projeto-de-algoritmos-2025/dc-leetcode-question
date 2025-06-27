import heapq

def elementos_mais_frequentes(numeros, k):
    # Dicionário para contar as frequências
    frequencia = {}
    
    for numero in numeros:
        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1
    
    # Usando min-heap para armazenar os k mais frequentes
    heap = []
    for numero, contagem in frequencia.items():
        heapq.heappush(heap, (contagem, numero))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extraindo os números do heap
    resultado = []
    while heap:
        contagem, numero = heapq.heappop(heap)
        resultado.append(numero)
    
    return resultado

# Função principal para entrada do usuário
def main():
    entrada = input("Digite os números separados por espaço: ")
    numeros = list(map(int, entrada.strip().split()))
    
    k = int(input("Digite o valor de k: "))
    
    resposta = elementos_mais_frequentes(numeros, k)
    
    print("Os", k, "elementos mais frequentes são:", resposta)

# Executa a função principal
if __name__ == "__main__":
    main()
