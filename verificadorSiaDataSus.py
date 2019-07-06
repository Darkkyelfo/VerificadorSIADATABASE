'''
Script para enviar notificação de novos bancos da SIA SUS
Python 3.7
'''
import re,time,smtplib,urllib3

url = "http://sia.datasus.gov.br/versao/listar_ftp_sia.php"

def enviarEmail(emails):
    gmail_user = 'exemplo@gmail.com'#coloca tua conta do gmail aki pra enviar. Tem que ser gmail
    gmail_password = '' #senha do teu email

    sent_from = gmail_user
    to = emails
    SUBJECT = "novo BD SIA"
    TEXT = "Vai olhar: http://sia.datasus.gov.br/versao/listar_ftp_sia.php"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to,message)
        server.close()
    except:
        print('Something went wrong...')

def downloadPage():
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    page = str(response.data)
    return page

def qtNovosBD():
    expressao_regular = "<tr>"
    page = downloadPage()
    regex = re.compile(expressao_regular)
    quantidade_atual = len(regex.findall(page))
    return quantidade_atual

def procurarNovoBdSia():
    emails_receber = ["exemplo2@gmail.com"]#lista com os email que vão receber a notificação
    qtd_anterior = 0
    while(True):
        print(qtd_anterior)
        novos = qtNovosBD()
        print(novos)
        if(novos>qtd_anterior):
            print("enviando...")
            enviarEmail(emails_receber)
            qtd_anterior = novos
        time.sleep(10)

procurarNovoBdSia()





