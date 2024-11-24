import tkinter as tk
from tkinter import messagebox
from src.models import add_task, list_tasks, delete_task, update_task


def create_task_window():
    def on_add_task():
        title = title_entry.get()
        description = description_entry.get()
        if title and description:
            add_task(title, description)
            messagebox.showinfo("Sucesso", "Tarefa adicionada!")
            list_all_tasks()
            title_entry.delete(0, tk.END)  # Limpa o campo após adicionar
            description_entry.delete(0, tk.END)  # Limpa o campo após adicionar
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def on_delete_task():
        selected_task = task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            delete_task(task_index)
            messagebox.showinfo("Sucesso", "Tarefa excluída!")
            list_all_tasks()
        else:
            messagebox.showerror("Erro", "Selecione uma tarefa para excluir!")

    def on_update_task():
        selected_task = task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            new_title = title_entry.get()
            new_description = description_entry.get()
            if new_title and new_description:  # Verifica se os campos estão preenchidos
                update_task(task_index, new_title, new_description)
                messagebox.showinfo("Sucesso", "Tarefa atualizada!")
                list_all_tasks()  # Atualiza a lista de tarefas
                title_entry.delete(0, tk.END)  # Limpa os campos após atualizar
                # Limpa os campos após atualizar
                description_entry.delete(0, tk.END)
            else:
                messagebox.showerror(
                    "Erro", "Preencha todos os campos para atualizar a tarefa!")

    def list_all_tasks():
        task_listbox.delete(0, tk.END)
        tasks = list_tasks()
        for task in tasks:
            task_listbox.insert(
                tk.END, f"{task['title']} - {task['description']}")

    window = tk.Tk()
    window.title("AgendaFox - Gerenciamento de Tarefas")
    window.geometry("500x400")

    # Layout mais organizado com o grid
    title_label = tk.Label(window, text="Título da Tarefa")
    title_label.grid(row=0, column=0, padx=10, pady=5)

    title_entry = tk.Entry(window, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=5)

    description_label = tk.Label(window, text="Descrição da Tarefa")
    description_label.grid(row=1, column=0, padx=10, pady=5)

    description_entry = tk.Entry(window, width=40)
    description_entry.grid(row=1, column=1, padx=10, pady=5)

    add_button = tk.Button(
        window, text="Adicionar Tarefa", command=on_add_task)
    add_button.grid(row=2, column=0, columnspan=2, pady=10)

    update_button = tk.Button(
        window, text="Atualizar Tarefa", command=on_update_task)
    update_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Lista de tarefas
    task_listbox = tk.Listbox(window, width=50, height=10)
    task_listbox.grid(row=4, column=0, columnspan=2, pady=10)

    delete_button = tk.Button(
        window, text="Excluir Tarefa", command=on_delete_task)
    delete_button.grid(row=5, column=0, columnspan=2, pady=10)

    list_all_tasks()  # Listar as tarefas existentes ao iniciar

    window.mainloop()
