# ED2-Trabalho1-AVL
Índice Remissivo com Árvore AVL

## Introdução

O problema proposto consiste na construção de um índice remissivo a partir de um arquivo de texto, associando cada palavra distinta do texto às linhas em que ela aparece.

Foi utilizada uma Árvore AVL, que é uma árvore binária de busca auto-balanceada. Essa escolha garante que as operações de inserção, remoção e busca ocorram em tempo O(log n), mesmo no pior caso, o que é essencial para lidar com textos grandes.

A solução segue os seguintes passos principais:

1. Leitura do arquivo texto linha a linha.

2. Normalização das palavras (remoção de caracteres não alfabéticos e conversão para minúsculas).

3. Inserção das palavras distintas na árvore AVL.

4. Armazenamento, em cada nó, da lista de linhas em que a palavra aparece.

- Outras operações auxiliares, como medidor de equilíbrio da árvore e frequência de palavras.

## Classe NO

Representa um nó da árvore AVL.

### Atributos:

- info: valor armazenado no nó.

- linhas: lista com os números das linhas onde o valor aparece.

- altura: altura do nó na árvore.

- esq: referência para o filho esquerdo.

- dir: referência para o filho direito.

### Propósito:

Armazenar uma palavra do índice remissivo e suas ocorrências no texto.

## Classe AVL

Classe responsável pela implementação da árvore AVL e das operações do índice.

### Inserção

```insert(valor, linha)```

Insere uma palavra na árvore.

Se a palavra já existir, a linha é adicionada à lista de ocorrências. Caso contrário, um novo nó é criado.

O balanceamento da árvore é mantido através de rotações.

### Busca

```busca(valor)```

Procura uma palavra na árvore e retorna o nó correspondente ou False caso não exista.

### Busca com Medidor de Equilíbrio (ME)

```buscaME(valor)```
