print('\n\033[4mOlá, você está num programa de registrar tarefas.\033[0m\n'.center(50))
tarefas = {} 
resposta = None
while resposta != '5':

    print('\n \033[31mDigite 1:\033[0m para adicionar uma nova tarefa. ')
    print(' \033[31mDigite 2:\033[0m para vizualizar suas tarefas. ')
    print(' \033[31mDigite 3:\033[0m para editar uma tarefa. ')
    print(' \033[31mDigite 4:\033[0m para excluir uma tarefa. ')
    print(' \033[31mDigite 5:\033[0m para sair do programa. \n')

    resposta = input('Digite: ')

    if resposta == '1':
        while True:
            print('\n\033[34mDigite o nome da sua tarefa.\033[0m\n')
            nova_tarefa = input('Digite: ').strip()
            if nova_tarefa != '':
                break
            else:
                print('\033[31m\nVocê precisar dar um nome para a sua tarefa. Digite um nome válido.\033[0m')

        print('\n\033[34mDigite uma descrição de sua nova tarefa.\033[0m\n')
        descrição_nova_tarefa = input('Digite: ')

        tarefas[nova_tarefa] = descrição_nova_tarefa
                       
    elif resposta == '2':
        print('\nSuas tarefas são:\n')
        cont = len(tarefas) - (len(tarefas) - 1)
        for i, j in tarefas.items():
            print(f'\033[32mTarefa {cont}:\033[0m {i}. \033[32mDescrição:\033[0m {j}.')
            cont = cont +1
