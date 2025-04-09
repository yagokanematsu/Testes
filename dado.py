import tkinter as tk
import random
from PIL import Image, ImageTk

def aleatorio():
    global foto
    numero = random.randint(1, 6)
    imagem_caminho = f'C:\\Programas\\media\\dado{numero}.jpg'
    imagem = Image.open(imagem_caminho)
    foto = ImageTk.PhotoImage(imagem)  
    espaco.config(image=foto)

aba = tk.Tk()
aba.geometry('300x300')
aba.title('Dado')

quadrado = tk.Frame(aba, padx=100, pady=50)
quadrado.pack(pady=40)

imagem_caminho = "C:\\Programas\\media\\branco.jpg"
imagem = Image.open(imagem_caminho)
foto = ImageTk.PhotoImage(imagem)

botao = tk.Button(quadrado, text="Rolar o dado", command=aleatorio, bg="#4163f8",font=('Arial', 10),fg='white',width=12)
botao.grid(column=1, row=1, columnspan=2)


espaco = tk.Label(quadrado, image=foto)
espaco.grid(row=0, column=1,columnspan=2)

aba.mainloop()
