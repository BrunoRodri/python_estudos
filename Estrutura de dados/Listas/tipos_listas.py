frutas = ["manzana", "banana", "naranja", "kiwi", "mango"]
frutas[0] # manzana
frutas[-1] # mango

frutas2 = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "f8", 4200000, 2020, 2900, "São Paulo", "Brasil", True]

matriz = [
  [1, "a", 2],
  [3.14, "b", 4],
  ["c", 5, 6]
]

matriz[0] #[1,"a",2]
matriz[0][1] # "a"


############## FATIAMENTO #################
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]


############## ITERAR LISTAS #################
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



############## COMPRESSAO DE LISTAS #################

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)