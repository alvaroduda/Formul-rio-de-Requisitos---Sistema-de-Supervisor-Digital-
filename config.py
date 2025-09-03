import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configurações da aplicação Flask"""
    
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_aqui_mude_em_producao'
    

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
  
    MAIL_RECIPIENT = os.environ.get('MAIL_RECIPIENT') or 'alvaro.hora@inoveagora.com.br'
    
 
    DEBUG = os.environ.get('FLASK_DEBUG', 'false').lower() in ['true', 'on', '1']

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurações para produção"""
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
