#criar a classe cache
import math
import random

class Cache:
    def __init__(self, assoc, n_sets, address_bits, b_size,algorithm):
        self.assoc = assoc
        self.n_sets = n_sets
        self.address_bits = address_bits
        self.b_size = b_size
        self.cache = [[None for _ in range(self.assoc)] for _ in range(self.n_sets)]
        self.algorithm = algorithm.lower()

        self.hits = 0
        self.misses = 0
        self.acess = 0
        self.compulsory_misses = 0
        self.unique_blocks_referenced = set()  # Conjunto de blocos únicos referenciados
        self.buffer = []
        
    def random_replace(self, set_index, set_tag):
        random_block_index = random.randint(0, self.assoc - 1)
        self.cache[set_index][random_block_index] = set_tag

    def lru_replace(self, set_index, set_tag):
       return     

    def searchBuffer(self,set_index):
        if len(self.buffer) == 0: return None
        #pesquisa o set
        for c in range(0,len(self.buffer),2):
            if self.buffer[c] == set_index:
                return self.buffer[c+1]
        return None

    def fifo_replace(self, set_index, set_tag):
        # caso não tenha nenhum elemento
        if self.searchBuffer(set_index) == None:
            self.cache[set_index][0] = set_tag
            self.buffer.append(set_index)
            self.buffer.append(1) # Marca a prox pos de preenchimento
            return
        # verifica se ta no final da fila, procura no buffer e zera a posição
        if self.searchBuffer(set_index) == self.b_size:
            for c in range(0,len(self.buffer),2):
                if self.buffer[c] == set_index:
                    self.buffer[c+1] = 0
        # add na pos de preenchimento
        self.cache[set_index][self.searchBuffer(set_index)]
        # pesquisa o set e incrementa o valor do buffer
        for c in range(0,len(self.buffer),2):
                if self.buffer[c] == set_index:
                    self.buffer[c+1] += 1 

    def substituition(self,set_index,set_tag):
        algo = self.algorithm
        if algo == "r":
            self.random_replace(set_index,set_tag)
        if algo == "l":
            self.lru_replace(set_index,set_tag) 
        if algo == "f":
            self.fifo_replace(set_index,set_tag)

    def simulate_cache_access(self, memory_address):
        self.acess += 1
        offset_bits = int(math.log2(self.b_size))
        index_bits = int(math.log2(self.n_sets))
        tag_bits = self.address_bits - offset_bits - index_bits
        
        set_index = (memory_address >> offset_bits) % self.n_sets
        set_tag = (memory_address >> offset_bits)
        
        block_found = False
        for block in self.cache[set_index]:
            if block == set_tag:
                block_found = True
                break
        
        if block_found:
            self.hits += 1
        else:
            self.misses += 1
            if self.cache[set_index][0] is None:
                self.compulsory_misses += 1
            self.unique_blocks_referenced.add(set_tag)
            if self.assoc == 1:
                self.cache[set_index][0] = set_tag
            else:
                self.substituition(set_index,set_tag)

    def calcular_miss_capacidade(self):
        total_unique_blocks = len(self.unique_blocks_referenced)
        total_misses_capacidade = max(0, total_unique_blocks - (self.n_sets * self.assoc))
        
        if self.acess == 0:
            return 0
        return total_misses_capacidade / self.acess

    def imprime(self):
        print("access number:", self.acess)
        print("hit rate: {:.4f}".format(self.hits / self.acess))
        print("miss rate: {:.4f}".format(self.misses / self.acess))
        print("compulsory miss rate: {:.4f}".format(self.compulsory_misses / self.acess))
        print("capacity miss rate: {:.4f}".format(self.calcular_miss_capacidade()))

""""
c = Cache(assoc=2, n_sets=4, address_bits=16, b_size=4,algorithm="l")

c.simulate_cache_access(0x1234)
c.simulate_cache_access(0xABCD)
c.simulate_cache_access(0x5678)
c.simulate_cache_access(0x1234)
c.simulate_cache_access(0x1234)

c.imprime()


# Criar uma instância do simulador de cache
simulador_cache = CacheSimulator(assoc=2, n_sets=4, address_bits=16, b_size=4)

# Simular acesso à cache
simulador_cache.simulate_cache_access(0x1234)
simulador_cache.simulate_cache_access(0xABCD)
simulador_cache.simulate_cache_access(0x5678)
simulador_cache.simulate_cache_access(0x1234)
simulador_cache.simulate_cache_access(0x1234)

# Criar uma instância da classe CacheSimulator
#cache_sim = CacheSimulator(assoc=1, n_sets=64, address_bits=32, b_size=16)

# Simular acessos à memória
#cache_sim.simulate_cache_access(0x4B0)
"""