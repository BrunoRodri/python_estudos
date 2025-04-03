class Veiculo:
  def __init__(self, cor, placa, numero_rodas):
    self.cor = cor
    self.placa = placa
    self.numero_rodas = numero_rodas

  def ligar_motor(self):
    print("Motor ligado")

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Carro(Veiculo):
  pass

class Motocicleta(Veiculo):
  pass

class Caminhao(Veiculo):
  def __init__(self, cor, placa, numero_rodas, carregado):
    super().__init__(cor, placa, numero_rodas)
    self.carregado = carregado

  def esta_carregado(self):
    print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("Preta", "abc-2345", 2)
carro = Carro("azul", "abc-1234", 4)
caminhao = Caminhao("verde", "abc-0887", 6, True)

print(moto)
print(carro)
print(caminhao)