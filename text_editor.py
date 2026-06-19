import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")
        
        self.current_file = None
        
        # Create menu bar
        self.create_menu()
        
        # Create text area
        self.text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        # Create status bar
        self.status_bar = tk.Label(root, text="Untitled - Not Saved", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Clear All", command=self.clear_all)
        
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.status_bar.config(text="Untitled - Not Saved")
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
            self.current_file = file_path
            self.status_bar.config(text=f"Opened: {os.path.basename(file_path)}")
    
    def save_file(self):
        if self.current_file is None:
            self.save_as_file()
        else:
            with open(self.current_file, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            self.status_bar.config(text=f"Saved: {os.path.basename(self.current_file)}")
            messagebox.showinfo("Success", "File saved successfully!")
    
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            self.current_file = file_path
            self.status_bar.config(text=f"Saved: {os.path.basename(file_path)}")
            messagebox.showinfo("Success", "File saved successfully!")
    
    def clear_all(self):
        response = messagebox.askyesno("Confirm", "Are you sure you want to delete all text?")
        if response:
            self.text_area.delete(1.0, tk.END)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
