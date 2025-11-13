from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
CORS(app)  # permite requisições do frontend hospedado em outro domínio

# Função original de envio de e-mail
def enviar_notificacao_email(email_remetente, senha_remetente, email_destinatario, assunto_email, caminho_arquivo_html_template_email):
    msg = MIMEMultipart()
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg['Subject'] = assunto_email

    with open(caminho_arquivo_html_template_email, 'r', encoding='utf-8') as arquivo:
        conteudo_html_template_email = arquivo.read()

    msg.attach(MIMEText(conteudo_html_template_email, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_remetente, senha_remetente)
        server.sendmail(email_remetente, email_destinatario, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro na tentativa de envio da notificação por e-mail: {e}")
    finally:
        server.quit()

# Endpoint Flask para receber dados do formulário
@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    dados = request.form
    nome = dados.get('nome')
    email_destinatario = dados.get('email')

    # Seus dados já fornecidos
    email_remetente = 'skai.skyfallgroup@gmail.com'
    senha_remetente = 'jqnp dgex ljwy hwtn'  # idealmente use variável de ambiente
    assunto_email = f"Olá {nome}!"
    caminho_template = 'TemplateEmail.html'

    try:
        enviar_notificacao_email(email_remetente, senha_remetente, email_destinatario, assunto_email, caminho_template)
        return jsonify({"status": "sucesso", "mensagem": "E-mail enviado com sucesso!"})
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
