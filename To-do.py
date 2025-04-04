import tkinter as tk


root = tk.Tk()
root.title("TO DO LIST")
root.config(bg="darkgreen")
root.geometry("400x500")


is_updating = False


input_var = tk.StringVar()
output_var = tk.StringVar()

def clear_output():
    output_var.set("")


def add_or_update_task():
    global is_updating

    task = input_var.get().strip()

    if task == "":
        output_var.set("Input bar is empty")
    else:
        if is_updating:
            selected = listbox.curselection()
            if selected and task not in listbox.get(0, tk.END):
                listbox.delete(selected[0])
                listbox.insert(selected[0], task)
                is_updating = False
                output_var.set("Task updated successfully")
            else:
                is_updating = False
                add_or_update_task()  # Add new if selected got deleted
        else:
            tasks = listbox.get(0, tk.END)
            if task not in tasks:
                listbox.insert(tk.END, task)
                output_var.set("Task added successfully")
            else:
                output_var.set("Task already exists")

    input_var.set("")
    listbox.selection_clear(0, tk.END)
    root.after(1500, clear_output)


def select_task_for_update():
    global is_updating

    if not listbox.size():
        output_var.set("List is empty")
    else:
        selected = listbox.curselection()
        if selected:
            input_var.set(listbox.get(selected[0]))
            is_updating = True
        else:
            output_var.set("No task selected")

    root.after(1500, clear_output)


def delete_task():
    if not listbox.size():
        output_var.set("List is empty")
    else:
        selected = listbox.curselection()
        if selected:
            listbox.delete(selected[0])
            output_var.set("Deleted successfully")
        else:
            output_var.set("No task selected")
    root.after(1500, clear_output)


def handle_button_click(event):
    text = event.widget.cget("text")
    if text == "CREATE":
        add_or_update_task()
    elif text == "UPDATE":
        select_task_for_update()
    elif text == "DELETE":
        delete_task()


heading = tk.Label(root, text="TO DO LIST", fg="white", bg="darkgreen",
                   font=("Arial", 20, "italic", "bold"), pady=15)
heading.pack()


frame1 = tk.Frame(root)
frame1.pack(fill="x", pady=5)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame1, height=10, width=50, yscrollcommand=scrollbar.set)
listbox.pack(fill="x")
scrollbar.config(command=listbox.yview)


frame2 = tk.Frame(root, bg="green")
frame2.pack(pady=10)

tk.Label(frame2, text="Input Task", bg="darkgreen", fg="white",
         font=("Arial", 13), padx=10).grid(row=0, column=0)

input_entry = tk.Entry(frame2, font=("Arial", 15, "bold"), textvariable=input_var)
input_entry.grid(row=0, column=1, pady=5)

output_entry = tk.Entry(frame2, state="readonly", width=25, justify="center",
                        bg="black", fg="darkgrey", font=("Arial", 10, "bold"),
                        textvariable=output_var)
output_entry.grid(row=1, column=1)


frame3 = tk.Frame(root, bg="darkgreen")
frame3.pack(pady=50)


def create_button(text, row, color, cmd=None):
    btn = tk.Button(frame3, text=text, width=20, fg="white", bg=color, padx=10)
    btn.grid(row=row, column=0, pady=10)
    if text == "QUIT":
        btn.config(command=cmd)
    else:
        btn.bind("<Button-1>", handle_button_click)

create_button("CREATE", 0, "grey")
create_button("UPDATE", 1, "grey")
create_button("DELETE", 2, "grey")
create_button("QUIT", 3, "red", cmd=root.quit)

root.mainloop()
