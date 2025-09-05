import tkinter as tk
from tkinter import messagebox
import json

FILENAME = 'contacts.json'


def load_contacts():
    """Loads contacts from a JSON file."""
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_contacts():
    """Saves the current contacts list to a JSON file."""
    with open(FILENAME, 'w') as f:
        json.dump(contacts, f, indent=4)


def populate_listbox():
    """Clears and repopulates the listbox with current contacts."""
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone cannot be empty.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    populate_listbox()
    clear_entries()


def delete_contact():
    try:
        selected_index = contact_listbox.curselection()[0]
        del contacts[selected_index]
        save_contacts()
        populate_listbox()
        clear_entries()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# --- Main App ---
contacts = load_contacts()

window = tk.Tk()
window.title("Contact Book")

# --- Frames ---
form_frame = tk.Frame(window, padx=10, pady=10)
form_frame.pack()

list_frame = tk.Frame(window, padx=10, pady=10)
list_frame.pack()

# --- Form Widgets ---
tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky='w')
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Phone:").grid(row=1, column=0, sticky='w')
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky='w')
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=2, column=1)

# --- Buttons ---
add_btn = tk.Button(form_frame, text="Add Contact", command=add_contact)
add_btn.grid(row=3, column=0, pady=10)

delete_btn = tk.Button(form_frame, text="Delete Selected", command=delete_contact)
delete_btn.grid(row=3, column=1, pady=10)

# --- Listbox ---
contact_listbox = tk.Listbox(list_frame, width=50, height=15)
contact_listbox.pack()
populate_listbox()

window.mainloop()