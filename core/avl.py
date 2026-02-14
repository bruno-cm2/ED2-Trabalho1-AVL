from core.no import NO


class AVL:

  def __init__(self):
    self.__raiz = None
    self.rot = 0

  def raiz(self):
    if (self.__raiz != None):
      return self.__raiz.info
    else:
      return None

  def __altura(self, no):
    if (no == None):
      return -1
    else:
      return no.altura

  def __balance(self, no):
    return self.__altura(no.esq) - self.__altura(no.dir)

  def LL(self, A):
    B = A.esq
    A.esq = B.dir
    B.dir = A

    A.altura = max(self.__altura(A.esq), self.__altura(A.dir)) + 1
    B.altura = max(self.__altura(B.esq), A.altura) + 1
    
    self.rot += 1

    return B

  def RR(self, A):
    B = A.dir
    A.dir = B.esq
    B.esq = A

    A.altura = max(self.__altura(A.dir), self.__altura(A.esq)) + 1
    B.altura = max(self.__altura(B.dir), A.altura) + 1
    
    self.rot += 1

    return B

  def LR(self, A):

    A.esq = self.RR(A.esq)
    A = self.LL(A)

    return A

  def RL(self, A):
    A.dir = self.LL(A.dir)
    A = self.RR(A)

    return A

  def insert(self, valor, linha):
    self.__raiz = self.__insert(valor, self.__raiz, linha)

  def __insert(self, valor, no, linha):
    if not no:
      return NO(valor, linha)

    if valor == no.info:
      no.linhas.append(linha)
    elif valor < no.info:
      no.esq = self.__insert(valor, no.esq, linha)
      if self.__balance(no) > 1:
        no = self.LL(no) if self.__balance(no.esq) >= 0 else self.LR(no)

    else:
      no.dir = self.__insert(valor, no.dir, linha)
      if self.__balance(no) < -1:
        no = self.RR(no) if self.__balance(no.dir) <= 0 else self.RL(no)

    no.altura = max(self.__altura(no.esq), self.__altura(no.dir))+1

    return no

  def remove(self, valor, linha):
    if not self.__raiz:
      return print(self)
    self.__raiz = self.__remove(self.__raiz, valor, linha)

  def __remove(self, no, valor, linha):
    if not no:
      return no
    if no.info > valor:
      no.esq = self.__remove(no.esq, valor, linha)
    elif no.info < valor:
      no.dir = self.__remove(no.dir, valor, linha)
    else:
      if linha in no.linhas:
        no.linhas.remove(linha)
        if len(no.linhas) > 0:
          return no
      if not no.esq or not no.dir:
        no = no.esq if no.esq else no.dir
      else:
        t = self.__buscaMenor(no.dir)
        no.info = t.info
        no.linhas = t.linhas
        no.dir = self.__remove(no.dir, no.info, linha)
        if self.__balance(no) > 1:
          no = self.LL(no) if self.__balance(no.esq) >= 0 else self.LR(no)

    if no:
      no.altura = max(self.__altura(no.esq), self.__altura(no.dir)) + 1

      if self.__balance(no) < -1:
        no = self.RR(no) if self.__balance(no.dir) <= 0 else self.RL(no)
      if self.__balance(no) > 1:
        no = self.LL(no) if self.__balance(no.esq) >= 0 else self.LR(no)

    return no

  def __buscaMenor(self, no):
    atual = no
    if atual.esq:
      atual = self.__buscaMenor(atual.esq)
    return atual

  def busca(self, valor):
    if not self.__raiz:
      return False
    return self.__busca(valor, self.__raiz)

  def buscaME(self, valor):
    no = self.busca(valor)
    if not no:
      return -1
    me = self.__contagem(no.esq) - self.__contagem(no.dir)
    if me == 0:
      return me
    print("Medidor de equilíbrio do nó:", me)

    return 1

  def __contagem(self, no):
    if not no:
      return 0
    return 1 + self.__contagem(no.esq) + self.__contagem(no.dir)

  def __busca(self, valor, no):
    if not no:
      return False
    if no.info == valor:
      return no
    elif no.info > valor:
      return self.__busca(valor, no.esq)
    else:
      return self.__busca(valor, no.dir)

  def prefix(self, pref):
    lista = []
    self.__prefix(self.__raiz, pref, lista)
    return lista

  def __prefix(self, no, pref, lista):
    if no:
      if no.info >= pref:
        self.__prefix(no.esq, pref, lista)
      if no.info.startswith(pref):
        lista.append(no.info)
      if no.info >= pref + 'z':
        self.__prefix(no.dir, pref, lista)

  def maisFreq(self):
    if not self.__raiz:
      return None
    return self.__maisFreq(self.__raiz, self.__raiz)

  def __maisFreq(self, no, maior):
    
    if not no:
      return maior
    
    if len(no.linhas) > len(maior.linhas):
      maior = no

    maior = self.__maisFreq(no.esq, maior)
    maior = self.__maisFreq(no.dir, maior)

    return maior

  def emOrdem(self):
    if self.__raiz:
      self.__emOrdem(self.__raiz)

  def __emOrdem(self, no):
    if no:
      self.__emOrdem(no.esq)
      print(f"{no.info}: {', '.join(map(str, no.linhas))} - {self.__balance(no)}")
      self.__emOrdem(no.dir)

  def __repr__(self):
    if not self.__raiz:
      return '< Árvore vazia >'
    return f'{self.__raiz}'
