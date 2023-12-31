import tkinter as tk
from tkinter import ttk
import random
import string

class GeradorSenhaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senha")

        self.tamanho_label = ttk.Label(root, text="Tamanho da Senha:")
        self.tamanho_label.grid(row=0, column=0, padx=10, pady=10)

        self.tamanho_entry = ttk.Entry(root, width=5)
        self.tamanho_entry.grid(row=0, column=1, padx=10, pady=10)

        self.gerar_button = ttk.Button(root, text="Gerar Senha", command=self.gerar_senha)
        self.gerar_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.senha_var = tk.StringVar()
        self.senha_label = ttk.Label(root, textvariable=self.senha_var, font=("Courier", 12))
        self.senha_label.grid(row=2, column=0, columnspan=2, pady=10)

    def gerar_senha(self):
        tamanho = int(self.tamanho_entry.get())
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        self.senha_var.set(senha)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorSenhaApp(root)
    root.mainloop()