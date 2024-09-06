
def add_item(items, descricao, valor, tipo): #definindo a funçao que possui esses paramentros

  item = {
      "valor":valor,
      "descricao": descricao,
      "tipo": tipo
    }
  
  items.append(item)  #essa função serve pra adicionar um novo item a lista
  
  
def calcular_totais(items): #função pra guardar entradas e saidas e definir o saldo total
  total_entrada = 0
  total_saida = 0
  for item in items:
    if item['tipo'] == 'Entrada': 
      total_entrada += item['valor'] 
    if item['tipo'] == 'Saida':
      total_saida += item['valor']  
      
  saldo_total = total_entrada - total_saida

  return {
      "entrada": total_entrada,
      "saida": total_saida,
      "saldo": saldo_total
      
  }