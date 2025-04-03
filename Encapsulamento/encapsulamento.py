class Conta:
  def __init__(self, nro_agencia, saldo=0):
    self._saldo = saldo
    self.nro_agencia = nro_agencia
    

  def depositar(self, valor):
    self._saldo += valor
    

  def sacar(self, valor):
    self._saldo -= valor

  def get_saldo(self):
    return self._saldo


conta = Conta("0001", 1000)
conta.depositar(500)

print(conta._saldo) # Atributo protegido, não deve ser acessado diretamente

print(conta.nro_agencia) 
print(conta.get_saldo())
