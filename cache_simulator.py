import sys
from openBinary import openBinary
from cache import Cache
from interface import *
from time import sleep

# Argumentos definidos por padrão para testesW
"""
sys.argv.append(256)
sys.argv.append(4)
sys.argv.append(4)
sys.argv.append('f')
sys.argv.append(0)
sys.argv.append('vortex.in.sem.persons.bin')
"""
def main():
	C = Cache
	if (len(sys.argv) > 1 and len(sys.argv) < 7):
		print("Numero de argumentos incorreto. Utilize:")
		print("python cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flag_saida> arquivo_de_entrada")
		exit(1)
	else:
		if (len(sys.argv) == 7):
			if sys.argv[5] == 1: # Flag 1 Saída Padrão
				C = Cache(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[6])
				for end in openBinary(C.address_bits):
					C.simulate_cache_access(end)
				data = C.getData()
				print(f'{C.getAcess()} {data[0]:.2f} {data[1]:.2f} {data[2]:.2f} {data[2]:.2f}')
		else:  # Flag 0 Formato Livre
			values = []
			elements = []
			GUI = sg.Window("Cache Simulator AOC II").layout(layout)
			while True:
				event, inputs = GUI.Read()
				if event == 'Adicionar':
					values.append(int(inputs['n_sets']))
					values.append(int(inputs['b_size']))
					values.append(int(inputs['assoc']))
					values.append(inputs['alg'])
					values.append(inputs['combo'])
					C = Cache(*values)
					for end in openBinary(C.address_bits):
						C.simulate_cache_access(end)
					for i in inputs: elements.append(GUI.find_element(i))
					for e in elements: e.update('')
					G = Graph(C.getData(),C.getAcess(),C.getCacheInfo())
					G.plot()
					values.clear()
		
if __name__ == '__main__':
	main()
