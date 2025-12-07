import tkinter as tk
from tkinter import ttk
from translate import Translator

langs = {
    "Inglés": "en", "Español": "es", "Francés": "fr", 
    "Alemán": "de", "Italiano": "it", "Portugués": "pt", "Japonés": "ja"
}

def traducer():
    try:
        code = langs[combo.get()]
        res = Translator(from_lang="autodetect", to_lang=code).translate(entry.get())
        lbl_res.config(text=res)
    except:
        lbl_res.config(text="Error")

root = tk.Tk()
root.title("Traductor")
root.geometry("300x250")

tk.Label(root, text="Texto:").pack()
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Label(root, text="Idioma a traducir:").pack()
combo = ttk.Combobox(root, values=list(langs.keys()), state="readonly")
combo.current(0)
combo.pack(pady=5)

tk.Button(root, text="Traducir", command=traducer).pack(pady=10)

lbl_res = tk.Label(root, text="...", font=("Arial", 12), wraplength=280)
lbl_res.pack(pady=10)

root.mainloop()
