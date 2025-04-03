def calcular_saldo(transacoes):
    saldo = 0
    
    for valor in transacoes:
      saldo = sum(transacoes)
    
    return f"Saldo: R$ {saldo:.2f}"
        

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)