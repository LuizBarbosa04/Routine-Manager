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

janela.mainloop()