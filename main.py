import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=100, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

def clear_entry():
    entry.delete(0, tk.END)  # Clear the entry

 # Add 'C' button
clear_button = tk.Button(root, text="C", padx=20, pady=20, command=clear_entry)
clear_button.grid(row=4, column=1)

root.mainloop()
