class Foo:
  def __init__(self, x=None):
    self._x = x

  @property
  def x(self):
    return self._x or 0
    
  @x.setter
  def x(self, valor):
    self._x += valor


foo = Foo(10)
