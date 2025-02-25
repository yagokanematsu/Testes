import tkinter as tk
def quadrante():
    try:
        x1 = float(x.get())
        y1 = float(y.get())
    except ValueError:
        pass

    if x1 == 0 and y1 == 0:
        res.config(state='normal')
        resultado.set('Origem')
        res.config(state="readonly")

    elif x1 == 0:
        res.config(state='normal')
        resultado.set('Eixo X')
        res.config(state="readonly")

    elif y1 == 0:
        res.config(state='normal')
        resultado.set('Eixo Y')
        res.config(state="readonly")

    elif x1>0 and y1>0:
        res.config(state='normal')
        resultado.set('Quadrante 1')
        res.config(state="readonly")

    elif x1>0 and y1<0:
        res.config(state='normal')
        resultado.set('Quadrante 4')
        res.config(state="readonly")

    elif x1<0 and y1<0:
        res.config(state='normal')
        resultado.set('Quadrante 3')
        res.config(state="readonly")

    elif x1<0 and y1>0:
        res.config(state='normal')
        resultado.set('Quadrante 2')
        res.config(state="readonly")

aba = tk.Tk()
aba.call('tk', 'scaling', 3.0)
aba.title('Coordenadas de um ponto')
aba.geometry('800x400')

quadrado = tk.Frame(aba, bg="#ffffff", padx=20, pady=20, border=20)
quadrado.pack(pady=40)

texto = tk.Label(quadrado, text='Informe a coordenada X:', font=('helvetica', 10), bg='#ffffff')
texto.grid(row=0, column=0,padx=10,pady=10)
texto1 = tk.Label(quadrado, text='Informe a coordenada Y:',font=('helvetica', 10), bg='#ffffff')
texto1.grid(row=1, column=0,padx=10,pady=10)
texto2 = tk.Label(quadrado, text='O ponto é pertecente ao',font=('helvetica', 10), bg='#ffffff')
texto2.grid(row=3, column=0,padx=10,pady=10)

x=tk.Entry(quadrado,width=10, justify='center',font=('helvetica', 10))
x.grid(row=0,column=1,padx=10,pady=10)

y=tk.Entry(quadrado,width=10, justify='center',font=('helvetica', 10))
y.grid(row=1,column=1,padx=10,pady=10)
resultado = tk.StringVar()
res=tk.Entry(quadrado,width=10, textvariable= resultado, justify='center', state='readonly', bg='#1f1f1f', font=('helvetica',10))
res.grid(row=3,column=1,padx=10,pady=10)

botao = tk.Button(quadrado,text='Encontrar posição', font=('helvetica',10), bg='#3b814b', fg='#ffffff', command= quadrante)
botao.grid(row=2,column=0, columnspan=2)

aba.mainloop()
