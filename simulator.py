# Exemplo de manipulação de endereços

# Representando endereços como inteiros
endereco1 = 0x1000
endereco2 = 0x2000

# Operações básicas
diferenca = endereco2 - endereco1
print(f"Diferença entre endereços: {diferenca}")

# Uso de deslocamentos (shifts) e máscaras
endereco = 0xABCD1234
n_bits_offset = 4
n_bits_indice = 8

tag = endereco >> (n_bits_offset + n_bits_indice)
indice = (endereco >> n_bits_offset) & ((1 << n_bits_indice) - 1)

print(f"Tag: {tag:X}")
print(f"Índice: {indice:X}")
