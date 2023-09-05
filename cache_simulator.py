import sys
from openBinary import openBinary
from cache import Cache
from interface import *

# Argumentos definidos por padrão para testesW
sys.argv.append(1)
sys.argv.append(4)
sys.argv.append(32)
sys.argv.append('l')
sys.argv.append(1)
sys.argv.append('vortex.in.sem.persons.bin')

def main():
	values = []
	C = Cache
	if len(sys.argv) > 1: # caso tenha argumentos roda sem GUI
		if (len(sys.argv) != 7):
			print("Numero de argumentos incorreto. Utilize:")
			print("python cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flag_saida> arquivo_de_entrada")
			exit(1)
		else:
			nsets = sys.argv[1]
			bsize = sys.argv[2]
			assoc = sys.argv[3]
			subst = sys.argv[4]
			flagOut = sys.argv[5]
			inputFile = sys.argv[6]
	else: # sem argumentos coleta os dados com a GUI
		GUI = Interface()
		values = GUI.parameters()
		nsets = int(values[0])
		bsize = int(values[1])
		assoc = int(values[2])
		subst = values[3]
		flagOut = int(values[4])
		inputFile = values[5]
	
	C = Cache(nsets,bsize,assoc,subst,flagOut,inputFile)

	# Seu codigo vai aqui
	addresses = openBinary(inputFile)
	for end in addresses:
		C.simulate_cache_access(int(end))
	C.imprime()

	cacheInfo = f'Cache {nsets} Conjuntos, Tamanho de bloco {bsize} ,Associatividade {assoc}, Algoritmo {subst}'
	labels = ['Hits','Miss','Misses Compulsórios','Misses capacidade']
	cacheData = C.getData()

	print(cacheData)
	G = Graph(labels,cacheData,C.getAcess(),cacheInfo)
	G.plot()


if __name__ == '__main__':
	main()
