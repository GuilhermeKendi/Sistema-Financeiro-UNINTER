def add_item(items, descricao, valor, tipo): #definindo a funçao que possui esses paramentros

  if tipo == "entrada":
    valor = abs(valor)  # Garante que o valor seja positivo
  elif tipo == "saida":
    valor = -abs(valor)  # Garante que o valor seja negativo

  item = {
    "valor":valor,
    "descricao": descricao,
    "tipo": tipo
  }
  
  items.append(item)  #essa função serve pra adicionar um novo item a lista
  
  
def calcular_totais(items): #função pra guardar entradas e saidas e definir o saldo total
  entrada = sum(t["valor"] for t in items if t["tipo"] == "entrada") #soma o valor de cada transacao do tipo entrada
  saida = sum(abs(t["valor"]) for t in items if t["tipo"] == "saida") #soma o valor de cada transacao do tipo entrada
  saldo = entrada - saida
  
  return {
    "entrada": entrada, 
    "saida": saida, 
    "saldo": saldo
    }
