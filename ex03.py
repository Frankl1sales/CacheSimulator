cache_lines = 4  # Número de linhas na cache
block_size = 16  # Tamanho do bloco em bytes 
address_bits = 32  # Número total de bits no endereço (32 bits neste caso)

# Criar a matriz da cache (linhas x blocos)
cache = [[None] for _ in range(cache_lines)]

def simulate_cache_access(memory_address):
    # Converter o endereço de memória para binário e preencher com zeros à esquerda
    binary_address = bin(memory_address)[2:].zfill(address_bits)

    # Dividir o endereço em tag, índice e offset
    offset_bits = binary_address[-int(address_bits / block_size):]
    index_bits = binary_address[-int(address_bits / block_size) - int(address_bits / cache_lines):-int(address_bits / block_size)]
    tag_bits = binary_address[:-int(address_bits / cache_lines) - int(address_bits / block_size)]

    tag = int(tag_bits, 2)
    index = int(index_bits, 2)

    while True:
        if cache[index][0] is None or cache[index][0] == tag:
            if cache[index][0] is None:
                print(f"Cache miss (empty line)! Tag: {tag}, Índice: {index}")
            else:
                print(f"Cache hit! Tag: {tag}, Índice: {index}")
            cache[index][0] = tag
            break
        else:
            print(f"Cache miss! Tag: {tag}, Índice: {index}")
            cache[index][0] = tag
            break

# Simulando acessos à memória
simulate_cache_access(34)
simulate_cache_access(45)
simulate_cache_access(35)
simulate_cache_access(23)

# Imprimir a matriz da cache (apenas para visualização)
for line in cache:
    print(line)
