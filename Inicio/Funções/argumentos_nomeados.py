def salvar_carro(marca, modelo, ano, placa):
  print(f"Carro cadastrado com sucesso! {marca}/{modelo}/{ano}/{placa}")



salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Chevrolet",modelo="Onix", ano=2020, placa="XYZ-5678")
salvar_carro(**{"marca":"Volkswagen", "modelo":"Gol", "ano":2015, "placa":"DEF-9012"})