import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=100, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

def clear_entry():
    entry.delete(0, tk.END)  # Clear the entry

root.mainloop()
