import json
import os

TASK_FILE = "data/tasks.json"

# Função para carregar as tarefas do arquivo JSON


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

# Função para salvar as tarefas no arquivo JSON


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

# Função para adicionar uma tarefa


def add_task(title, description):
    tasks = load_tasks()
    task = {"title": title, "description": description}
    tasks.append(task)
    save_tasks(tasks)

# Função para listar as tarefas


def list_tasks():
    return load_tasks()

# Função para remover uma tarefa


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
