import tkinter as tk
import random
from PIL import Image, ImageTk

def aleatorio():
    global photo 
    numero = random.randint(1, 6)
    image_caminho = f'C:\\Programas\\dado{numero}.jpg'
    image = Image.open(image_caminho)
    photo = ImageTk.PhotoImage(image)  
    label.config(image=photo)

aba = tk.Tk()
aba.geometry('500x300')
aba.title('Bloco')

quadrado = tk.Frame(aba, bg="#ffffff", padx=100, pady=50)
quadrado.pack(pady=40)

image_caminho = "C:\\Programas\\dado6.jpg"
image = Image.open(image_caminho)
photo = ImageTk.PhotoImage(image)

botao = tk.Button(quadrado, text="Rolar o dado", command=aleatorio, bg="#4163f8",font=('Arial', 10),fg='white',width=12)
botao.grid(column=1, row=1, columnspan=2)


label = tk.Label(quadrado, image=photo)
label.grid(row=0, column=1,columnspan=2)

aba.mainloop()
