import tkinter as tk
import random

class NumberGuesser:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guesser Game 🎯")
        self.root.geometry("800x500")
        self.root.config(bg="#d6eaf8")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.score = 0

        # --- Title ---
        self.title_label = tk.Label(
            root,
            text="🎯 Guess the Number Between 1 and 100 🎯",
            font=("Comic Sans MS", 24, "bold"),
            bg="#d6eaf8",
            fg="#1b4f72"
        )
        self.title_label.pack(pady=30)

        # --- Entry Box ---
        self.guess_label = tk.Label(
            root,
            text="Enter your guess:",
            font=("Comic Sans MS", 18, "bold"),
            bg="#d6eaf8",
            fg="#154360"
        )
        self.guess_label.pack(pady=10)

        self.guess_entry = tk.Entry(
            root,
            font=("Comic Sans MS", 18),
            width=10,
            justify="center"
        )
        self.guess_entry.pack(pady=10)

        # --- Guess Button ---
        self.guess_button = tk.Button(
            root,
            text="✅ Guess",
            command=self.check_guess,
            font=("Comic Sans MS", 16, "bold"),
            bg="#5dade2",
            fg="white",
            width=12
        )
        self.guess_button.pack(pady=10)

        # --- Feedback Label ---
        self.feedback_label = tk.Label(
            root,
            text="",
            font=("Comic Sans MS", 18, "bold"),
            bg="#d6eaf8"
        )
        self.feedback_label.pack(pady=20)

        # --- Score Label ---
        self.score_label = tk.Label(
            root,
            text=f"Score: {self.score}",
            font=("Comic Sans MS", 16, "bold"),
            bg="#d6eaf8",
            fg="#1a5276"
        )
        self.score_label.pack(pady=5)

        # --- Restart and Exit Buttons ---
        self.button_frame = tk.Frame(root, bg="#d6eaf8")
        self.button_frame.pack(pady=20)

        self.restart_button = tk.Button(
            self.button_frame,
            text="🔄 Restart",
            command=self.restart_game,
            font=("Comic Sans MS", 14, "bold"),
            bg="#58d68d",
            fg="white",
            width=10
        )
        self.restart_button.grid(row=0, column=0, padx=10)

        self.exit_button = tk.Button(
            self.button_frame,
            text="❌ Exit",
            command=root.destroy,
            font=("Comic Sans MS", 14, "bold"),
            bg="#ec7063",
            fg="white",
            width=10
        )
        self.exit_button.grid(row=0, column=1, padx=10)

    def check_guess(self):
        """Check the user's guess"""
        guess = self.guess_entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="⚠️ Please enter a valid number!", fg="red")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.secret_number:
            self.feedback_label.config(text="⬆️ Too Low! Try Again!", fg="#2874a6")
        elif guess > self.secret_number:
            self.feedback_label.config(text="⬇️ Too High! Try Again!", fg="#a93226")
        else:
            self.feedback_label.config(text=f"🎉 Correct! You guessed it in {self.attempts} tries!", fg="green")
            self.score += max(10 - self.attempts, 1)  # More tries = less score
            self.score_label.config(text=f"Score: {self.score}")
            self.guess_button.config(state="disabled")

        self.guess_entry.delete(0, tk.END)

    def restart_game(self):
        """Restart with a new number"""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state="normal")

# --- Run the Game ---
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuesser(root)
    root.mainloop()
