import PySimpleGUI as sg
import matplotlib.pyplot as plt

layout = [
		[sg.Text('Numero de conjuntos:       '),sg.Input(size=(20,0),key='n_sets')],
		[sg.Text('Tamanho do bloco:           '),sg.Input(size=(20,0),key='b_size')],
		[sg.Text('Associtividade:                 '),sg.Input(size=(20,0),key='assoc')],
		[sg.Text('Substituição [l,r,f]:            '),sg.Input(size=(20,0),key='alg')],
		[sg.Text('Arquivo:'),sg.Combo(['bin_100.bin','bin_1000.bin','bin_10000.bin','vortex.in.sem.persons.bin'],key='combo',size=(30,0))],
		[sg.Button('Adicionar')]
	]
	
class Graph:
    def __init__(self,values,acess,cacheInfo):
        self.names = ['Hits','Miss','Misses Compulsórios','Misses capacidade','Misses conflito']
        self.values = values
        self.title = cacheInfo
        self.acess = acess
    
    def plot(self):
        fig, xy = plt.subplots()
        xy.bar(self.names,self.values)
        xy.set_title(f"""{self.title}
Total de acessos = {self.acess:.4f}     Hits = {self.values[0]:.4f}     Misses = {self.values[1]:.4f} 
Misses Compulsórios = {self.values[2]:.4f}     Misses de Capacidade = {self.values[3]:.4f}     Misses Conflito = {self.values[4]}""")
        fig.set_size_inches(8,6)
        plt.show()