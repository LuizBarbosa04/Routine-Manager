import tkinter as tk
from tkinter import simpledialog


class Home:

    def __init__(self, janela):

        self.janela = janela

        self.compromissos = []

        self.frame_principal = tk.Frame(
            self.janela,
            bg="white",
            padx=20,
            pady=20
        )

        self.frame_principal.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.titulo = tk.Label(
            self.frame_principal,
            text="Compromissos",
            font=("Segoe UI", 22, "bold"),
            bg="white"
        )

        self.titulo.pack(anchor="w")

        self.lista_compromissos = tk.Frame(
            self.frame_principal,
            bg="white"
        )

        self.lista_compromissos.pack(
            fill="both",
            expand=True,
            pady=20
        )

        self.barra_botoes = tk.Frame(
            self.frame_principal,
            bg="white"
        )

        self.barra_botoes.pack(fill="x")

        self.botao_adicionar = tk.Button(
            self.barra_botoes,
            text="Adicionar",
            width=15,
            command=self.adicionar_compromisso
        )

        self.botao_adicionar.pack(side="left", padx=5)

        self.botao_remover = tk.Button(
            self.barra_botoes,
            text="Remover",
            width=15
        )

        self.botao_remover.pack(side="left", padx=5)

        self.botao_marcar = tk.Button(
            self.barra_botoes,
            text="Marcar como feito",
            width=18
        )

        self.botao_marcar.pack(side="left", padx=5)

        self.botao_excel = tk.Button(
            self.barra_botoes,
            text="Gerar planilha",
            width=15
        )

        self.botao_excel.pack(side="left", padx=5)

    def atualizar_lista(self):

        for widget in self.lista_compromissos.winfo_children():
            widget.destroy()

        for compromisso in self.compromissos:

            texto = tk.Label(
                self.lista_compromissos,
                text="☐ " + compromisso,
                font=("Segoe UI", 14),
                bg="white",
                anchor="w"
            )

            texto.pack(fill="x", pady=2)

    def adicionar_compromisso(self):

        nome = simpledialog.askstring(
            "Novo compromisso",
            "Digite o nome do compromisso:"
        )

        if nome:
            self.compromissos.append(nome)
            self.atualizar_lista()