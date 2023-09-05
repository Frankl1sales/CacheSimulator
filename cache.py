#criar a classe cache
import math
import random
from functools import lru_cache
from collections import OrderedDict

class Cache:
    def __init__(self, n_sets, b_size, assoc, algorithm, flagOut, address_bits):
        self.assoc = assoc
        self.n_sets = n_sets
        self.address_bits = address_bits
        self.b_size = b_size
        self.cache = [[None for _ in range(self.assoc)] for _ in range(self.n_sets)]
        self.algorithm = algorithm.lower()
        self.flagOut = flagOut

        self.hits = 0
        self.misses = 0
        self.acess = 0
        self.compulsory_misses = 0
        self.unique_blocks_referenced = set()  # Conjunto de blocos únicos referenciados
        self.buffer = [[] for _ in range(self.n_sets)]  # Lista vazia para cada conjunto
        self.lru_buffers = [OrderedDict() for _ in range(self.n_sets)]

    def simulate_cache_access(self, memory_address):
        self.acess += 1
        offset_bits = int(math.log2(self.b_size))
        index_bits = int(math.log2(self.n_sets))
        #unsupported operand type(s) for -: 'str' and 'int'
        #tag_bits = self.address_bits - offset_bits - index_bits
        
        set_index = (memory_address >> offset_bits) % self.n_sets
        set_tag = (memory_address >> offset_bits)
        
        block_found = False
        for block in self.cache[set_index]:
            if block is not None and block == set_tag:
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
    
    def random_replace(self, set_index, set_tag):
        random_block_index = random.randint(0, self.assoc - 1)
        self.cache[set_index][random_block_index] = set_tag

    def lru_replace(self, set_index, set_tag):
        # Verifica se o conjunto está vazio (todos os blocos são None)
        if any(block is None for block in self.cache[set_index]):
            # Se o conjunto não está vazio, encontramos o bloco LRU
            # com base no buffer que armazena as idades.
            lru_block_index = list(self.lru_buffers[set_index].keys())[0] if self.lru_buffers[set_index] else 0
        else:
            # Caso contrário, o conjunto está vazio e todos os blocos estão ocupados
            # Procura o primeiro bloco vazio no conjunto
            for block_index, block in enumerate(self.cache[set_index]):
                if block is None:
                    lru_block_index = block_index
                    break

            # Caso não encontre nenhum bloco vazio, retorna
            if lru_block_index is None:
                return

        # Substitui o bloco LRU ou o bloco None pela nova tag
        self.cache[set_index][lru_block_index] = set_tag
        # Atualiza o buffer LRU com o bloco mais recente
        if 0 <= lru_block_index < len(self.lru_buffers[set_index]):
            self.lru_buffers[set_index].move_to_end(lru_block_index)


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
            self.cache[0][set_index] = set_tag
            self.buffer.append(set_index)
            self.buffer.append(1) # Marca a prox pos de preenchimento
            return
        # verifica se ta no final da fila, procura no buffer e zera a posição
        if self.searchBuffer(set_index) == self.b_size:
            for c in range(0,len(self.buffer),2):
                if self.buffer[c] == set_index:
                    self.buffer[c+1] = 0
        # add na pos de preenchimento
        self.cache[self.searchBuffer(set_index)][set_index] = set_tag
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


'''
c = Cache(assoc=2, n_sets=4, address_bits=16, b_size=4,algorithm="r")

c.simulate_cache_access(0x1234)
c.simulate_cache_access(0xABCD)
c.simulate_cache_access(0x5678)
c.simulate_cache_access(0x1234)
c.simulate_cache_access(0x1234)

c.imprime()
'''


"""
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