import matplotlib.pyplot as plt
import numpy as np

# Dados para o primeiro conjunto de pontos
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)

# Dados para o segundo conjunto de pontos
x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2)

# Criar o gráfico
plt.figure(figsize=(10, 5))

# Plotar os pontos do primeiro conjunto de dados
plt.plot(x1, y1, label='Seno')

# Plotar os pontos do segundo conjunto de dados
plt.plot(x2, y2, label='Cosseno', linestyle='dashed')

# Adicionar rótulos aos eixos e título ao gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Dois Gráficos em um')

# Adicionar uma legenda
plt.legend()

# Mostrar o gráfico
plt.show()