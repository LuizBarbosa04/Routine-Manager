import tkinter as tk

from screens.home import Home

janela = tk.Tk()

janela.title("Routine Manager")
janela.state("zoomed")
janela.configure(bg="#F5F5F5")

Home(janela)

janela.mainloop()