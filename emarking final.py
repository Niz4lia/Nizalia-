import tkinter as tk
from tkinter import messagebox

# -------------------------
# SIMPLE AI LOGIC (no installs)
# -------------------------
import difflib

def fair_similarity(answer, model):
    """Calculate a fair similarity score (not word-to-word)."""
    a = answer.lower().replace('.', '').replace(',', '')
    m = model.lower().replace('.', '').replace(',', '')
    words_a = set(a.split())
    words_m = set(m.split())
    overlap = len(words_a & words_m)
    total = len(words_m)
    word_score = overlap / total if total else 0
    seq_score = difflib.SequenceMatcher(None, a, m).ratio()
    return round((seq_score * 0.6 + word_score * 0.4) * 100, 2)


# -------------------------
# TKINTER APP SETUP
# -------------------------
root = tk.Tk()
root.title("E-Marking and Scrutiny Automation System")
root.geometry("750x500")
root.configure(bg="#d6ebff")

# Shared database (temporary in-memory)
database = {
    "model_answer": "",
    "student_answer": "",
    "marks": 0,
    "approved": False,
    "recheck_requested": False,
    "mark_history": [],
}

# -------------------------
# FRAME SETUP
# -------------------------
def show_frame(frame):
    frame.tkraise()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

role_frame = tk.Frame(root, bg="#d6ebff")
teacher_frame = tk.Frame(root, bg="#d6ebff")
level_frame = tk.Frame(root, bg="#d6ebff")
parent_frame = tk.Frame(root, bg="#d6ebff")

for f in (role_frame, teacher_frame, level_frame, parent_frame):
    f.grid(row=0, column=0, sticky="nsew")

# -------------------------
# ROLE SELECTION FRAME
# -------------------------
tk.Label(role_frame, text="Select Role", font=("Arial", 18, "bold"), bg="#d6ebff").pack(pady=30)
for name, frame in [("Teacher", teacher_frame), ("Level Head", level_frame), ("Parent", parent_frame)]:
    tk.Button(
        role_frame,
        text=name,
        font=("Arial", 14),
        width=20,
        bg="#a7d0f5",
        command=lambda f=frame: show_frame(f)
    ).pack(pady=10)

# -------------------------
# TEACHER FRAME
# -------------------------
tk.Label(teacher_frame, text="👨‍🏫 Teacher Portal", font=("Arial", 16, "bold"), bg="#d6ebff").pack(pady=10)

notify_label = tk.Label(teacher_frame, text="", bg="#d6ebff", font=("Arial", 11, "italic"))
notify_label.pack(pady=5)

tk.Label(teacher_frame, text="Model Answer:", bg="#d6ebff", font=("Arial", 12)).pack()
model_text = tk.Text(teacher_frame, width=80, height=4)
model_text.pack(pady=5)

tk.Label(teacher_frame, text="Student Answer:", bg="#d6ebff", font=("Arial", 12)).pack()
student_text = tk.Text(teacher_frame, width=80, height=4)
student_text.pack(pady=5)

result_label = tk.Label(teacher_frame, text="", bg="#d6ebff", font=("Arial", 12))
result_label.pack(pady=5)

def evaluate_answer():
    model = model_text.get("1.0", tk.END).strip()
    student = student_text.get("1.0", tk.END).strip()

    if not model or not student:
        messagebox.showwarning("Warning", "Both answers are required!")
        return

    score = fair_similarity(student, model)
    database["model_answer"] = model
    database["student_answer"] = student
    database["marks"] = score
    database["approved"] = False
    database["recheck_requested"] = False
    database["mark_history"].append(score)

    result_label.config(text=f"AI Suggested Marks: {score:.2f} / 100")

def submit_marks():
    if database["marks"] == 0:
        messagebox.showwarning("Warning", "Evaluate the answer first!")
        return
    messagebox.showinfo("Submitted", "Marks submitted to Level Head for approval.")
    notify_label.config(text="")
    show_frame(role_frame)

def teacher_on_open():
    if database["recheck_requested"]:
        notify_label.config(text="⚠️ Recheck requested by parent. Please review and resubmit.")
    else:
        notify_label.config(text="")

tk.Button(teacher_frame, text="Evaluate", font=("Arial", 12), bg="#a7d0f5", command=evaluate_answer).pack(pady=5)
tk.Button(teacher_frame, text="Submit to Level Head", font=("Arial", 12), bg="#a7d0f5", command=submit_marks).pack(pady=5)
tk.Button(teacher_frame, text="Back", font=("Arial", 12), bg="#cde7ff", command=lambda: show_frame(role_frame)).pack(pady=10)

# -------------------------
# LEVEL HEAD FRAME
# -------------------------
tk.Label(level_frame, text="👩‍💼 Level Head Portal", font=("Arial", 16, "bold"), bg="#d6ebff").pack(pady=10)
review_label = tk.Label(level_frame, text="", bg="#d6ebff", font=("Arial", 12))
review_label.pack(pady=10)

def load_for_review():
    if not database["model_answer"]:
        review_label.config(text="No submissions yet.")
        return
    review_label.config(
        text=f"Student Answer:\n{database['student_answer']}\n\nAI Marks: {database['marks']}\nStatus: {'Approved' if database['approved'] else 'Pending'}"
    )

def approve_marks():
    if not database["model_answer"]:
        messagebox.showinfo("Info", "No submission to approve.")
        return
    database["approved"] = True
    messagebox.showinfo("Approved", "Marks approved successfully.")
    show_frame(role_frame)

tk.Button(level_frame, text="Load Submission", font=("Arial", 12), bg="#a7d0f5", command=load_for_review).pack(pady=5)
tk.Button(level_frame, text="Approve Marks", font=("Arial", 12), bg="#a7d0f5", command=approve_marks).pack(pady=5)
tk.Button(level_frame, text="Back", font=("Arial", 12), bg="#cde7ff", command=lambda: show_frame(role_frame)).pack(pady=10)

# -------------------------
# PARENT FRAME
# -------------------------
tk.Label(parent_frame, text="👩‍👧 Parent Portal", font=("Arial", 16, "bold"), bg="#d6ebff").pack(pady=10)
parent_result = tk.Label(parent_frame, text="", bg="#d6ebff", font=("Arial", 12))
parent_result.pack(pady=10)

def view_results():
    if not database["model_answer"]:
        parent_result.config(text="No exam record found.")
    elif not database["approved"]:
        parent_result.config(text="Results not approved yet.")
    else:
        hist = ", ".join(str(m) for m in database["mark_history"])
        parent_result.config(
            text=f"✅ Final Marks: {database['marks']} / 100\n\nAnswer:\n{database['student_answer']}\n\nPrevious Marks: {hist}"
        )

def request_recheck():
    if not database["approved"]:
        messagebox.showinfo("Info", "Marks must be approved first.")
        return
    database["recheck_requested"] = True
    database["approved"] = False
    messagebox.showinfo("Recheck Requested", "Your recheck request has been sent to the teacher.")
    show_frame(role_frame)

tk.Button(parent_frame, text="View Result", font=("Arial", 12), bg="#a7d0f5", command=view_results).pack(pady=5)
tk.Button(parent_frame, text="Request Recheck", font=("Arial", 12), bg="#ffb6b6", command=request_recheck).pack(pady=5)
tk.Button(parent_frame, text="Back", font=("Arial", 12), bg="#cde7ff", command=lambda: show_frame(role_frame)).pack(pady=10)

# -------------------------
# START APP
# -------------------------
def open_teacher():
    teacher_on_open()
    show_frame(teacher_frame)

for w in role_frame.winfo_children():
    if isinstance(w, tk.Button) and w.cget("text") == "Teacher":
        w.config(command=open_teacher)

show_frame(role_frame)
root.mainloop()
