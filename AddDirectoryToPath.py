import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def add_to_path(directory):
    try:
        subprocess.run(f'setx PATH "%PATH%;{directory}"', shell=True, check=True)
        messagebox.showinfo("Success", f"Added to PATH:\n{directory}")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to add directory to PATH.")

def browse_directory(entry):
    directory = filedialog.askdirectory()
    if directory:
        entry.delete(0, tk.END)
        entry.insert(0, directory)

def execute_add(entry):
    directory = entry.get()
    if directory:
        add_to_path(directory)

def main():
    root = tk.Tk()
    root.title("Add Directory to PATH")
    root.geometry("300x200")

    label = tk.Label(root, text="Paste or browse to select a directory:")
    label.pack(pady=10)

    entry = tk.Entry(root, width=45)
    entry.pack(pady=5)

    browse_button = tk.Button(root, text="Browse", command=lambda: browse_directory(entry))
    browse_button.pack(pady=5)

    add_button = tk.Button(root, text="Add", command=lambda: execute_add(entry), height=20, width=20)
    add_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
