print('\n\033[4mOlá, você está num programa de registrar tarefas.\033[0m\n'.center(50))
tarefas = {} 
resposta = None
while resposta != '6':

    print('\n \033[31mDigite 1:\033[0m para adicionar uma nova tarefa. ')
    print(' \033[31mDigite 2:\033[0m para vizualizar suas tarefas. ')
    print(' \033[31mDigite 3:\033[0m para editar uma tarefa. ')
    print(' \033[31mDigite 4:\033[0m para excluir uma tarefa. ')
    print(' \033[31mDigite 5:\033[0m para excluir todas as tarefas.')
    print(' \033[31mDigite 6:\033[0m para sair do programa. \n')

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

    elif resposta == '3':
        print('\nEssas são as suas tarefas, qual você deseja alterar?\n')
        cont = len(tarefas) - (len(tarefas) - 1)
        for i, j in tarefas.items():
            print(f'\033[32mTarefa {cont}:\033[0m {i}. \033[32mDescrição:\033[0m {j}.')
            cont = cont +1        
        while True:
            while True:
                try:
                    num_tarefa = int(input('\n\033[95mDigite o número da tarefa que queira alterar:\033[0m '))
                except ValueError:
                    print('\nDigite um valor válido.')
                else:
                    break
            if num_tarefa > (len(tarefas)) or num_tarefa <= 0:
                print('\nDigite um valor válido.')
            else:
                break

        novo_nome = input('\033[95mDigite o novo nome de sua tarefa:\033[0m ')
        tarefas_chaves = list(tarefas.keys())
        tarefas[novo_nome] =  tarefas.pop(tarefas_chaves[num_tarefa - 1])
        print('\n')
        nova_descricao = input('\033[95mDigite a nova descrição de sua tarefa:\033[0m ')
        tarefas[novo_nome] = nova_descricao

    elif resposta == '4':
        print('\nEssas são as suas tarefas, qual você deseja excluir?\n')
        cont = len(tarefas) - (len(tarefas) - 1)
        for i, j in tarefas.items():
            print(f'\033[32mTarefa {cont}:\033[0m {i}. \033[32mDescrição:\033[0m {j}.')
            cont = cont +1    
        while True:
            while True:
                try:
                    num_tarefa = int(input('\n\033[95mDigite o número da tarefa que queira excluir:\033[0m '))
                except ValueError:
                    print('\nDigite um valor válido.')
                else:
                    break
            if num_tarefa == '' or num_tarefa > (len(tarefas) + 1) or num_tarefa <= 0:
                print('\nDigite um valor válido.')
            else:
                break
        tarefas_chaves = list(tarefas.keys())
        del tarefas[tarefas_chaves[num_tarefa - 1]]

    elif resposta == '5':
        tarefas.clear()

print('\n\033[93mPrograma Encerrado!\033[0m')