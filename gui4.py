import tkinter as tk
import time
import random

class ReactionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ Reaction Time Tester ⚡")
        self.root.geometry("800x500")
        self.root.config(bg="#dfe7fd")

        self.start_time = None
        self.waiting = False
        self.best_time = None

        # --- Title ---
        self.title_label = tk.Label(
            root,
            text="⚡ Reaction Time Tester ⚡",
            font=("Comic Sans MS", 28, "bold"),
            bg="#dfe7fd",
            fg="#3333cc"
        )
        self.title_label.pack(pady=30)

        # --- Reaction Area ---
        self.screen = tk.Button(
            root,
            text="Click 'Start' to Begin!",
            font=("Comic Sans MS", 22, "bold"),
            bg="#ccccff",
            fg="#333",
            width=30,
            height=8,
            relief="ridge",
            bd=5,
            state="disabled"
        )
        self.screen.pack(pady=20)
        self.screen.config(command=self.react)

        # --- Start Button ---
        self.start_btn = tk.Button(
            root,
            text="▶️ Start",
            command=self.start_game,
            font=("Comic Sans MS", 16, "bold"),
            bg="#66cc66",
            fg="white",
            width=12
        )
        self.start_btn.pack(pady=10)

        # --- Result Label ---
        self.result_label = tk.Label(
            root,
            text="",
            font=("Comic Sans MS", 18),
            bg="#dfe7fd"
        )
        self.result_label.pack(pady=10)

        # --- Best Score ---
        self.best_label = tk.Label(
            root,
            text="🏆 Best: None",
            font=("Comic Sans MS", 16, "bold"),
            bg="#dfe7fd",
            fg="#000099"
        )
        self.best_label.pack(pady=10)

    def start_game(self):
        """Start the game and hide the start button"""
        self.start_btn.pack_forget()  # Hide start button
        self.result_label.config(text="")
        self.screen.config(text="Wait for GREEN...", bg="#ff9999", state="normal")
        self.waiting = True

        # Wait for a random delay before turning green
        delay = random.randint(2000, 5000)  # 2–5 seconds
        self.root.after(delay, self.turn_green)

    def turn_green(self):
        """Turn the screen green, ready for click"""
        if self.waiting:
            self.screen.config(text="CLICK NOW!", bg="#99ff99")
            self.start_time = time.time()
            self.waiting = False

    def react(self):
        """Handle player's click"""
        # Clicked too early
        if self.waiting:
            self.screen.config(
                text="Too soon! 😅 Wait for green next time.",
                bg="#ff6666"
            )
            self.waiting = False
            self.start_time = None
            self.after_reset()
            return

        # Valid click (after green)
        if self.start_time:
            reaction_time = round((time.time() - self.start_time) * 1000)
            self.screen.config(
                text=f"Your time: {reaction_time} ms",
                bg="#ccccff"
            )
            self.start_time = None

            # Update best time
            if self.best_time is None or reaction_time < self.best_time:
                self.best_time = reaction_time
                self.best_label.config(text=f"🏆 Best: {self.best_time} ms")
                self.result_label.config(text="🔥 New Record!", fg="green")
            else:
                self.result_label.config(text="⚡ Try Again!", fg="blue")

            self.after_reset()
        else:
            self.screen.config(
                text="Click 'Start' to begin!",
                bg="#ccccff"
            )

    def after_reset(self):
        """Wait and show Start button again"""
        self.screen.config(state="disabled")
        self.root.after(2000, self.show_start_btn)

    def show_start_btn(self):
        self.screen.config(text="Click 'Start' to Begin!", bg="#ccccff")
        self.start_btn.pack(pady=10)

# --- Run the Game ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ReactionGame(root)
    root.mainloop()


