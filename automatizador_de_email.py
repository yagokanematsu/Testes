import smtplib
import csv
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
from datetime import datetime

def ler_contatos(arquivo_contatos):
    """
    Lê o arquivo CSV de contatos e retorna uma lista de dicionários.
    O arquivo deve ter pelo menos os campos 'nome' e 'email'.
    """
    contatos = []
    try:
        with open(arquivo_contatos, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contatos.append(row)
        return contatos
    except Exception as e:
        print(f"Erro ao ler arquivo de contatos: {e}")
        return []

def ler_template(arquivo_template):
    """
    Lê o arquivo de template de email e o retorna como um objeto Template.
    """
    try:
        with open(arquivo_template, 'r', encoding='utf-8') as file:
            conteudo = file.read()
            return Template(conteudo)
    except Exception as e:
        print(f"Erro ao ler template: {e}")
        return None

def enviar_email(destinatario, assunto, corpo, servidor_smtp, porta, remetente, senha):
    """
    Envia um email para o destinatário especificado.
    """
    try:
        # Configuração da mensagem
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario['email']
        msg['Subject'] = assunto
        
        # Anexando o corpo do email
        msg.attach(MIMEText(corpo, 'html'))
        
        # Iniciando conexão com o servidor SMTP
        with smtplib.SMTP(servidor_smtp, porta) as server:
            server.starttls()  # Habilita a criptografia TLS
            server.login(remetente, senha)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Erro ao enviar email para {destinatario['email']}: {e}")
        return False

def automatizar_emails(arquivo_contatos, arquivo_template, assunto, servidor_smtp, porta, remetente, senha, intervalo=5):
    """
    Automatiza o envio de emails para uma lista de contatos usando um template.
    """
    tempo_inicio = datetime.now()
    
    contatos = ler_contatos(arquivo_contatos)
    template = ler_template(arquivo_template)
    
    if not contatos or not template:
        print("Não foi possível executar o automatizador de emails.")
        return
    
    enviados = 0
    falhas = 0
    
    for contato in contatos:
        corpo_email = template.substitute(contato)
        
        print(f"Enviando email para {contato['nome']} ({contato['email']})...")
        
        if enviar_email(contato, assunto, corpo_email, servidor_smtp, porta, remetente, senha):
            enviados += 1
            print(f"Email enviado com sucesso para {contato['email']}!")
        else:
            falhas += 1
        
        if contato != contatos[-1]:
            time.sleep(intervalo)
    
    tempo_fim = datetime.now()
    tempo_execucao = tempo_fim - tempo_inicio
    
    # Resultados
    print(f"\nResumo do envio de emails:")
    print(f"- Total de contatos: {len(contatos)}")
    print(f"- Emails enviados com sucesso: {enviados}")
    print(f"- Falhas no envio: {falhas}")
    print(f"- Tempo total de execução: {tempo_execucao}")
    print(f"- Tempo médio por email: {tempo_execucao/len(contatos) if contatos else 0}")

if __name__ == "__main__":
    print(f"Iniciando automatizador de emails em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    tempo_inicio_total = datetime.now()
    
    arquivo_contatos = "C:\\programas\\python\\contatos.csv"
    arquivo_template = "C:\\programas\\python\\template.html"
    assunto = "Promoção"
    
    servidor_smtp = "smtp.gmail.com" 
    porta = 587  
    remetente = "gatinhojoaogilberto@gmail.com"
    senha = "wqps mytv xafv ider"
    
    intervalo = 5
    
    automatizar_emails(
        arquivo_contatos, 
        arquivo_template, 
        assunto, 
        servidor_smtp, 
        porta, 
        remetente, 
        senha, 
        intervalo
    )
    
    tempo_fim_total = datetime.now()
    tempo_total = tempo_fim_total - tempo_inicio_total
    print(f"\nTempo total de execução do programa: {tempo_total}")