import random
import tkinter as tk
from tkinter import messagebox, font

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        self.scores = {"user": 0, "computer": 0, "tie": 0}
        self.user_choice = None
        self.computer_choice = None
        
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.button_font = font.Font(family="Arial", size=14)
        self.score_font = font.Font(family="Arial", size=12)
        
        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = tk.Label(
            self.root, 
            text="Rock-Paper-Scissors", 
            font=self.title_font
        )
        self.title_label.pack(pady=20)
        
        self.instructions = tk.Label(
            self.root,
            text="Choose your weapon:",
            font=self.button_font
        )
        self.instructions.pack()
        
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)
        
        self.rock_btn = tk.Button(
            self.buttons_frame,
            text="Rock",
            font=self.button_font,
            width=10,
            command=lambda: self.make_choice("rock")
        )
        self.rock_btn.pack(side=tk.LEFT, padx=10)
        
        self.paper_btn = tk.Button(
            self.buttons_frame,
            text="Paper",
            font=self.button_font,
            width=10,
            command=lambda: self.make_choice("paper")
        )
        self.paper_btn.pack(side=tk.LEFT, padx=10)
        
        self.scissors_btn = tk.Button(
            self.buttons_frame,
            text="Scissors",
            font=self.button_font,
            width=10,
            command=lambda: self.make_choice("scissors")
        )
        self.scissors_btn.pack(side=tk.LEFT, padx=10)
        
        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(pady=20)
        
        self.user_choice_label = tk.Label(
            self.results_frame,
            text="Your choice: ",
            font=self.score_font
        )
        self.user_choice_label.pack()
        
        self.computer_choice_label = tk.Label(
            self.results_frame,
            text="Computer choice: ",
            font=self.score_font
        )
        self.computer_choice_label.pack()
        
        self.result_label = tk.Label(
            self.results_frame,
            text="",
            font=self.score_font
        )
        self.result_label.pack(pady=10)
        
      
        self.score_frame = tk.Frame(self.root)
        self.score_frame.pack()
        
        self.user_score_label = tk.Label(
            self.score_frame,
            text="You: 0",
            font=self.score_font
        )
        self.user_score_label.pack(side=tk.LEFT, padx=10)
        
        self.computer_score_label = tk.Label(
            self.score_frame,
            text="Computer: 0",
            font=self.score_font
        )
        self.computer_score_label.pack(side=tk.LEFT, padx=10)
        
        self.tie_score_label = tk.Label(
            self.score_frame,
            text="Ties: 0",
            font=self.score_font
        )
        self.tie_score_label.pack(side=tk.LEFT, padx=10)
        
        self.reset_btn = tk.Button(
            self.root,
            text="Reset Game",
            font=self.button_font,
            command=self.reset_game
        )
        self.reset_btn.pack(pady=20)
    
    def make_choice(self, choice):
        self.user_choice = choice
        self.computer_choice = random.choice(["rock", "paper", "scissors"])
        
        self.user_choice_label.config(text=f"Your choice: {self.user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer choice: {self.computer_choice.capitalize()}")
        
        result = self.determine_winner(self.user_choice, self.computer_choice)
        self.scores[result] += 1
        
        if result == "tie":
            self.result_label.config(text="It's a tie!")
        elif result == "user":
            self.result_label.config(text="You win!")
        else:
            self.result_label.config(text="Computer wins!")
        
        self.update_scoreboard()
    
    def determine_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            return "user"
        return "computer"
    
    def update_scoreboard(self):
        self.user_score_label.config(text=f"You: {self.scores['user']}")
        self.computer_score_label.config(text=f"Computer: {self.scores['computer']}")
        self.tie_score_label.config(text=f"Ties: {self.scores['tie']}")
    
    def reset_game(self):
        self.scores = {"user": 0, "computer": 0, "tie": 0}
        self.user_choice = None
        self.computer_choice = None
        self.user_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer choice: ")
        self.result_label.config(text="")
        self.update_scoreboard()
        messagebox.showinfo("Game Reset", "The game has been reset!")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()