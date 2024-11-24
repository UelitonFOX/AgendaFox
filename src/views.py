# views.py
import tkinter as tk

def create_task_window():
    window = tk.Tk()
    window.title("AgendaFox - Tarefas")
    window.geometry("400x300")

    label = tk.Label(window, text="Adicionar tarefa", font=("Arial", 12))
    label.pack(pady=20)

    button_add_task = tk.Button(window, text="Adicionar tarefa", font=("Arial", 12))
    button_add_task.pack(pady=10)

    window.mainloop()
