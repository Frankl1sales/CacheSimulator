import math

assoc = 4  # Número de linhas na cache
n_sets = 4  # Tamanho do bloco em bytes
address_bits = 32  # Número total de bits no endereço (32 bits neste caso)
b_size = 16 # Número
# Criar a cache
cache = [
    [0 for i in range(assoc)] for j in range(n_sets)
]
cache_val = [
    [0 for i in range(assoc)] for j in range(n_sets)
]

for i in cache:
    print(i)

def simulate_cache_aces(memory_address):
    offset = int(math.log2(b_size))
    index_bits = int(math.log2(n_sets))
    tag_bits = address_bits-offset-index_bits
    print(offset)
    print(index_bits)
    print(tag_bits)

    endereco = int(memory_address) / (2**offset)
    print(endereco)

    mapecache = endereco % n_sets
    print(mapecache)

    # Simulando acessos à memória
simulate_cache_aces(0x014)

"""
    index_bits = memory_address[:address_bits - (int(address_bits/))]

def simulate_cache_access(memory_address):
    # Converter o endereço de memória para binário e preencher com zeros à esquerda
    binary_address = bin(memory_address)[2:].zfill(address_bits)

    # Dividir o endereço em tag, índice e offset
    tag_bits = binary_address[:address_bits - (int(address_bits / cache_lines) + int(address_bits / block_size))]
    index_bits = binary_address[-int(address_bits / cache_lines) - int(address_bits / block_size):-int(address_bits / block_size)]
    offset_bits = binary_address[-int(address_bits / block_size):]

    tag = int(tag_bits, 2)
    index = int(index_bits, 2)
    offset = int(offset_bits, 2)

    # Verificar se o bloco está na cache
    if cache[index][0] == tag:
        print(f"Cache hit! Tag: {tag}, Índice: {index}, Offset: {offset}")
    else:
        print(f"Cache miss! Tag: {tag}, Índice: {index}, Offset: {offset}")
        cache[index][0] = tag

# Simulando acessos à memória
simulate_cache_access(20)
simulate_cache_access(40)
simulate_cache_access(45)
simulate_cache_access(23)

# Imprimir a matriz da cache (apenas para visualização)
for line in cache:
    print(line)
"""