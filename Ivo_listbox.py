import tkinter as tk
from tkinter import messagebox

# Function to save the data from the entries to the listbox
def save_data():
    name = entry_name.get()
    address = entry_address.get()
    cpf = entry_cpf.get()
    age = entry_age.get()

    if not (name and address and cpf and age):
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    user_data = f"Name: {name}, Address: {address}, CPF: {cpf}, Age: {age}"
    listbox_users.insert(tk.END, user_data)

    # Clear the entry fields after saving
    entry_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Function to delete the selected item from the listbox
def delete_data():
    selected_user = listbox_users.curselection()
    if not selected_user:
        messagebox.showwarning("Selection Error", "Please select a user to delete.")
        return
    listbox_users.delete(selected_user)

# Create the main window
root = tk.Tk()
root.title("User Information")

# Labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_address = tk.Entry(root)
entry_address.grid(row=1, column=1, padx=10, pady=5)

label_cpf = tk.Label(root, text="CPF:")
label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_cpf = tk.Entry(root)
entry_cpf.grid(row=2, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1, padx=10, pady=5)

# Buttons for saving and deleting data
btn_save = tk.Button(root, text="SAVE", command=save_data)
btn_save.grid(row=4, column=0, padx=10, pady=10)

btn_delete = tk.Button(root, text="DELETE", command=delete_data)
btn_delete.grid(row=4, column=1, padx=10, pady=10)

# Listbox to display users' information
listbox_users = tk.Listbox(root, width=60, height=10)
listbox_users.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
