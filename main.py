import tkinter as tk
import winsound

# Function to evaluate the expression and play a different sound for "="
def evaluate_expression():
    winsound.Beep(800, 200)  # Play a different sound for "=" button
    try:
        result = eval(entry.get())  # Evaluate the expression
        entry.delete(0, tk.END)     # Clear the entry
        entry.insert(tk.END, str(result))  # Insert the result
    except Exception:
        entry.delete(0, tk.END)  # Clear the entry on error
        entry.insert(tk.END, "Error")  # Show error
        entry.config(state="disabled")  # Disable the entry after error

# Function to handle button clicks
def button_click(value):
    if entry["state"] == "disabled":  # Prevent further input after error
        return
    winsound.Beep(500, 100)  # Play a sound when any other button is clicked
    current = entry.get()  # Get current input
    entry.delete(0, tk.END)  # Clear the entry
    entry.insert(tk.END, current + str(value))  # Append clicked button value

# Function to clear the entry and re-enable input
def clear_entry():
    winsound.Beep(500, 100)  # Play a sound when 'C' is clicked
    entry.config(state="normal")  # Re-enable the entry after clearing
    entry.delete(0, tk.END)  # Clear the entry

# Create the main window
root = tk.Tk()
root.title("Attractive Simple Calculator")
root.configure(bg='#222')  # Set background color for the window

# Set window size
root.geometry("400x500")

# Create an entry widget with custom font and background color
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 18), bg='#333', fg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Create button styles
button_style = {'font': ('Arial', 16), 'padx': 20, 'pady': 20, 'bg': '#444', 'fg': 'white'}
operator_style = {'font': ('Arial', 16), 'padx': 20, 'pady': 20, 'bg': '#ff9900', 'fg': 'white'}

# Create number buttons with colors and fonts
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0)
]

# Add buttons to the grid
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, **button_style, command=lambda value=text: button_click(value))
    button.grid(row=row, column=column, padx=5, pady=5)

# Create operator and equal buttons with a different style
operator_buttons = [
    ('/', 1, 3), ('*', 2, 3), ('-', 3, 3), ('+', 4, 3), ('=', 4, 2)
]

for (text, row, column) in operator_buttons:
    if text == "=":
        button = tk.Button(root, text=text, **operator_style, command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, **operator_style, command=lambda value=text: button_click(value))
    button.grid(row=row, column=column, padx=5, pady=5)

# Add 'C' button with a different color
clear_button = tk.Button(root, text="C", **operator_style, command=clear_entry)
clear_button.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
