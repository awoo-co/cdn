import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)  # Clear previous text
            text_area.insert(tk.END, file.read())
        window.title(f"Simple Editor - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))
        window.title(f"Simple Editor - {filepath}")

window = tk.Tk()
window.title("Simple Editor")

text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD)
text_area.pack(expand=True, fill="both")

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()