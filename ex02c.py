import math

class CacheSimulator:
    def __init__(self, assoc, n_sets, address_bits, b_size):
        self.assoc = assoc
        self.n_sets = n_sets
        self.address_bits = address_bits
        self.b_size = b_size
        
        self.cache = [
            [0 for _ in range(self.assoc)] for _ in range(self.n_sets)
        ]
    
    def simulate_cache_access(self, memory_address):
        offset_bits = int(math.log2(self.b_size))
        index_bits = int(math.log2(self.n_sets))
        tag_bits = self.address_bits - offset_bits - index_bits
        
        set_index = (memory_address >> offset_bits) % self.n_sets
        set_tag = (memory_address >> (offset_bits + index_bits))
        
        print("Set Tag:", set_tag)
        print("Offset bits:", offset_bits)
        print("Index bits:", index_bits)
        print("Tag bits:", tag_bits)
        print("Memory Address:", hex(memory_address))
        print("Set Index:", set_index)

# Criar uma instância da classe CacheSimulator
#cache_sim = CacheSimulator(assoc=1, n_sets=64, address_bits=32, b_size=16)

# Simular acessos à memória
#cache_sim.simulate_cache_access(0x4B0)
