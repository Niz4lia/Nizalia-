import tkinter as tk
import random

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Fun Math Quiz Game 🎯")
        self.root.geometry("800x550")
        self.root.config(bg="#e6f7ff")

        self.score = 0
        self.question = ""
        self.answer = 0
        self.level = "Easy"

        # --- Title ---
        self.title_label = tk.Label(
            root,
            text="✨ Math Quiz Challenge ✨",
            font=("Comic Sans MS", 28, "bold"),
            bg="#e6f7ff",
            fg="#0066cc"
        )
        self.title_label.pack(pady=20)

        # --- Level Buttons ---
        self.level_frame = tk.Frame(root, bg="#e6f7ff")
        self.level_frame.pack(pady=5)

        tk.Label(self.level_frame, text="Select Level:", font=("Comic Sans MS", 14), bg="#e6f7ff").grid(row=0, column=0, padx=5)
        tk.Button(self.level_frame, text="Easy", bg="#99ff99", font=("Comic Sans MS", 12, "bold"),
                  command=lambda: self.set_level("Easy")).grid(row=0, column=1, padx=5)
        tk.Button(self.level_frame, text="Medium", bg="#ffff99", font=("Comic Sans MS", 12, "bold"),
                  command=lambda: self.set_level("Medium")).grid(row=0, column=2, padx=5)
        tk.Button(self.level_frame, text="Hard", bg="#ff9999", font=("Comic Sans MS", 12, "bold"),
                  command=lambda: self.set_level("Hard")).grid(row=0, column=3, padx=5)

        # --- Question Display ---
        self.question_label = tk.Label(
            root,
            text="Press 'Next' to start!",
            font=("Comic Sans MS", 22, "bold"),
            bg="#ccf2ff",
            fg="#333",
            width=25,
            height=2,
            relief="ridge",
            bd=3
        )
        self.question_label.pack(pady=30)

        # --- Answer Entry ---
        self.entry = tk.Entry(root, font=("Comic Sans MS", 18), width=10, justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_answer)

        self.tip_label = tk.Label(
            root,
            text="💡 Type your answer and press ENTER!",
            font=("Comic Sans MS", 14, "italic"),
            bg="#e6f7ff",
            fg="#6666cc"
        )
        self.tip_label.pack()

        # --- Buttons ---
        self.button_frame = tk.Frame(root, bg="#e6f7ff")
        self.button_frame.pack(pady=10)

        self.next_btn = tk.Button(
            self.button_frame, text="➡ Next", command=self.new_question,
            font=("Comic Sans MS", 14, "bold"), bg="#66ccff", fg="white", width=10
        )
        self.next_btn.grid(row=0, column=0, padx=10)

        self.reset_btn = tk.Button(
            self.button_frame, text="🔁 Reset", command=self.reset_quiz,
            font=("Comic Sans MS", 14, "bold"), bg="#ff6666", fg="white", width=10
        )
        self.reset_btn.grid(row=0, column=1, padx=10)

        # --- Result Label ---
        self.result_label = tk.Label(root, text="", font=("Comic Sans MS", 16), bg="#e6f7ff")
        self.result_label.pack(pady=10)

        # --- Score Display ---
        self.score_label = tk.Label(root, text=f"🏆 Score: {self.score}", font=("Comic Sans MS", 16, "bold"), bg="#e6f7ff", fg="#3333cc")
        self.score_label.pack(pady=10)

    # --- Set Difficulty Level ---
    def set_level(self, level):
        self.level = level
        self.result_label.config(text=f"Level set to: {level}", fg="#333")
        self.new_question()

    # --- Generate a New Question ---
    def new_question(self):
        self.entry.delete(0, tk.END)
        ops = ["+", "-", "*"]
        op = random.choice(ops)

        if self.level == "Easy":
            a, b = random.randint(1, 10), random.randint(1, 10)
        elif self.level == "Medium":
            a, b = random.randint(10, 50), random.randint(10, 50)
        else:
            a, b = random.randint(50, 100), random.randint(10, 100)

        self.question = f"{a} {op} {b}"
        self.answer = eval(self.question)
        self.question_label.config(text=self.question, bg="#ccf2ff", fg="#333")
        self.result_label.config(text="")

    # --- Check Answer ---
    def check_answer(self, event=None):
        try:
            user_ans = int(self.entry.get())
            if user_ans == self.answer:
                self.score += 1
                self.result_label.config(
                    text=f"✅ Correct! {self.question} = {self.answer}",
                    fg="green"
                )
                self.question_label.config(bg="#b3ffb3")  # green background for correct
            else:
                self.result_label.config(
                    text=f"❌ Wrong! Correct answer: {self.answer}",
                    fg="red"
                )
                self.question_label.config(bg="#ffcccc")  # red background for wrong

            self.score_label.config(text=f"🏆 Score: {self.score}")
            self.entry.delete(0, tk.END)
            self.root.after(1000, self.new_question)  # auto next question after 1 sec
        except ValueError:
            self.result_label.config(text="⚠️ Please enter a number!", fg="orange")

    # --- Reset Quiz ---
    def reset_quiz(self):
        self.score = 0
        self.score_label.config(text=f"🏆 Score: {self.score}")
        self.result_label.config(text="")
        self.question_label.config(text="Press 'Next' to start!", bg="#ccf2ff", fg="#333")
        self.entry.delete(0, tk.END)

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()

