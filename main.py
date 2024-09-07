import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())  # Evaluate the expression
        entry.delete(0, tk.END)     # Clear the entry
        entry.insert(tk.END, str(result))  # Insert the result
    except Exception:
        entry.delete(0, tk.END)  # Clear the entry on error
        entry.insert(tk.END, "Error")  # Show error

# Function to handle button clicks
def button_click(value):
    current = entry.get()  # Get current input
    entry.delete(0, tk.END)  # Clear the entry
    entry.insert(tk.END, current + str(value))  # Append clicked button value

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)  # Clear the entry

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0)
]

# Add buttons to the grid
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda value=text: button_click(value))
    button.grid(row=row, column=column)

# Create operator and equal buttons
operator_buttons = [
    ('/', 1, 3), ('*', 2, 3), ('-', 3, 3), ('+', 4, 3), ('=', 4, 2)
]

for (text, row, column) in operator_buttons:
    if text == "=":
        button = tk.Button(root, text=text, padx=20, pady=20, command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda value=text: button_click(value))
    button.grid(row=row, column=column)

 # Add 'C' button
clear_button = tk.Button(root, text="C", padx=20, pady=20, command=clear_entry)
clear_button.grid(row=4, column=1)

root.mainloop()
