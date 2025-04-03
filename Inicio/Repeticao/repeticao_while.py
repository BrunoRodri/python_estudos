saldo = 500
def sacar(saldo, valor_saque):
  if saldo >= valor_saque:
    saldo -= valor_saque
    print(f"Saque efetuado com sucesso! Saldo atual: {saldo}")
    print("Retire o dinheiro na boca do caixa.")
  else:
    print("Saldo insuficiente!")
  return saldo

while True:
  print("\n" + "="*30)
  print("\nSeja bem-vindo(a)!")
  opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato \n[3] Sair \n>>>"))

  if opcao == 1:
    valor_saque = float(input("Informe o valor do saque: "))
    saldo = sacar(saldo, valor_saque)
  elif opcao == 2:
    print("Extrato:")
    print(f"Saldo atual: {saldo}")
  elif opcao == 3:
    print("Saindo do sistema...")
    break
  else:
    print("Opção inválida! Tente Novamente")
