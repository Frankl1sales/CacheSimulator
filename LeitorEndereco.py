from cache import Cache

class LeitorEndereco:
    def __init__(self, filename):
        self.filename = filename
        self.file_handle = None

    def __enter__(self):
        self.file_handle = open(self.filename, "rb")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file_handle:
            self.file_handle.close()

    def read_next_address(self):
        temp_bytes = self.file_handle.read(4)
        if len(temp_bytes) < 4:
            return None

        address = int.from_bytes(temp_bytes, byteorder='big')

        return address
# Teste da classe LeitorEndereco
if __name__ == "__main__":
    filename = "vortex.in.sem.persons.bin"
    obj = Cache(assoc=2, n_sets=512, address_bits=32, b_size=8, algorithm="r")
    # Duvida: como é a representação de uma cache que o bloco é menor que o bloco de memoria

    with LeitorEndereco(filename) as leitor:
        address = leitor.read_next_address()
        while address is not None:
            #print(hex(address))
            obj.simulate_cache_access(address)
            address = leitor.read_next_address()
    obj.imprime()