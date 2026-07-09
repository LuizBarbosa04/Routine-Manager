import tkinter as tk

janela = tk.Tk()

janela.title("Routine Manager")

janela.state("zoomed")

janela.configure(bg="#F5F5F5")

frame_principal = tk.Frame(
    janela,
    bg="white",
    padx=20,
    pady=20
)

frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

titulo = tk.Label(
    frame_principal,
    text="Compromissos",
    font=("Sagoe UI", 22, "bold"),
    bg="white"
)

titulo.pack(anchor="w")

lista_compromissos = tk.Frame(
    frame_principal,
    bg="white"
)

lista_compromissos.pack(
    fill="both",
    expand=True,
    pady=20
)

barra_botoes = tk.Frame(
    frame_principal,
    bg="white"
)

barra_botoes.pack(fill="x")

botao_adicionar = tk.Button(
    barra_botoes,
    text="Adicionar",
    width=15
)

botao_remover = tk.Button(
    barra_botoes,
    text="Remover",
    width=15
)

botao_marcar = tk.Button(
    barra_botoes,
    text="Marcar como feito",
    width=18
)

botao_excel = tk.Button(
    barra_botoes,
    text="Gerar planilha",
    width=15
)

botao_adicionar.pack(side="left", padx=5)

botao_remover.pack(side="left", padx=5)

botao_marcar.pack(side="left", padx=5)

botao_excel.pack(side="left", padx=5)


janela.mainloop()