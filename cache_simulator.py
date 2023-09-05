import sys
from openBinary import openBinary
from cache import Cache

# Argumentos definidos por padrão para testesW
sys.argv.append(1)
sys.argv.append(4)
sys.argv.append(32)
sys.argv.append('l')
sys.argv.append(1)
sys.argv.append('vortex.in.sem.persons.bin')

def main():
	if (len(sys.argv) != 7):
		print("Numero de argumentos incorreto. Utilize:")
		print("python cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flag_saida> arquivo_de_entrada")
		exit(1)
	
	nsets = sys.argv[1]
	bsize = sys.argv[2]
	assoc = sys.argv[3]
	subst = sys.argv[4]
	flagOut = sys.argv[5]
	arquivoEntrada = sys.argv[6]

	C = Cache(nsets,bsize,assoc,subst,flagOut,arquivoEntrada)

	print("Argumentos passados")
	print("nsets =", nsets)
	print("bsize =", bsize)
	print("assoc =", assoc)
	print("subst =", subst)
	print("flagOut =", flagOut)
	print("arquivo =", arquivoEntrada)

	# Seu codigo vai aqui
	addresses = openBinary(arquivoEntrada)

	for end in addresses:
		C.simulate_cache_access(int(end))

	C.imprime()


if __name__ == '__main__':
	main()