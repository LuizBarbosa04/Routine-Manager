import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from database.database import Database



class Home:

    def __init__(self, janela):

        self.janela = janela

        self.db = Database()

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

        self.tabela = ttk.Treeview(
            self.frame_principal,
            columns=("Compromisso",),
            show="headings",
            height=20
        )

        self.tabela.heading(
            "Compromisso",
            text="Compromissos"
        )

        self.tabela.column(
            "Compromisso",
            width=900
        )

        self.tabela.pack(
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
            width=15,
            command=self.remover_compromisso
        )

        self.botao_remover.pack(side="left", padx=5)

        self.botao_marcar = tk.Button(
            self.barra_botoes,
            text="Marcar como feito",
            width=18,
            command=self.concluir_compromisso
        )

        self.botao_marcar.pack(side="left", padx=5)

        self.botao_excel = tk.Button(
            self.barra_botoes,
            text="Gerar planilha",
            width=15
        )

        self.botao_excel.pack(side="left", padx=5)

        self.carregar_compromissos()

    def carregar_compromissos(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        compromissos = self.db.listar_compromissos()

        for compromisso in compromissos:

            self.tabela.insert(
                "",
                "end",
                iid=compromisso[0],
                values=(compromisso[1],)
            )

    def adicionar_compromisso(self):

        nome = simpledialog.askstring(
            "Novo compromisso",
            "Digite o nome do compromisso:"
        )

        if nome:

           self.db.adicionar_compromisso(nome)

           self.carregar_compromissos()
            
    def remover_compromisso(self):

        selecionado = self.tabela.selection()

        if not selecionado:
            return
        
        id_compromisso = int(selecionado[0])

        self.db.remover_compromisso(id_compromisso)

        self.carregar_compromissos()

    def concluir_compromisso(self):

        selecionado = self.tabela.selection()

        if not selecionado:
            return
        
        id_compromisso = int(selecionado[0])

        self.db.registrar_conclusao(id_compromisso)