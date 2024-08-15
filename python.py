#FUNCAO PARA VERIFICAR SE O USUARIO QUER CONTINUAR COM O PROGRAMA
def continuar():
    while True:
        try:
            continuar = input('Deseja continuar? s - Sim || n - Nao ').lower().strip()
            if continuar == 's':
                return True
            elif continuar == 'n':
                return False
            else:
                print('Informe um valor válido...')
        except ValueError:
            print('Digite s - Sim ou n - Nao')

#INICIO DO CODIGO
print('SISTEMA FINANCEIRO')
print('--' * 30)

entrada = {
    "Categoria": "null",
    "Valor": 0
    }
saida = {
    "Categoria": "null",
    "Valor": 0
    }

total = 0

while True:
    try:
        print('1 - Registrar nova entrada')
        print('2 - Registrar nova saida')
        print('3 - Mostrar meu total')
        print('0 - sair')
        opcao = int(input('Digite a opção que deseja: '))
        if opcao == 1:
            entrada['Categoria'] = input('Digite a categoria da nova entrada: ')
            entrada['Valor'] = float(input('Digite o valor da nova entrada: '))
            total += entrada['Valor']
            if not continuar(): #IF NOT CONITNUAR(): -> SERVE PARA CASO O USUARIO DIGA QUE NAO QUER CONTINUAR, O PROGRAMA RECONHECE O NAO COMO TRUE E DA SEQUENCIA NO BREAK ENCERRANDO O LOOP, CONSEQUENTEMENTE O PROGRAMA
                print('Encerrando...')
                break
        elif opcao == 2: 
            saida['Categoria'] = input('Digite a categoria da nova saida: ')
            saida['Valor'] = float(input('Digite o valor da nova saida: '))
            total -= saida['Valor']
            if not continuar(): 
                print('Encerrando...')
                break
        elif opcao == 3: 
            print(f"Seu total atual é: {total:.2f}")
            if not continuar(): 
                print('Encerrando...')
                break
        elif opcao == 0:
            print('Encerrando...')
            break
        else:
            print('Digite uma opção válida...')
    except ValueError:
        print('Digite uma opção entre 0 e 3...')

