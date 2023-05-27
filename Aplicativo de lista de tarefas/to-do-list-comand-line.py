class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Tarefa adicionada com sucesso!")

    def remove_task(self, index):
        if index >= 0 and index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print("Tarefa removida:", removed_task.description)
        else:
            print("Índice inválido!")

    def complete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            task = self.tasks[index]
            task.completed = True
            print("Tarefa concluída:", task.description)
        else:
            print("Índice inválido!")

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("Nenhuma tarefa encontrada.")
        else:
            for i, task in enumerate(self.tasks):
                status = "[x] " if task.completed else "[ ] "
                print(f"{i}. {status}{task.description}")

def main():
    task_manager = TaskManager()

    while True:
        print("\n-- Aplicativo de Lista de Tarefas --")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            description = input("Digite a descrição da tarefa: ")
            task_manager.add_task(description)
        elif choice == "2":
            index = int(input("Digite o índice da tarefa a ser removida: "))
            task_manager.remove_task(index)
        elif choice == "3":
            index = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
            task_manager.complete_task(index)
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
