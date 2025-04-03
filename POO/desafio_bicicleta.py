class Bicicleta:
  def __init__(self, cor, modelo, ano, valor,):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor

  def buzinar(self):
    print("Bip Bip")

  def parar(self):
    print("Parando a bicicleta")
    print(f"A bicicleta {self.modelo} parou")

  def andar(self):
    print("Acelerando a bicicleta")
    print(f"A bicicleta {self.modelo} está andando")

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



b1 = Bicicleta("vermelha", "caloi", 2020, 1000)

b1.buzinar()
b1.andar()
b1.parar()
print(f"A bicicleta {b1.modelo} é {b1.cor} e custa {b1.valor}")

b2 = Bicicleta("azul", "monark", 2021, 1200)

Bicicleta.buzinar(b2)

print(b2)