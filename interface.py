import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario_digitado = usuario_entry.get()
    senha_digitada = senha_entry.get()

    # Verificação de usuário e senha (exemplo simples)
    if usuario_digitado == "usuario" and senha_digitada == "senha":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

# Criar a janela
janela = tk.Tk()
janela.title("Login")

# Labels e Entries usando o gerenciador de layout grid
usuario_label = tk.Label(janela, text="Usuário:")
usuario_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
usuario_entry = tk.Entry(janela)
usuario_entry.grid(row=0, column=1, padx=10, pady=5)

senha_label = tk.Label(janela, text="Senha:")
senha_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
senha_entry = tk.Entry(janela, show="*")
senha_entry.grid(row=1, column=1, padx=10, pady=5)

# Botão de login
login_button = tk.Button(janela, text="Login", command=verificar_login)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Ajustar o tamanho das colunas para que os elementos fiquem alinhados
janela.grid_columnconfigure(0, minsize=100)
janela.grid_columnconfigure(1, minsize=150)

# Iniciar a interface
janela.mainloop()

