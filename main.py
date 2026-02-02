from core.avl import AVL

avl = AVL()

with open('texto.txt') as txt:
  num_palavras = 0
  palavras = set()
  for index, line in enumerate(txt):
    lista = line.split()
    for string in lista:
      termo = ''.join(c for c in string if c.isalpha()).lower()
      num_palavras +=1
      palavra = (termo, index+1)
      palavras.add(palavra)
for palavra in palavras: avl.insert(*palavra)
        
    
print('-' * 10)
print('Índice:')
avl.emOrdem()
print('Número total de palavras:', num_palavras)
print('Número total de palavras repetidas:', len(palavras))
print(', '.join(avl.prefix('aids')))
print(avl.raiz())
print(avl.buscaME('aidsman'))
    

      

