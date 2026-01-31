from core.no import NO

class AVL:
  
  def __init__(self):
    self.__raiz = None

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

    A.__altura = max(self.__altura(A.esq), self.__altura(A.dir)) + 1
    B.__altura = max(self.__altura(B.esq), A.__altura) + 1

    return B

  def RR(self, A):
    B = A.dir
    A.dir = B.esq
    B.esq = A

    A.__altura = max(self.__altura(A.dir), self.__altura(A.esq)) + 1
    B.__altura = max(self.__altura(B.dir), A.__altura) + 1

    return B

  def LR(self, A):

    A.esq = self.LL(A.esq)
    A = self.RR(A)

    return A

  def RL(self, A):
    A.dir = self.RR(A.dir)
    A = self.LL(A)

    return A

  def insert(self, valor):
    self.__raiz = self.__insert(valor, self.__raiz)

  def __insert(self, valor, no):
    if not no:
      return NO(valor)

    if valor == no.info:
      no.freq += 1
    elif valor < no.info:
      no.esq = self.__insert(valor, no.esq)
      if self.__balance(no) > 1:
        no = self.LL(no) if no.esq.info > valor else self.LR(no)
    else:
      no.dir = self.__insert(valor, no.dir)
      if self.__balance(no) < -1:
        no = self.RR(no) if no.dir.info < valor else self.RL(no)

    no.altura = max(self.__altura(no.esq), self.__altura(no.dir))+1

    return no

  def busca(self, valor):
    if not self.__raiz:
      return False
    return self.__busca(valor, self.__raiz)

  def __busca(self, valor, no):
    if not no:
      return False
    if no.info == valor:
      return no
    elif no.info > valor:
      return self.__busca(valor, no.esq)
    else:
      return self.__busca(valor, no.dir)

  def __emOrdem(self, no):
    if no:
      self.__emOrdem(no.esq)
      print("(", no.info, no.freq, ") ", end=' ')
      self.__emOrdem(no.dir)

  def emOrdem(self):
    if (self.__raiz != None):
      self.__emOrdem(self.__raiz)
  
  def __repr__(self):
    if not self.__raiz:
      return '< Árvore vazia >'
    return f'{self.__raiz}'