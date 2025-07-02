import tkinter as tk
def add_task():
  task= entry.get()
  if task:
    listbox.insert(tk.END,task)
    entry.delete(0,tk.END)
    save_tasks()
def save_tasks():
  with open("tasks.txt","w") as file:
    tasks=listbox.get(0,tk.END)
    for task in tasks:
      file.write(task+"\n")
def load_tasks():
  try:
    with open("tasks.txt","r") as file:
      for line in file:
        listbox.insert(tk.END,line.strip())
  except FileNotFoundError:
    pass
def mark_completed():
  try:
    selected_index=listbox.curselection()[0]
    task_text=listbox.get(selected_index)

    if "✅" not in task_text:
      task_text+="✅"
      listbox.delete(selected_index)
      listbox.insert(selected_index,task_text)
      save_tasks()
  except IndexError :
    pass
def delete_task():
  try:
    selected_index=listbox.curselection()[0]
    listbox.delete(selected_index)
    save_tasks()
  except IndexError:
    pass





root = tk.Tk()
root.title("TO DO LIST APP")
root.geometry("400x400")
entry=tk.Entry(root,width=30)
entry.pack(pady=10)

add_button=tk.Button(root,text="Add Task",command = add_task)
add_button.pack(pady=5)

mark_button=tk.Button(root,text="Mark as Completed",command=mark_completed)
mark_button.pack(pady=5)

delete_button=tk.Button(root,text="Delete Task",command=delete_task)
delete_button.pack(pady=5)



listbox=tk.Listbox(root,width=40)
listbox.pack(pady=10)

load_tasks()


root.mainloop()