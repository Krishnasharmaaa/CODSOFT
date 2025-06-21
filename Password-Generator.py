import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("450x400")
        self.root.resizable(False, False)
        
        self.password_length = tk.IntVar(value=12)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()
        self.difficulty = tk.StringVar(value="Medium")
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        difficulty_frame = ttk.LabelFrame(main_frame, text="Password Difficulty", padding=10)
        difficulty_frame.pack(fill=tk.X, pady=5)
        
        difficulties = [
            ("Easy", "Easy"),
            ("Medium", "Medium"),
            ("Hard", "Hard"),
            ("Custom", "Custom")
        ]
        
        for text, mode in difficulties:
            ttk.Radiobutton(
                difficulty_frame,
                text=text,
                variable=self.difficulty,
                value=mode,
                command=self.set_difficulty
            ).pack(side=tk.LEFT, padx=5)
        
        length_frame = ttk.Frame(main_frame)
        length_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(length_frame, text="Password Length:").pack(side=tk.LEFT)
        self.length_slider = ttk.Scale(
            length_frame,
            from_=6,
            to=32,
            variable=self.password_length,
            command=lambda e: self.update_length_label()
        )
        self.length_slider.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.X)
        
        self.length_label = ttk.Label(length_frame, text="12")
        self.length_label.pack(side=tk.LEFT)
        options_frame = ttk.LabelFrame(main_frame, text="Character Types", padding=10)
        options_frame.pack(fill=tk.X, pady=10)
        
        self.uppercase_check = ttk.Checkbutton(
            options_frame,
            text="Uppercase Letters (A-Z)",
            variable=self.include_uppercase
        )
        self.uppercase_check.pack(anchor=tk.W)
        
        self.lowercase_check = ttk.Checkbutton(
            options_frame,
            text="Lowercase Letters (a-z)",
            variable=self.include_lowercase
        )
        self.lowercase_check.pack(anchor=tk.W)
        
        self.digits_check = ttk.Checkbutton(
            options_frame,
            text="Digits (0-9)",
            variable=self.include_digits
        )
        self.digits_check.pack(anchor=tk.W)
        
        self.symbols_check = ttk.Checkbutton(
            options_frame,
            text="Symbols (!@#$%^&*)",
            variable=self.include_symbols
        )
        self.symbols_check.pack(anchor=tk.W)
        
        ttk.Button(
            main_frame,
            text="Generate Password",
            command=self.generate_password
        ).pack(pady=10)
        
        password_frame = ttk.Frame(main_frame)
        password_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(password_frame, text="Generated Password:").pack(side=tk.LEFT)
        
        self.password_entry = ttk.Entry(
            password_frame,
            textvariable=self.generated_password,
            font=('Courier', 12),
            state='readonly'
        )
        self.password_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        ttk.Button(
            password_frame,
            text="Copy",
            command=self.copy_to_clipboard
        ).pack(side=tk.LEFT)
        
        self.set_difficulty()
    
    def set_difficulty(self):
        difficulty = self.difficulty.get()
        
        if difficulty == "Easy":
            self.password_length.set(8)
            self.include_uppercase.set(True)
            self.include_lowercase.set(True)
            self.include_digits.set(False)
            self.include_symbols.set(False)
            self.toggle_character_options(False)
        elif difficulty == "Medium":
            self.password_length.set(12)
            self.include_uppercase.set(True)
            self.include_lowercase.set(True)
            self.include_digits.set(True)
            self.include_symbols.set(False)
            self.toggle_character_options(False)
        elif difficulty == "Hard":
            self.password_length.set(16)
            self.include_uppercase.set(True)
            self.include_lowercase.set(True)
            self.include_digits.set(True)
            self.include_symbols.set(True)
            self.toggle_character_options(False)
        else:  
            self.toggle_character_options(True)
        
        self.update_length_label()
    
    def toggle_character_options(self, state):
        """Enable/disable character checkboxes based on mode"""
        if state:
            self.uppercase_check.config(state=tk.NORMAL)
            self.lowercase_check.config(state=tk.NORMAL)
            self.digits_check.config(state=tk.NORMAL)
            self.symbols_check.config(state=tk.NORMAL)
        else:
            self.uppercase_check.config(state=tk.DISABLED)
            self.lowercase_check.config(state=tk.DISABLED)
            self.digits_check.config(state=tk.DISABLED)
            self.symbols_check.config(state=tk.DISABLED)
    
    def update_length_label(self):
        self.length_label.config(text=str(int(self.password_length.get())))
    
    def generate_password(self):
        if not any([
            self.include_uppercase.get(),
            self.include_lowercase.get(),
            self.include_digits.get(),
            self.include_symbols.get()
        ]):
            messagebox.showerror("Error", "Please select at least one character type")
            return
        
        char_sets = []
        if self.include_uppercase.get():
            char_sets.append(string.ascii_uppercase)
        if self.include_lowercase.get():
            char_sets.append(string.ascii_lowercase)
        if self.include_digits.get():
            char_sets.append(string.digits)
        if self.include_symbols.get():
            char_sets.append(string.punctuation)
        
        length = int(self.password_length.get())
        password = []
        
        for char_set in char_sets:
            password.append(random.choice(char_set))
        
        remaining_length = length - len(password)
        all_chars = ''.join(char_sets)
        password.extend(random.choice(all_chars) for _ in range(remaining_length))
        
        random.shuffle(password)
        password = ''.join(password)
        
        self.generated_password.set(password)
    
    def copy_to_clipboard(self):
        if self.generated_password.get():
            self.root.clipboard_clear()
            self.root.clipboard_append(self.generated_password.get())
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password generated yet")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()