import tkinter as tk
from tkinter import filedialog

def abrir_arquivo():
    filepath = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            texto.delete("1.0", tk.END)
            texto.insert(tk.END, content)

def copiar_paragrafo(event):
    index = texto.index(tk.CURRENT)
    start = texto.search("\n\n", index, backwards=True, stopindex="1.0")
    if start == "":
        start = "1.0"
    else:
        start = texto.index(f"{start}+1c")
    end = texto.search("\n\n", index, stopindex=tk.END)
    if end == "":
        end = tk.END
    paragrafo = texto.get(start, end)
    root.clipboard_clear()
    root.clipboard_append(paragrafo)

def iniciar_selecao(event):
    texto.tag_add("selecao", "current linestart", "current lineend+1c")

def encerrar_selecao(event):
    texto.tag_remove("selecao", "1.0", tk.END)

root = tk.Tk()
root.title("Copiar Parágrafo")

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

texto = tk.Text(root, wrap="word", yscrollcommand=scrollbar.set)
texto.pack(expand=True, fill="both")

scrollbar.config(command=texto.yview)

texto.bind("<Enter>", iniciar_selecao)
texto.bind("<Leave>", encerrar_selecao)
texto.bind("<Button-1>", copiar_paragrafo)

abrir_button = tk.Button(root, text="Abrir Arquivo", command=abrir_arquivo)
abrir_button.pack(pady=5)

root.mainloop()
