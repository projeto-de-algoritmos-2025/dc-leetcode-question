from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def select(nums, k):
            if len(nums) <= 5:
                return sorted(nums)[k]

            chunks = [nums[i:i + 5] for i in range(0, len(nums), 5)]
            medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

            pivot = select(medians, len(medians) // 2)

            lows = [el for el in nums if el < pivot]
            highs = [el for el in nums if el > pivot]
            pivots = [el for el in nums if el == pivot]

            if k < len(lows):
                return select(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return select(highs, k - len(lows) - len(pivots))

        return select(nums, len(nums) - k)


def interativo():
    print("=== Encontrar o k-ésimo maior elemento ===")
    entrada = input("Digite a lista de números separada por vírgula (ex: 3,2,1,5,6,4): ")
    try:
        nums = list(map(int, entrada.strip().split(',')))
        k = int(input("Digite o valor de k (ex: 2): "))
        if k < 1 or k > len(nums):
            print("⚠️  Valor de k inválido.")
            return
        sol = Solution()
        resultado = sol.findKthLargest(nums, k)
        print(f"\n✅ O {k}-ésimo maior elemento é: {resultado}")
    except ValueError:
        print("❌ Entrada inválida. Certifique-se de usar apenas números inteiros.")

if __name__ == "__main__":
    interativo()
