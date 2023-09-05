import PySimpleGUI as sg
import matplotlib.pyplot as plt

class Interface:
	def __init__(self):
		layout = [
			[sg.Text('Numero de conjuntos:'),sg.Input(size=(10,0),key='n_sets')],
			[sg.Text('Tamanho do bloco:    '),sg.Input(size=(10,0),key='b_size')],
			[sg.Text('Associtividade:          '),sg.Input(size=(10,0),key='assoc')],
			[sg.Text('Substituição [l,r,f]:     '),sg.Input(size=(10,0),key='alg')],
			[sg.Text('Flag:'),sg.Radio("0","flag", key="flag_0"), sg.Radio("1", "RADIO1", key="flag_1")],
			[sg.Text('Arquivo:'),sg.Combo(['bin_100.bin','bin_1000.bin','bin_10000.bin','vortex.in.sem.persons.bin'],key='combo',size=(20,0))],
			[sg.Button('Enviar Dados')]
		]
		window = sg.Window("AOC II Andersson De Souza e Franklin Sales").layout(layout)
		self.button, self.values = window.Read()

	def parameters(self):
		n_sets = self.values['n_sets']
		b_size = self.values['b_size']
		assoc = self.values['assoc']
		alg = self.values['alg']
		flag = bool
		file = self.values['combo']
		if self.values['flag_1'] == True:
			flag = 1
		else: flag = 0
		return n_sets,b_size,assoc,alg,flag,file
	
class Graph:
    def __init__(self,names,values,acess,title):
        self.names = names
        self.values = values
        self.title = title
        self.acess = acess
    
    def plot(self):
        fig, xy = plt.subplots()
        xy.bar(self.names,self.values)
        xy.set_title(f"""{self.title}
Total de acessos = {self.acess:.4f}     Hits = {self.values[0]:.4f}     Misses = {self.values[1]:.4f} 
Misses Compulsórios = {self.values[2]:.4f}     Misses de Capacidade = {self.values[3]:.4f}""")
        fig.set_size_inches(8,6)
        plt.show()