import tkinter as tk
import random
import time

# --- Sample texts for the typing test ---
texts = [
    "Typing fast is fun when your fingers fly like lightning on the keyboard!",
    "Python makes programming enjoyable with its simple and readable syntax.",
    "Practice every day and you'll be amazed how quickly your typing improves.",
    "Speed and accuracy go hand in hand when it comes to mastering typing."
]

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Fun Typing Speed Test 🎮")
        self.root.geometry("850x570")
        self.root.config(bg="#fff5cc")  # light yellow background

        self.sample_text = random.choice(texts)
        self.start_time = None
        self.end_time = None

        # --- Title ---
        self.title_label = tk.Label(
            root,
            text="✨ Typing Speed Challenge ✨",
            font=("Comic Sans MS", 28, "bold"),
            bg="#fff5cc",
            fg="#ff6600"
        )
        self.title_label.pack(pady=20)

        # --- Text Display ---
        self.text_display = tk.Label(
            root,
            text=self.sample_text,
            wraplength=700,
            justify="center",
            font=("Comic Sans MS", 16),
            bg="#ffebcc",
            fg="#333",
            padx=15,
            pady=15,
            relief="ridge",
            bd=4
        )
        self.text_display.pack(pady=10)

        # --- Typing Area ---
        self.entry = tk.Text(root, height=6, width=80, font=("Comic Sans MS", 14), wrap="word")
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)
        self.entry.bind("<Return>", self.on_enter_press)

        # --- Tip Label ---
        self.tip_label = tk.Label(
            root,
            text="💡 Press ENTER to stop typing!",
            font=("Comic Sans MS", 14, "italic"),
            bg="#fff5cc",
            fg="#6666cc"
        )
        self.tip_label.pack()

        # --- Buttons Frame ---
        self.button_frame = tk.Frame(root, bg="#fff5cc")
        self.button_frame.pack(pady=10)

        self.submit_btn = tk.Button(
            self.button_frame, text="✅ Done", command=self.check_speed,
            font=("Comic Sans MS", 14, "bold"), bg="#66cc66", fg="white", width=10
        )
        self.submit_btn.grid(row=0, column=0, padx=10)

        self.reset_btn = tk.Button(
            self.button_frame, text="🔁 Reset", command=self.reset_test,
            font=("Comic Sans MS", 14, "bold"), bg="#ff6666", fg="white", width=10
        )
        self.reset_btn.grid(row=0, column=1, padx=10)

        # --- Result Label ---
        self.result_label = tk.Label(root, text="", font=("Comic Sans MS", 16), bg="#fff5cc", fg="#333")
        self.result_label.pack(pady=20)

    # --- Start Timer ---
    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    # --- When Enter is Pressed ---
    def on_enter_press(self, event):
        self.check_speed()
        return "break"  # prevents adding a newline

    # --- Check Typing Speed and Accuracy ---
    def check_speed(self):
        if self.start_time is None:
            return

        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        typed_text = self.entry.get("1.0", "end-1c")
        words = typed_text.split()
        word_count = len(words)
        speed = (word_count / total_time) * 60 if total_time > 0 else 0

        accuracy = self.calculate_accuracy(self.sample_text, typed_text)
        self.result_label.config(
            text=f"🚀 Speed: {speed:.1f} WPM | 🎯 Accuracy: {accuracy:.1f}%"
        )

    # --- Calculate Accuracy ---
    def calculate_accuracy(self, sample, typed):
        sample_words = sample.split()
        typed_words = typed.split()
        correct = sum(1 for i in range(min(len(sample_words), len(typed_words)))
                      if sample_words[i] == typed_words[i])
        return (correct / len(sample_words)) * 100 if sample_words else 0

    # --- Reset Test ---
    def reset_test(self):
        new_text = random.choice(texts)
        while new_text == self.sample_text and len(texts) > 1:
            new_text = random.choice(texts)

        self.sample_text = new_text
        self.text_display.config(text=self.sample_text)
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
