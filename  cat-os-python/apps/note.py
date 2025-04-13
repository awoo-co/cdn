import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    filepath = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    try:
        with open(filepath, "r") as file:
            text_area.delete("1.0", tk.END)  # Clear the current text
            text_area.insert(tk.END, file.read())
        window.title(f"Simple Notepad - {filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file:\n{e}")

def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    try:
        with open(filepath, "w") as file:
            file.write(text_area.get("1.0", tk.END))
        window.title(f"Simple Notepad - {filepath}")
        messagebox.showinfo("Success", "File saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file:\n{e}")

# Create the main window
window = tk.Tk()
window.title("Simple Notepad")

# Create a text area where you can type
text_area = tk.Text(window)
text_area.pack(expand=True, fill="both")

# Create a menu bar
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

# Start the application
window.mainloop()