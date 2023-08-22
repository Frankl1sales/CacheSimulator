import math

assoc = 1  # Número de linhas na cache
n_sets = 64  # Número de conjuntos
address_bits = 32  # Número total de bits no endereço (32 bits neste caso)
b_size = 16  # Tamanho do bloco em bytes

# Criar a cache
cache = [
    [0 for _ in range(assoc)] for _ in range(n_sets)
]

def simulate_cache_access(memory_address):
    offset_bits = int(math.log2(b_size))
    index_bits = int(math.log2(n_sets))
    tag_bits = address_bits - offset_bits - index_bits

    # Calcula o endereço do conjunto (index) da cache
    print(memory_address >> offset_bits)
    set_index = (memory_address >> offset_bits) % n_sets
    set_tag = (memory_address >> (offset_bits+index_bits)) 
    print("Set Tag:", set_tag)

    print("Offset bits:", offset_bits)
    print("Index bits:", index_bits)
    print("Tag bits:", tag_bits)
    print("Memory Address:", hex(memory_address))
    print("Set Index:", set_index)

# Simulando acessos à memória
simulate_cache_access(0x4B0)
