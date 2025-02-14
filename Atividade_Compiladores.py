def main():
    tarefas = []
    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Mostrar Tarefas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            remover_tarefa(tarefas)
        elif opcao == "3":
            mostrar_tarefas(tarefas)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def remover_tarefa(tarefas):
    mostrar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa para remover: "))
        if 1 <= indice <= len(tarefas):
            removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{removida}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número valido:")

