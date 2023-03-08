from random import seed, randint
import csv
import smtplib
from email.mime.text import MIMEText

def carregaListaAlunos():
    dadosAlunos = []

    with open('todos.csv', newline='', encoding='utf-8') as arquivo:
        dados = csv.reader(arquivo, delimiter=';')

        for linha in dados:       
            nome, email = linha
            dadosAlunos.append({'nome':nome, 'email':email})
                                
        return dadosAlunos
                 
def enviaEmail(aluno, email, senha):
    '''
    Para que o envio funcione é preciso desligar parte das
    verificações de segurança da conta do Google (isso não é uma boa ideia!):
    https://www.google.com/settings/security/lesssecureapps
    '''
    # conexão com os servidores do google
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    # username ou email para logar no servidor
    username = email
    password = senha

    from_addr = email
    to_addrs = [aluno['email'].lower()]   #oficial

    # montando a mensagem
    mensagem = "Olá "+ aluno['nome'] +", Feliz 2023! \n\n"

    mensagem += "mensagem que vc quer enviar\n"

    mensagem += "\n\n\n"
    mensagem += "Grande Abraço,\n\n"
    mensagem += "Augusto L. P. Nunes\n"
    mensagem += "PROJETO: RESIDÊNCIA EM TIC 08 - Redes 5G PR\n"
    mensagem += "Uma iniciativa: MCTI Futuro\n"
    mensagem += "Executora do projeto: Instituto Federal do Paraná - IFPR\n"   
    mensagem += "Coordenadoria: Associação para Promoção da Excelência do Software Brasileiro - Softex\n" 
    mensagem += "Nossos canais oficiais:\n"

    mensagem += "https://huawei-ifpr.vercel.app\n"
    mensagem += "https://www.linkedin.com/company/ictacademy-ifpr\n"
    mensagem += "https://www.instagram.com/ictacademy.ifpr\n"
    mensagem += "https://www.facebook.com/ictacademy.ifpr\n"
    mensagem += "https://www.youtube.com/@ictacademyifpr"
    
    
    # a biblioteca email possui vários templates
    # para diferentes formatos de mensagem
    # neste caso usaremos MIMEText para enviar
    # somente texto
    message = MIMEText(mensagem)
    message['subject'] = 'Curso online de Redes 5G Gratuito'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()
    
'''
Aqui está a parte principal do programa
É aqui que o passo a passo do problema será resolvido
'''
if __name__ == "__main__":
    
    print("##############################################")
    print("# 1 - Enviar emails para alunos              #")
    print("# 2 - sair                                   #")
    print("##############################################")
    opcao = int(input("Digite sua opção: "))

    if opcao == 2: exit(0)

    if opcao ==  1:
        email = input("Digite o email da sua conta para envio: ")
        senha = input("Digite a senha da sua conta de email: ")    

        #carrega os dados dos alunos que estão no aquivo .csv
        alunos = carregaListaAlunos()

        #para cada aluno, realiza o sorteio e envia o email com o resultado
        for aluno in alunos:  
            try:      
                #mensagem para o aluno                                
                enviaEmail(aluno, email, senha)
                
                #formatando a saída:
                print("Mensagem enviada para: " + aluno['nome'])
                
                exit()
                
            except Exception as e:
                log = open('erros.txt', 'a')
                log.write('Erro para + ' + aluno['nome'] + ': '+str(e)+'\n')
                log.close()
