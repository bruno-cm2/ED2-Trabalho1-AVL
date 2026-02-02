class NO:
  def __init__(self, info, linha):
    self.info = info
    self.altura = 0
    self.linhas = [linha]
    self.esq = None
    self.dir = None

  def __repr__(self):
    dir = f'>{self.dir}' if self.dir else ''
    esq = f'{self.esq}<' if self.esq else ''
    return  f'{esq} {self.info} {dir}'