import sys
import math
import random

class CACHE:
    def __init__(self):
        self.tag = 0
        self.is_empty = True
        self.inserted_at = 0
        self.access_at = 0

def associative(file, n_ways, n_sets, n_bits_offset, n_bits_index, flag_out, subst):
    access_number = 0
    compulsory_miss = 0
    hit = 0
    capacity_miss = 0
    conflict_miss = 0

    cache = [[CACHE() for _ in range(n_ways)] for _ in range(n_sets)]

    with open(file, "rb") as file_handle:
        while True:
            temp_char = file_handle.read(1)
            if not temp_char:
                break

            access_number += 1
            address = int.from_bytes(temp_char, byteorder='big')

            for _ in range(3):
                temp_char = file_handle.read(1)
                address = (address << 8) | int.from_bytes(temp_char, byteorder='big')

            tag = address >> (n_bits_offset + n_bits_index)
            index = (address & ((1 << n_bits_index) - 1) << n_bits_offset) >> n_bits_offset

            way = 0
            is_found = False

            while n_ways > way and not is_found:
                if cache[index][way].is_empty:
                    cache[index][way].tag = tag
                    cache[index][way].is_empty = False
                    cache[index][way].inserted_at = access_number
                    cache[index][way].access_at = access_number
                    compulsory_miss += 1
                    is_found = True
                elif cache[index][way].tag == tag:
                    hit += 1
                    cache[index][way].access_at = access_number
                    is_found = True
                else:
                    way += 1

            if not is_found:
                cache_space_free = sum(1 for row in cache for block in row if block.is_empty)

                if cache_space_free > 0:
                    conflict_miss += 1
                else:
                    capacity_miss += 1

                if subst == 'R':
                    randomReplacement(cache, n_ways, index, tag, access_number)
                if subst == 'F':
                    fifoReplacement(cache, n_ways, index, tag, access_number)
                if subst == 'L':
                    lruReplacement(cache, n_ways, index, tag, access_number)

    getStatistics(flag_out, access_number, compulsory_miss, hit, capacity_miss, conflict_miss)
    deallocateCache(cache, n_sets)

def randomReplacement(c, n_ways, index, tag, access_number):
    random_number = random.randint(0, n_ways - 1)
    c[index][random_number].tag = tag
    c[index][random_number].is_empty = False
    c[index][random_number].inserted_at = access_number
    c[index][random_number].access_at = access_number

def fifoReplacement(c, n_ways, index, tag, access_number):
    count = 0
    for i in range(1, n_ways):
        if c[index][i].inserted_at < c[index][count].inserted_at:
            count = i

    c[index][count].tag = tag
    c[index][count].is_empty = False
    c[index][count].inserted_at = access_number
    c[index][count].access_at = access_number

def lruReplacement(c, n_ways, index, tag, access_number):
    count = 0
    for i in range(1, n_ways):
        if c[index][i].access_at < c[index][count].access_at:
            count = i

    c[index][count].tag = tag
    c[index][count].is_empty = False
    c[index][count].inserted_at = access_number
    c[index][count].access_at = access_number

def getStatistics(output_flag, access_number, compulsory_miss, hit, capacity_miss, conflict_miss):
    hit_rate = hit / access_number
    miss_rate = (compulsory_miss + capacity_miss + conflict_miss) / access_number
    compulsory_miss_rate = (compulsory_miss / miss_rate) / access_number
    capacity_miss_rate = (capacity_miss / miss_rate) / access_number
    conflict_miss_rate = (conflict_miss / miss_rate) / access_number

    if output_flag == 0:
        print("Access number:", access_number)
        print("Hit rate:", format(hit_rate, '.2f'))
        print("Miss rate:", format(miss_rate, '.2f'))
        print("Compulsory miss rate:", format(compulsory_miss_rate, '.2f'))
        print("Capacity miss rate:", format(capacity_miss_rate, '.2f'))
        print("Conflict miss rate:", format(conflict_miss_rate, '.2f'))
    else:
        print(access_number, format(hit_rate, '.2f'), format(miss_rate, '.2f'),
              format(compulsory_miss_rate, '.2f'), format(capacity_miss_rate, '.2f'),
              format(conflict_miss_rate, '.2f'))

def deallocateCache(c, n_sets):
    if c is not None:
        for i in range(n_sets):
            del c[i]
        del c

if __name__ == "__main__":
    n_sets = int(sys.argv[1])
    b_size = int(sys.argv[2])
    assoc = int(sys.argv[3])
    subst = sys.argv[4]
    flag_out = int(sys.argv[5])
    filename = sys.argv[6]

    n_bits_offset = int(math.log2(b_size))
    n_bits_index = int(math.log2(n_sets))

    associative(filename, assoc, n_sets, n_bits_offset, n_bits_index, flag_out, subst)
