import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    text_area.delete(1.0, tk.END)
    window.title("Untitled - Notepad")


def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return

    try:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        window.title(f"{file_path} - Notepad")
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file: {e}")


def save_file():
    file_path = filedialog.asksaveasfilename(
        initialfile="Untitled.txt",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return

    try:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        window.title(f"{file_path} - Notepad")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")


# --- UI Setup ---
window = tk.Tk()
window.title("Untitled - Notepad")
window.geometry("800x600")

# Text Area
text_area = tk.Text(window, font=("Arial", 12), wrap="word")
text_area.pack(expand=True, fill="both")

# Menu Bar
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()