def mostrar_menu():
    print('=' * 35)
    print("Menu:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Exibir Tarefas")
    print("5. Sair")
    print('=' * 35)


def adicionar_tarefa():
    print('=' * 35)
    tarefa = input("Digite a nova tarefa:")
    tarefas = {"tarefa": tarefa, "status": 'Pendente'}
    with open('lista_de_tarefas.txt', 'r') as f:
        linhas = f.readlines()
        i = len(linhas) + 1
    with open('lista_de_tarefas.txt', 'a') as f:
        f.write(f'{i}. {tarefas["tarefa"]} -- {tarefas["status"]}\n')
    print(f'"Tarefa {tarefa}" adicionada com sucesso!')


def remover_tarefa():
    exibir_tarefas()
    print('=' * 35)
    try:
        indice = int(input("Digite o número da tarefa que deseja remover:")) - 1
        with open("lista_de_tarefas.txt", "r") as f:
            linhas = f.readlines()
            if 0 <= indice <= len(linhas):
                del linhas[indice]
            else:
                print("Índice inválido")
        with open("lista_de_tarefas.txt", "w") as f:
            for i, linha in enumerate(linhas, start=1):
                texto = linha.split(".", 1)
                f.write(f"{i}. {texto[1]}")
        print(f"Tarefa {indice + 1} removida")
    except ValueError:
        print('Índice inválido')


def marcar_tarefa_concluida():
    exibir_tarefas()
    print('=' * 35)
    indice = int(input("Digite aqui o número da tarefa que deseja marcar como concluída:")) - 1
    try:
        with open('lista_de_tarefas.txt', 'r') as f:
            linhas = f.readlines()
        if 0 <= indice < len(linhas):
            linhas[indice] = linhas[indice].replace("Pendente", "Concluída")
            with open('lista_de_tarefas.txt', 'w') as f:
                f.writelines(linhas)
                print(f"Tarefa {indice + 1} marcada como concluída!")
        else:
            print("Índice inválido.")
    except FileNotFoundError:
        print("Arquivo não encontrado")


def exibir_tarefas():
    print('=' * 35)
    try:
        with open('lista_de_tarefas.txt', 'r') as f:
            conteudo = f.read()
            if not conteudo.strip():
                print("Nenhuma tarefa encontrada!")
            else:
                print("LISTA DE TAREFAS")
                print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado")


def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            remover_tarefa()
        elif escolha == '3':
            marcar_tarefa_concluida()
        elif escolha == '4':
            exibir_tarefas()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Escolha inválida! Tenta novamente.")
