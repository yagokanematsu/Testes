import tkinter as tk

def podio():
    try:
        valor1 = int(nome.get())
        valor2 = int(nome1.get())
        valor3 = int(nome2.get())
    except ValueError:
        return 

    tempos = [(valor1, 0), (valor2, 1), (valor3, 2)]
    tempos.sort()
    real = []
    for gg in range(3):
        real.append(tempos[gg][1])
    real = list(map(lambda x: x+1, real))

    for i, resu in enumerate([resultado, resultado1, resultado2]):
        for t in [nome3, nome4, nome5]:
            t.config(state='normal')
        resu.set(f"{real[i]}°")
    for f in [nome3, nome4, nome5]:
        f.config(state="readonly")

aba = tk.Tk()
aba.title("Medalhas")
aba.call('tk', 'scaling', 3.0)
aba.geometry('800x500')
aba.configure(bg="#f0f0f0")

quadrado = tk.Frame(aba, bg="#ffffff", padx=100, pady=20)
quadrado.pack(pady=20)

texto = tk.Label(quadrado, text='Tempo 1:', font=("helvetica", 12), bg="#ffffff")
texto.grid(row=1, column=0, padx=10, pady=10)

texto1 = tk.Label(quadrado, text='Tempo 2:', font=("helvetica", 12), bg="#ffffff")
texto1.grid(row=2, column=0, padx=10, pady=10)

texto2 = tk.Label(quadrado, text='Tempo 3:', font=("helvetica", 12), bg="#ffffff")
texto2.grid(row=3, column=0, padx=10, pady=10)

nome = tk.Entry(quadrado, font=("helvetica", 12), width=10)
nome.grid(row=1, column=1, padx=10, pady=10)

nome1 = tk.Entry(quadrado, font=("helvetica", 12), width=10)
nome1.grid(row=2,column=1,   padx=10, pady=10)

nome2 = tk.Entry(quadrado, font=("helvetica", 12), width=10)
nome2.grid(row=3, column=1, padx=10, pady=10)

texto3 = tk.Label(quadrado, text='Posição:', font=("helvetica", 12), bg="#ffffff")
texto3.grid(row=0, column=2, padx=10, pady=10)

resultado, resultado1, resultado2 = tk.StringVar(), tk.StringVar(), tk.StringVar()

nome3 = tk.Entry(quadrado, font=("helvetica", 12),textvariable=resultado, width=5, justify="center", state="readonly")
nome3.grid(row=1, column=2, padx=10, pady=10)

nome4 = tk.Entry(quadrado, font=("helvetica", 12),textvariable=resultado1, width=5,justify="center", state="readonly")
nome4.grid(row=2, column=2, padx=10, pady=10)

nome5 = tk.Entry(quadrado, font=("helvetica", 12), textvariable=resultado2, width=5,justify="center", state="readonly")
nome5.grid(row=3, column=2, padx=10, pady=10)

botao = tk.Button(quadrado, text='Calcular', font=("helvetica", 12), bg="#3b814b", fg="white", command=podio, width=15)
botao.grid(row=4, column=0, columnspan=3, pady=20)

aba.mainloop()
