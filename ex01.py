from LeitorEndereco import LeitorEndereco

class cache:
    def __init__(self,b_size,assoc):
    
    def calcular_indice(self,endereco, n_sets):
        return endereco % n_sets

# Criar a cache
    n_sets = int(input("Digite o número de conjuntos: "))
    assoc = int(input("Digite o número de associações: "))

cache_tag = [
    [0 for i in range(assoc)] for j in range(n_sets)
]
cache_val = [
    [0 for i in range(assoc)] for j in range(n_sets)
]

for i in cache_tag:
    print(i)

# Simular a leitura do próximo endereço
"""""
objeto = LeitorEndereco()

endereco = objeto.read_next_address()
print("Endereço de memória lido:", endereco)

indice_do_conjunto = calcular_indice(endereco, n_sets)
print("Índice do conjunto:", indice_do_conjunto)
"""

"""
lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

lista = [1 for numero in range(10)]
print(lista)
"""