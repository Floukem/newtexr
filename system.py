import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEText

host = "smtp.gmail.com"
port = "587"
login = "skai.skyfallgroup@gmail.com"
senha = "jqnp dgex ljwy hwtn"

server = smtplib.SMTP(host,port)

server.ehlo()
server.starttls()
server.login(login, senha)