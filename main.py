from core.avl import AVL

import time
import unicodedata

avl = AVL()

inicio = time.perf_counter()

with open('texto.txt') as txt:
  num_palavras = 0
  palavras = set()
  for index, line in enumerate(txt):
    lista = line.split()
    for string in lista:
      nfkd = unicodedata.normalize('NFKD', string)
      termo = ''.join(c for c in nfkd if c.isalpha()).lower()
      num_palavras +=1
      palavra = (termo, index+1)
      palavras.add(palavra)
      
for palavra in palavras: avl.insert(*palavra)

fim = time.perf_counter()
        
    
print('-' * 10)
print('Índice:')
avl.emOrdem()
print('Número total de palavras:', num_palavras)
print('Número total de palavras repetidas:', len(palavras))
print('Número total de palavras repetidas descartadas:', num_palavras - len(palavras))
print('Tempo de construção:', round(fim - inicio, 6))
print('Número de rotações executadas:', avl.rot)