# Criamos uma lista vazia para guardar as tarefas
tarefas = []

while True:
    print("\n" + "="*20)
    print(" 📋 LISTA DE TAREFAS")
    print("="*20)
    print("1. Adicionar tarefa")
    print("2. Ver todas as tarefas")
    print("3. Remover tarefa")
    print("4. Sair")
    
    opcao = input("\nEscolha uma opção (1-4): ")

    # OPÇÃO 1: ADICIONAR
    if opcao == '1':
        nova_tarefa = input("Digite o nome da tarefa: ").capitalize()
        tarefas.append(nova_tarefa)
        print(f"✅ Tarefa '{nova_tarefa}' adicionada!")

    # OPÇÃO 2: MOSTRAR LISTA
    elif opcao == '2':
        print("\n--- SUAS TAREFAS ---")
        if len(tarefas) == 0:
            print("A lista está vazia.")
        else:
            # O enumerate ajuda a mostrar o número (i) e a tarefa (t)
            for i, t in enumerate(tarefas):
                print(f"{i}: {t}")

    # OPÇÃO 3: REMOVER
    elif opcao == '3':
        # Primeiro mostramos a lista para saber o número
        print("\nQual número deseja apagar?")
        for i, t in enumerate(tarefas):
            print(f"{i}: {t}")
        
        try:
            numero_remover = int(input("Digite o número da tarefa: "))
            # Verificamos se o número existe na lista
            if 0 <= numero_remover < len(tarefas):
                removida = tarefas.pop(numero_remover)
                print(f"❌ Tarefa '{removida}' removida com sucesso!")
            else:
                print("⚠️ Número inválido!")
        except:
            print("⚠️ Erro: Digite apenas números inteiros.")

    # OPÇÃO 4: SAIR
    elif opcao == '4':
        print("Encerrando programa...")
        break
        
    else:
        print("Opção inválida, tente novamente.")
