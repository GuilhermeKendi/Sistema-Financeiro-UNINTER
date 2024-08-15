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

entradas = []
saidas = []

total = 0

while True:
    try:
        print('1 - Registrar nova entrada')
        print('2 - Registrar nova saida')
        print('3 - Mostrar meu total')
        print('4 - Mostrar Historico')
        print('0 - sair')
        opcao = int(input('Digite a opção que deseja: '))

        if opcao == 1:
            nova_entrada = {
                "Categoria": input('Digite a categoria da nova entrada: '),
                "Valor": float(input('Digite o valor da nova entrada: '))
            }
            entradas.append(nova_entrada)

            total += nova_entrada['Valor']

            if not continuar(): #IF NOT CONITNUAR(): -> SERVE PARA CASO O USUARIO DIGA QUE NAO QUER CONTINUAR, O PROGRAMA RECONHECE O NAO COMO TRUE E DA SEQUENCIA NO BREAK ENCERRANDO O LOOP, CONSEQUENTEMENTE O PROGRAMA
                print('Encerrando...')
                break

        elif opcao == 2: 
            nova_saida = {
                "Categoria": input('Digite a categoria da nova saida: '),
                "Valor": float(input('Digite o valor da nova saida: '))
            }
            saidas.append(nova_saida)

            total -= nova_saida['Valor']

            if not continuar(): 
                print('Encerrando...')
                break

        elif opcao == 3: 
            print(f"Seu total atual é: {total:.2f}")

            if not continuar(): 
                print('Encerrando...')
                break

        elif opcao == 4: 
            print('Registro de entradas: ')
            for c in entradas:
                print(f'Categoria: {c["Categoria"]} || Valor: {c["Valor"]:.2f}')
            
            print('\nRegistro de Saidas: ')
            for c in saidas:
                print(f'Categoria: {c["Categoria"]} || Valor: {c["Valor"]:.2f}')
            
            if not continuar(): 
                print('Encerrando...')
                break

        elif opcao == 0:
            print('Encerrando...')
            break

        else:
            print('Digite uma opção válida...')

    except ValueError:
        print('Digite uma opção entre 0 e 4...')

