#rotas
from main import app
from flask import render_template, request, redirect, url_for
from calculo import add_item, calcular_totais

itens= [] #não guarda os valores anteriores 

@app.route("/", methods=['GET', 'POST']) #definir as rotas e nosso metodo que no nosso caos e get e post
def homepage():
  ent = 0
  sai = 0
  sal= 0

  if request.method == 'POST':
    descricao = request.form['desc'] #e pra puxar os valores vindos do formulario html
    valor = float(request.form['valor'])
    tipo = request.form['Tipo']
    
    add_item(itens,descricao, valor,tipo) # esta chamando a função add_item pra ser executada

    resultado = calcular_totais(itens)

    ent=resultado['entrada']
    sai=resultado['saida']
    sal=resultado['saldo']

    # Redireciona para a mesma página após submissão do formulário
    return redirect(url_for('homepage'))
  
  resultado = calcular_totais(itens)
  ent = resultado['entrada']
  sai = resultado['saida']
  sal = resultado['saldo']

  return render_template("homepage.html", entrada=ent, saida=sai, saldo=sal, transacoes=itens) #para reenderizar a homepage junto as variaveis que serao usadas como paranmetro
