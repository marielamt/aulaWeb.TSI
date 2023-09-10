from flask import Flask, render_template
from flask import request   #para trabalhar com os métodos GET e POST
from flask import flash     #para msgs popup
from flask import redirect  #para redirecionar páginas


# os templates coloca em outra pasta. 
# Por padrão, fica na pasta templates e não precisa informar no template_folder,
# mas se quiser armazenar em outra pasta indique nesse parâmetro.
meu_site = Flask(__name__, template_folder='templates') 
# no caso de usar flash pede a configuração de uma chave secreta
meu_site.config['SECRET_KEY'] = "palavra-secreta-IFRO"


@meu_site.route("/")       #se no navegador digitar / ou /index
@meu_site.route("/index")  
def indice():
    #return render_template ("t_index.html") #optei por prefixar com t_ os nomes dos arquivos que usam template
    return redirect ('/login')

@meu_site.route("/contato")
def contato():
    return render_template("t_contato.html") 

#rota /usuarios COM passagem de argumentos
@meu_site.route("/usuarios/<nome_usuario>;<nome_profissao>")
#rota /usuarios SEM passagem de argumentos --> definir valor padrão com defaults
@meu_site.route("/usuarios", defaults={"nome_usuario":"usuário?","nome_profissao":""})  
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  

    
#new
@meu_site.route("/login")
def login():
    return render_template("t_login.html")
    
#new
"""++++
Para poder recuperar os argumentos passados nos parâmetros na URL precisa importar o pacote
from flask import request

Também precisa colocar que essa página aceita requisições de tipo GET ou POST
O GET é padrão, mas no caso do POST altere no html method="POST"
"""
@meu_site.route("/autenticar", methods=['GET', 'POST']) 
def autenticar():
    #método POST - pega nos fields (campos) do formulário
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    if usuario == "admin" and senha == "ifro":
        return f"usuario: {usuario} e senha: {senha}"
    else:
        #para não dar msg. na outra página, vamos manter na própria página com flash
        #adicionar import flash
        flash("Dados inválidos!")
        flash("Login ou senha inválidos!")
        return redirect ('/login') #adicionar import redirect


if __name__ == "__main__": 
     meu_site.run(port = 5000) 
     