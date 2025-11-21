import tkinter as tk
from tkinter import messagebox
import time
import random

# --------------------------
# SAMPLE TEXTS
# --------------------------
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast requires both practice and focus.",
    "Python is a versatile language used for many applications.",
    "Artificial Intelligence is shaping the future of technology.",
    "Consistency is the key to mastering any skill."
]

# --------------------------
# MAIN APP CLASS
# --------------------------
class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x500")
        self.root.config(bg="#f8f8f8")

        self.sample_text = random.choice(texts)
        self.start_time = None
        self.end_time = None

        # --------------------------
        # TITLE
        # --------------------------
        self.title_label = tk.Label(
            root,
            text="Typing Speed Test",
            font=("Arial", 26, "bold"),
            bg="#f8f8f8",
            fg="#333"
        )
        self.title_label.pack(pady=20)

        # --------------------------
        # DISPLAY TEXT
        # --------------------------
        self.text_display = tk.Label(
            root,
            text=self.sample_text,
            wraplength=700,
            justify="center",
            font=("Arial", 16),
            bg="#e6f0ff",
            fg="#000",
            padx=15,
            pady=15,
            relief="groove",
            bd=2
        )
        self.text_display.pack(pady=20)

        # --------------------------
        # ENTRY BOX
        # --------------------------
        self.entry = tk.Text(root, height=6, width=80, font=("Arial", 14))
        self.entry.pack(pady=20)
        self.entry.bind("<KeyPress>", self.start_timer)

        # --------------------------
        # BUTTONS
        # --------------------------
        self.button_frame = tk.Frame(root, bg="#f8f8f8")
        self.button_frame.pack()

        self.submit_btn = tk.Button(
            self.button_frame, text="Done", command=self.check_speed,
            font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", width=10
        )
        self.submit_btn.grid(row=0, column=0, padx=10)

        self.reset_btn = tk.Button(
            self.button_frame, text="Reset", command=self.reset_test,
            font=("Arial", 14, "bold"), bg="#e74c3c", fg="white", width=10
        )
        self.reset_btn.grid(row=0, column=1, padx=10)

        # --------------------------
        # RESULT LABEL
        # --------------------------
        self.result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f8f8f8")
        self.result_label.pack(pady=20)
        # Bind ESC key to end the test
        self.root.bind("<Escape>", lambda event: self.check_speed())

    # --------------------------
    # TIMER START
    # --------------------------
    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    # --------------------------
    # CHECK SPEED
    # --------------------------
    def check_speed(self):
        if self.start_time is None:
            messagebox.showwarning("Error", "You must start typing first!")
            return

        self.end_time = time.time()
        elapsed = self.end_time - self.start_time

        typed_text = self.entry.get("1.0", tk.END).strip()
        word_count = len(typed_text.split())
        speed = round((word_count / elapsed) * 60, 2)  # WPM

        accuracy = self.calculate_accuracy(typed_text, self.sample_text)

        self.result_label.config(
            text=f"Speed: {speed} WPM | Accuracy: {accuracy}%"
        )

    # --------------------------
    # CALCULATE ACCURACY
    # --------------------------
    def calculate_accuracy(self, typed, original):
        typed_words = typed.split()
        original_words = original.split()
        correct = 0

        for i in range(min(len(typed_words), len(original_words))):
            if typed_words[i] == original_words[i]:
                correct += 1

        accuracy = (correct / len(original_words)) * 100
        return round(accuracy, 2)

    # --------------------------
    # RESET TEST
    # --------------------------
    def reset_test(self):
        new_text= random.choice(texts)
        # Make sure it's not the same as the previous one
        while new_text == self.sample_text and len(texts) > 1:
            new_text = random.choice(texts)

        self.sample_text = new_text
        self.text_display.config(text=self.sample_text)
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None

# --------------------------
# RUN APP
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
