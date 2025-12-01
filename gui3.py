import tkinter as tk
import random

class WordScrambleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🔤 Word Scramble Game 🎯")
        self.root.geometry("800x550")
        self.root.config(bg="#f0f8ff")

        # --- Word List ---
        self.words = [
            "python", "computer", "science", "keyboard", "internet",
            "program", "mouse", "laptop", "screen", "language",
            "window", "variable", "function", "random", "syntax"
        ]

        self.correct_word = ""
        self.score = 0

        # --- Title ---
        self.title_label = tk.Label(
            root, text="✨ Word Scramble Challenge ✨",
            font=("Comic Sans MS", 28, "bold"),
            bg="#f0f8ff", fg="#0066cc"
        )
        self.title_label.pack(pady=20)

        # --- Word Display ---
        self.word_label = tk.Label(
            root,
            text="Game Starting...",
            font=("Comic Sans MS", 24, "bold"),
            bg="#e6f7ff",
            fg="#333",
            width=25,
            height=2,
            relief="ridge",
            bd=3
        )
        self.word_label.pack(pady=30)

        # --- Entry Field ---
        self.entry = tk.Entry(root, font=("Comic Sans MS", 18), width=20, justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_answer)

        self.tip_label = tk.Label(
            root, text="💡 Unscramble the word and press ENTER!",
            font=("Comic Sans MS", 14, "italic"),
            bg="#f0f8ff", fg="#6666cc"
        )
        self.tip_label.pack()

        # --- Reset Button ---
        self.reset_btn = tk.Button(
            root, text="🔁 Reset Game", command=self.reset_game,
            font=("Comic Sans MS", 14, "bold"), bg="#ff6666", fg="white", width=15
        )
        self.reset_btn.pack(pady=10)

        # --- Result Label ---
        self.result_label = tk.Label(
            root, text="", font=("Comic Sans MS", 16), bg="#f0f8ff"
        )
        self.result_label.pack(pady=10)

        # --- Score Display ---
        self.score_label = tk.Label(
            root, text=f"🏆 Score: {self.score}",
            font=("Comic Sans MS", 16, "bold"), bg="#f0f8ff", fg="#3333cc"
        )
        self.score_label.pack(pady=10)

        # start the first word
        self.new_word()

    # --- Generate New Word ---
    def new_word(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.word_label.config(bg="#e6f7ff", fg="#333")

        # pick a new random word
        self.correct_word = random.choice(self.words)
        scrambled = list(self.correct_word)
        random.shuffle(scrambled)
        scrambled_word = ''.join(scrambled)

        # display the scrambled version
        self.word_label.config(text=scrambled_word)

    # --- Check Answer ---
    def check_answer(self, event=None):
        if not self.correct_word:
            return

        user_input = self.entry.get().strip().lower()

        # === NEW: handle empty input gracefully ===
        if not user_input:
            self.result_label.config(text="⚠️ Type the unscrambled word first!", fg="orange")
            return
        # ==========================================

        self.entry.delete(0, tk.END)

        if user_input == self.correct_word:
            self.score += 1
            self.result_label.config(
                text=f"✅ Correct! The word was '{self.correct_word}'",
                fg="green"
            )
            self.word_label.config(bg="#b3ffb3")
        else:
            self.result_label.config(
                text=f"❌ Wrong! The correct word was '{self.correct_word}'",
                fg="red"
            )
            self.word_label.config(bg="#ffcccc")

        self.score_label.config(text=f"🏆 Score: {self.score}")

        # move to next word after 1 second
        self.root.after(1000, self.new_word)

    # --- Reset Game ---
    def reset_game(self):
        self.score = 0
        self.correct_word = ""
        self.word_label.config(text="Game Reset! Starting again...", bg="#e6f7ff", fg="#333")
        self.result_label.config(text="")
        self.score_label.config(text=f"🏆 Score: {self.score}")
        self.entry.delete(0, tk.END)
        self.root.after(1000, self.new_word)

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = WordScrambleGame(root)
    root.mainloop()
