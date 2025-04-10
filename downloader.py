import tkinter as tk
from tkinter import ttk
import yt_dlp

COR_FUNDO = "#66d575" 
COR_TEXTO = "black"
COR_BOTAO = "#057ed6" 
COR_BOTAO_HOVER = "#a5d6ff" 

def estilizar_botao(botao):
    botao.config(bg=COR_BOTAO, fg=COR_TEXTO, font=("Arial", 12), relief="raised", bd=3)
    botao.bind("<Enter>", lambda e: botao.config(bg=COR_BOTAO_HOVER))
    botao.bind("<Leave>", lambda e: botao.config(bg=COR_BOTAO))

def baixar_mp3():
    def download_mp3():
        link = url.get()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

    nova_janela = tk.Toplevel(aba, bg=COR_FUNDO)
    nova_janela.title("Baixar MP3")
    nova_janela.geometry("350x200")

    ttk.Label(nova_janela, text="Digite a URL do vídeo:", background=COR_FUNDO, foreground=COR_TEXTO, font=("Arial", 12)).pack(pady=10)
    url = ttk.Entry(nova_janela, width=40)
    url.pack(pady=5)

    botao_baixar = tk.Button(nova_janela, text="Baixar MP3", command=download_mp3)
    estilizar_botao(botao_baixar)
    botao_baixar.pack(pady=10)

    botao_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
    estilizar_botao(botao_fechar)
    botao_fechar.pack(pady=5)

def baixar_mp4():
    def download_mp4():
        link = url.get()
        opcoes = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        }
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([link])

    nova_janela = tk.Toplevel(aba, bg=COR_FUNDO)
    nova_janela.title("Baixar MP4")
    nova_janela.geometry("350x200")

    ttk.Label(nova_janela, text="Digite a URL do vídeo:", background=COR_FUNDO, foreground=COR_TEXTO, font=("Arial", 12)).pack(pady=10)
    url = ttk.Entry(nova_janela, width=40)
    url.pack(pady=5)

    botao_baixar = tk.Button(nova_janela, text="Baixar MP4", command=download_mp4)
    estilizar_botao(botao_baixar)
    botao_baixar.pack(pady=10)

    botao_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
    estilizar_botao(botao_fechar)
    botao_fechar.pack(pady=5)

aba = tk.Tk()
aba.title("YouTube Downloader")
aba.geometry("400x300")
aba.config(bg=COR_FUNDO)

ttk.Label(aba, text="Baixe vídeos ou áudios do YouTube", background=COR_FUNDO, foreground=COR_TEXTO, font=("Arial", 14, "bold")).pack(pady=20)

botao1 = tk.Button(aba, text="Baixar MP3", command=baixar_mp3, width=20, height=2)
estilizar_botao(botao1)
botao1.pack(pady=10)

botao2 = tk.Button(aba, text="Baixar MP4", command=baixar_mp4, width=20, height=2)
estilizar_botao(botao2)
botao2.pack(pady=10)

botao3 = tk.Button(aba, text="Fechar", command=aba.destroy, width=20, height=2)
estilizar_botao(botao3)
botao3.pack(pady=10)

aba.mainloop()
