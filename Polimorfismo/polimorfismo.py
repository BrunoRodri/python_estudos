class Passaro:
  def voar(self):
    print("Voando...")


class Pato(Passaro):
  def voar(self):
    return super().voar()  # Chama o método voar da classe pai Passaro


class Avestruz(Passaro):
  def voar(self):
    print("O avestruz não pode voar")


def plano_voo(obj):
  obj.voar()

p1 = Pato()
p2 = Avestruz()

plano_voo(p1)  # O pássaro está voando
plano_voo(p2)  # O avestruz não pode voar