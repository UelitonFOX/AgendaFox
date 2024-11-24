import tkinter as tk
from tkinter import messagebox
from models import add_task, list_tasks, delete_task

def create_task_window():
    def on_add_task():
        title = title_entry.get()
        description = description_entry.get()
        if title and description:
            add_task(title, description)
            messagebox.showinfo("Sucesso", "Tarefa adicionada!")
            list_all_tasks()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def on_delete_task():
        selected_task = task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            delete_task(task_index)
            messagebox.showinfo("Sucesso", "Tarefa excluída!")
            list_all_tasks()

    def list_all_tasks():
        task_listbox.delete(0, tk.END)
        tasks = list_tasks()
        for task in tasks:
            task_listbox.insert(tk.END, f"{task['title']} - {task['description']}")

    window = tk.Tk()
    window.title("AgendaFox - Gerenciamento de Tarefas")
    window.geometry("500x400")

    # Campos para adicionar tarefa
    title_label = tk.Label(window, text="Título da Tarefa")
    title_label.pack()

    title_entry = tk.Entry(window, width=40)
    title_entry.pack()

    description_label = tk.Label(window, text="Descrição da Tarefa")
    description_label.pack()

    description_entry = tk.Entry(window, width=40)
    description_entry.pack()

    add_button = tk.Button(window, text="Adicionar Tarefa", command=on_add_task)
    add_button.pack(pady=10)

    # Lista de tarefas
    task_listbox = tk.Listbox(window, width=50, height=10)
    task_listbox.pack(pady=10)

    delete_button = tk.Button(window, text="Excluir Tarefa", command=on_delete_task)
    delete_button.pack(pady=10)

    list_all_tasks()  # Listar as tarefas existentes ao iniciar

    window.mainloop()
