
from flask import Flask, render_template, request, flash, redirect, url_for
import os
import urllib.parse

app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_aqui_mude_em_producao'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            
            formulario = request.form
            
            
            
         
            email_data = {
                'disponibilidade': formulario.get('disponibilidade'),
                'horarios': formulario.get('horarios', 'Não informado'),
                'registro': formulario.get('registro'),
                'hospedagem': formulario.get('hospedagem'),
                'estrutura': formulario.get('estrutura'),
                'estoque': formulario.get('estoque'),
                'produto_novo': formulario.get('produto_novo'),
                'email_config': formulario.get('email_config'),
                'responsavel': formulario.get('responsavel'),
                'perguntas_adicionais': formulario.get('perguntas_adicionais', 'Não informado'),
                'especificacoes': formulario.get('especificacoes', 'Não informado'),
                'observacoes': formulario.get('observacoes', 'Não informado')
            }
            
            
            return redirect(url_for('confirmacao', **email_data))
            
        except Exception as e:
            flash(f'Erro ao enviar o formulário: {str(e)}', 'error')
            return render_template("formulario.html")
    
    return render_template("formulario.html")

@app.route("/confirmacao")
def confirmacao():
    
    disponibilidade = request.args.get('disponibilidade', '')
    horarios = request.args.get('horarios', 'Não informado')
    registro = request.args.get('registro', '')
    hospedagem = request.args.get('hospedagem', '')
    estrutura = request.args.get('estrutura', '')
    estoque = request.args.get('estoque', '')
    produto_novo = request.args.get('produto_novo', '')
    email_config = request.args.get('email_config', '')
    responsavel = request.args.get('responsavel', '')
    perguntas_adicionais = request.args.get('perguntas_adicionais', 'Não informado')
    especificacoes = request.args.get('especificacoes', 'Não informado')
    observacoes = request.args.get('observacoes', 'Não informado')

    
    
    email_body = f"""FORMULÁRIO DE REQUISITOS - SISTEMA DE SUPERVISOR DIGITAL
INNOVATECH

═══════════════════════════════════════════════════════════════

1. DISPONIBILIDADE DO SCRIPT:
   {disponibilidade}
   
   Horários específicos: {horarios}

2. REGISTRO DE OPERAÇÕES:
   {registro}

3. HOSPEDAGEM E EXECUÇÃO DO SCRIPT:
   {hospedagem}

4. ESTRUTURA DAS TABELAS DE MÁQUINAS:
   {estrutura}

5. DEFINIÇÃO DE ESTOQUE BAIXO:
   {estoque}

6. IDENTIFICAÇÃO DE MÁQUINA NOVA OU USADA:
   {produto_novo}

7. CONFIGURAÇÃO DE ENVIO DE E-MAILS:
   {email_config}

8. SUPERVISORA ATUAL:
   {responsavel}

9. PERGUNTAS ADICIONAIS:
   {perguntas_adicionais}

10. ESPECIFICAÇÕES DO PROJETO:
    {especificacoes}

11. OBSERVAÇÕES IMPORTANTES:
    {observacoes}

═══════════════════════════════════════════════════════════════

Sistema de Supervisor Digital - INNOVATECH"""
    
    
    encoded_subject = urllib.parse.quote_plus("Formulário de Requisitos Preenchido para o Software de Supervisor Digital")
    encoded_body = urllib.parse.quote_plus(email_body)
    outlook_url = f"mailto:alvaro.hora@inoveagora.com.br?subject={encoded_subject}&body={encoded_body}"
    
    return render_template("confirmacao.html", 
                         email_body=email_body,
                         outlook_url=outlook_url)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
