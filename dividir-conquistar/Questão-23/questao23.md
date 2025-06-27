# 23. Mesclar k Listas Ordenadas

Você recebe um array de k listas ligadas `listas`, onde cada lista ligada está ordenada em ordem crescente.

Mescle todas as listas ligadas em uma única lista ligada ordenada e retorne-a.

### Exemplo 1
Entrada: listas = [ [1,4,5], [1,3,4], [2,6] ]

Saída: [1,1,2,3,4,4,5,6]

Explicação: As listas ligadas são:
[

  1->4->5,
  
  1->3->4,
  
  2->6
  
]

Mesclando todas em uma única lista ordenada:

1->1->2->3->4->4->5->6

### Exemplo 2 

Entrada: listas = [ ]

Saída: [ ]

### Restrições:

* k == listas.length
* 0 <= k <= 10⁴
* 0 <= listas[i].length <= 500
* -10⁴ <= listas[i][j] <= 10⁴
* listas[i] está ordenada em ordem crescente.
* A soma de todos os tamanhos `listas[i].length` não excederá 10⁴.
