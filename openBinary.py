# Abrir um arquivo binário em modo de leitura
def openBinary(name):
    with open(name, 'rb') as file:
        binary_data = file.read()  # Lê todos os bytes do arquivo
    # Suponha que cada endereço ocupe 4 bytes (32 bits)
    address_size = 4
    num_addresses = len(binary_data) // address_size
    # Interpretar os dados binários como endereços
    addresses = []
    for i in range(num_addresses):
        start = i * address_size
        end = start + address_size
        address_bytes = binary_data[start:end]
        address = int.from_bytes(address_bytes, byteorder='big')  # Converte bytes para int
        addresses.append(address)
    return addresses
