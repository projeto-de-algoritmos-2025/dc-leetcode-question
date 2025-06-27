from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        indexed_nums = [(i, num) for i, num in enumerate(nums)]

        def merge_sort(start, end):
            if end - start <= 1:
                return indexed_nums[start:end]

            mid = (start + end) // 2
            left = merge_sort(start, mid)
            right = merge_sort(mid, end)

            merged = []
            i = j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or (i < len(left) and left[i][1] <= right[j][1]):
                    result[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            indexed_nums[start:end] = merged
            return merged

        merge_sort(0, n)
        return result


def interativo():
    print("=== Contador de elementos menores à direita ===")
    entrada = input("Digite a lista de números separada por vírgula (ex: 5,2,6,1): ")
    try:
        nums = list(map(int, entrada.strip().split(',')))
        sol = Solution()
        resultado = sol.countSmaller(nums)
        print(f"\n✅ Resultado: {resultado}")
    except ValueError:
        print("❌ Entrada inválida. Certifique-se de digitar apenas números inteiros separados por vírgula.")

if __name__ == "__main__":
    interativo()
