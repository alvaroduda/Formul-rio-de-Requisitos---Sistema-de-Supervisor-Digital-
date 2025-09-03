import os
from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail, Message


load_dotenv()


app = Flask(__name__)


app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp-mail.outlook.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')


mail = Mail(app)

def test_email():
    """Testa o envio de email"""
    
   
    if not app.config['MAIL_USERNAME'] or not app.config['MAIL_PASSWORD']:
        print("❌ ERRO: Credenciais de email não configuradas!")
        print("\n📋 Para configurar:")
        print("1. Copie o arquivo 'config_email_example.txt' para '.env'")
        print("2. Preencha MAIL_USERNAME e MAIL_PASSWORD com suas credenciais do Outlook")
        print("   MAIL_USERNAME deve ser: alvaro.hora@inoveagora.com.br")
        print("3. Para Outlook, use sua senha normal (não precisa de senha de app)")
        return False
    
    try:
       
        msg = Message(
            subject='Teste de Envio Automático - Sistema de Supervisor Digital',
            recipients=['alvaro.hora@inoveagora.com.br'],
            body='''Este é um email de teste para verificar se o envio automático está funcionando.

Se você recebeu este email, o sistema está configurado corretamente!

Sistema de Supervisor Digital - INNOVATECH
Data/Hora: ''' + str(os.popen('date /t & time /t').read().strip()),
            sender=app.config['MAIL_DEFAULT_SENDER']
        )
        
        print("📧 Enviando email de teste...")
        print(f"   De: {app.config['MAIL_USERNAME']}")
        print(f"   Para: alvaro.hora@inoveagora.com.br")
        print(f"   Servidor: {app.config['MAIL_SERVER']}:{app.config['MAIL_PORT']}")
        
        
        mail.send(msg)
        
        print("✅ Email enviado com sucesso!")
        print("📬 Verifique sua caixa de entrada em alvaro.hora@inoveagora.com.br")
        return True
        
    except Exception as e:
        print(f"❌ ERRO ao enviar email: {str(e)}")
        print("\n🔧 Possíveis soluções:")
        print("1. Verifique se as credenciais estão corretas")
        print("2. Para Outlook, use sua senha normal da conta")
        print("3. Se tiver 2FA ativado, desative ou gere uma senha de app")
        print("4. Verifique se a conta não está bloqueada por segurança")
        return False

if __name__ == "__main__":
    print("🧪 Teste de Envio de Email - Sistema de Supervisor Digital")
    print("=" * 60)
    
    test_email()
    
    print("\n" + "=" * 60)
    print("💡 Dica: Se o teste funcionou, o formulário também funcionará!")
