class Scache:
    def __init__(self, nsets, bsize,assoc):
        self.nsets = nsets
        self.bsize = bsize
        self.assoc = assoc
    def printedee(self):
        print(f'{self.nsets} está aceler.')
#criar objeto 
cache1 = Scache(256,8,1)
cache2 = Scache(256,8,2)

#print da cache
cache1.printedee()
       
