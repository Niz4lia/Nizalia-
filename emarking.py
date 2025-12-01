import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import json, os
from difflib import SequenceMatcher


DATA_FILE = "emarking_data.json"

# -------------------- DATA SETUP --------------------
def setup_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "users": {
                "admin": {"role": "Admin", "password": "admin123"},
                "ali": {"role": "Teacher", "password": "teach123", "class": "10A"},
                "mrs_khan": {"role": "Parent", "password": "parent123", "child": "Sara Khan"},
                "head_upper": {"role": "LevelHead", "password": "head123", "level": "9-12"}
            },
            "students": {
                "Sara Khan": {
                    "class": "10A",
                    "subject": "English",
                    "reference": "Photosynthesis is the process by which green plants make food using sunlight.",
                    "answer": "Photosynthesis helps plants create food with sunlight.",
                    "marks": None,
                    "grade": None,
                    "approved": False,
                    "recheck": False
                }
            }
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# -------------------- MAIN APP CLASS --------------------
class EMarkingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Marking System v2")
        self.root.geometry("400x300")
        self.root.configure(bg="#d4ebf2")  # light blue theme

        setup_data()

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Label(root, text="E-Marking System", font=("Helvetica", 16, "bold"), bg="#d4ebf2", fg="#034f84").pack(pady=20)
        tk.Label(root, text="Username:", bg="#d4ebf2").pack()
        tk.Entry(root, textvariable=self.username_var).pack()

        tk.Label(root, text="Password:", bg="#d4ebf2").pack()
        tk.Entry(root, textvariable=self.password_var, show="*").pack()

        tk.Button(root, text="Login", command=self.login, bg="#98c1d9", fg="black").pack(pady=10)

    def login(self):
        data = load_data()
        user = self.username_var.get()
        pw = self.password_var.get()

        if user in data["users"] and data["users"][user]["password"] == pw:
            role = data["users"][user]["role"]
            self.root.destroy()

            if role == "Admin":
                AdminWindow(user)
            elif role == "Teacher":
                TeacherWindow(user)
            elif role == "Parent":
                ParentWindow(user)
            elif role == "LevelHead":
                LevelHeadWindow(user)
        else:
            messagebox.showerror("Error", "Invalid username or password")

# -------------------- COMMON FUNCTIONS --------------------
def calc_similarity(ref, ans):
    return round(SequenceMatcher(None, ref.lower(), ans.lower()).ratio() * 100, 2)

def calc_grade(percentage):
    if percentage >= 90: return "A"
    elif percentage >= 75: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 45: return "D"
    else: return "F"

# -------------------- ADMIN WINDOW --------------------
# -------------------- TEACHER WINDOW --------------------
class TeacherWindow:
    def __init__(self, username):
        self.username = username
        self.win = tk.Tk()
        self.win.title("Teacher Panel")
        self.win.geometry("600x500")
        self.win.configure(bg="#cfeaf5")

        tk.Label(self.win, text=f"Teacher Panel ({username})", font=("Helvetica", 14, "bold"),
                 bg="#cfeaf5", fg="#033e6b").pack(pady=10)

        self.tree = ttk.Treeview(self.win, columns=("Subject", "Marks", "Grade", "Recheck"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, pady=10)

        self.refresh_data()

        btn_frame = tk.Frame(self.win, bg="#cfeaf5")
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Mark Automatically", command=self.auto_mark, bg="#98c1d9").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Edit Marks", command=self.edit_marks, bg="#98c1d9").grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Handle Recheck", command=self.handle_recheck, bg="#98c1d9").grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Logout", command=self.logout, bg="#98c1d9").grid(row=0, column=3, padx=5)

        self.win.mainloop()

    def refresh_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        data = load_data()
        for student, info in data["students"].items():
            self.tree.insert("", "end", values=(info["subject"], info["marks"], info["grade"], info["recheck"]))

    def auto_mark(self):
        data = load_data()
        for student, info in data["students"].items():
            percent = calc_similarity(info["reference"], info["answer"])
            grade = calc_grade(percent)
            data["students"][student]["marks"] = percent
            data["students"][student]["grade"] = grade
        save_data(data)
        messagebox.showinfo("Done", "Auto marking completed.")
        self.refresh_data()

    def edit_marks(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Warning", "Select a student first.")
            return
        item = self.tree.item(sel[0])
        subject = item["values"][0]
        data = load_data()

        # find student by subject
        for student, info in data["students"].items():
            if info["subject"] == subject:
                new_marks = tk.simpledialog.askfloat("Edit Marks", f"Enter new marks for {student}:")
                if new_marks is not None:
                    data["students"][student]["marks"] = new_marks
                    data["students"][student]["grade"] = calc_grade(new_marks)
                    save_data(data)
                    messagebox.showinfo("Updated", "Marks updated successfully.")
                    self.refresh_data()
                    return

    def handle_recheck(self):
        data = load_data()
        for student, info in data["students"].items():
            if info["recheck"]:
                info["recheck"] = False
                messagebox.showinfo("Recheck", f"Recheck for {student} has been addressed.")
        save_data(data)
        self.refresh_data()

    def logout(self):
        self.win.destroy()
        main()


# -------------------- PARENT WINDOW --------------------
class ParentWindow:
    def __init__(self, username):
        self.username = username
        self.win = tk.Tk()
        self.win.title("Parent Panel")
        self.win.geometry("500x400")
        self.win.configure(bg="#cfeaf5")

        data = load_data()
        child = data["users"][username]["child"]

        tk.Label(self.win, text=f"Parent Panel ({username})", font=("Helvetica", 14, "bold"),
                 bg="#cfeaf5", fg="#033e6b").pack(pady=10)
        tk.Label(self.win, text=f"Child: {child}", bg="#cfeaf5").pack(pady=5)

        info = data["students"][child]
        self.info_text = tk.Text(self.win, height=10, width=55)
        self.info_text.pack(pady=10)
        self.display_info(info)

        tk.Button(self.win, text="Request Recheck", command=lambda: self.request_recheck(child), bg="#98c1d9").pack(pady=5)
        tk.Button(self.win, text="Logout", command=self.logout, bg="#98c1d9").pack(pady=5)

        self.win.mainloop()

    def display_info(self, info):
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, f"Subject: {info['subject']}\n")
        self.info_text.insert(tk.END, f"Marks: {info['marks']}\n")
        self.info_text.insert(tk.END, f"Grade: {info['grade']}\n")
        self.info_text.insert(tk.END, f"Approved: {info['approved']}\n")
        self.info_text.insert(tk.END, f"Recheck Requested: {info['recheck']}\n")

    def request_recheck(self, child):
        data = load_data()
        if data["students"][child]["recheck"]:
            messagebox.showinfo("Info", "Recheck already requested.")
        else:
            data["students"][child]["recheck"] = True
            save_data(data)
            messagebox.showinfo("Requested", "Recheck request sent to teacher.")
            self.display_info(data["students"][child])

    def logout(self):
        self.win.destroy()
        main()

# -------------------- LEVEL HEAD WINDOW --------------------
class LevelHeadWindow:
    def __init__(self, username):
        self.username = username
        self.win = tk.Tk()
        self.win.title("Level Head Panel")
        self.win.geometry("600x500")
        self.win.configure(bg="#cfeaf5")

        tk.Label(self.win, text=f"Level Head Panel ({username})", font=("Helvetica", 14, "bold"),
                 bg="#cfeaf5", fg="#033e6b").pack(pady=10)

        self.tree = ttk.Treeview(self.win, columns=("Student", "Subject", "Marks", "Grade", "Approved"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, pady=10)

        tk.Button(self.win, text="Approve Selected", command=self.approve_result, bg="#98c1d9").pack(pady=5)
        tk.Button(self.win, text="Logout", command=self.logout, bg="#98c1d9").pack(pady=5)

        self.refresh_data()
        self.win.mainloop()

    def refresh_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        data = load_data()
        for student, info in data["students"].items():
            self.tree.insert("", "end", values=(student, info["subject"], info["marks"], info["grade"], info["approved"]))

    def approve_result(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Warning", "Select a student first.")
            return
        item = self.tree.item(sel[0])
        student = item["values"][0]
        data = load_data()
        if data["students"][student]["approved"]:
            messagebox.showinfo("Info", "Already approved.")
        else:
            data["students"][student]["approved"] = True
            save_data(data)
            messagebox.showinfo("Approved", f"Result for {student} has been approved.")
        self.refresh_data()

    def logout(self):
        self.win.destroy()
        main()


# -------------------- ADMIN WINDOW --------------------
class AdminWindow:
    def __init__(self, username):
        self.username = username
        self.win = tk.Tk()
        self.win.title("Admin Panel")
        self.win.geometry("600x500")
        self.win.configure(bg="#cfeaf5")

        tk.Label(self.win, text=f"Admin Panel ({username})", font=("Helvetica", 14, "bold"),
                 bg="#cfeaf5", fg="#033e6b").pack(pady=10)

        self.tree = ttk.Treeview(self.win, columns=("Username", "Role"), show="headings")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Role", text="Role")
        self.tree.pack(fill="both", expand=True, pady=10)

        tk.Button(self.win, text="Add User", command=self.add_user, bg="#98c1d9").pack(pady=5)
        tk.Button(self.win, text="Logout", command=self.logout, bg="#98c1d9").pack(pady=5)

        self.refresh_users()
        self.win.mainloop()

    def refresh_users(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        data = load_data()
        for user, info in data["users"].items():
            self.tree.insert("", "end", values=(user, info["role"]))

    def add_user(self):
        add_win = tk.Toplevel(self.win)
        add_win.title("Add New User")
        add_win.geometry("300x300")
        add_win.configure(bg="#cfeaf5")

        tk.Label(add_win, text="Username:", bg="#cfeaf5").pack()
        u = tk.Entry(add_win)
        u.pack()

        tk.Label(add_win, text="Password:", bg="#cfeaf5").pack()
        p = tk.Entry(add_win)
        p.pack()

        tk.Label(add_win, text="Role:", bg="#cfeaf5").pack()
        role_box = ttk.Combobox(add_win, values=["Teacher", "Parent", "LevelHead"], state="readonly")
        role_box.pack()

        def save_new_user():
            user = u.get().strip()
            pw = p.get().strip()
            role = role_box.get().strip()
            if not user or not pw or not role:
                messagebox.showwarning("Warning", "All fields are required.")
                return
            data = load_data()
            if user in data["users"]:
                messagebox.showerror("Error", "Username already exists.")
                return
            data["users"][user] = {"role": role, "password": pw}
            save_data(data)
            messagebox.showinfo("Added", "User added successfully.")
            add_win.destroy()
            self.refresh_users()

        tk.Button(add_win, text="Save", command=save_new_user, bg="#98c1d9").pack(pady=10)


    def logout(self):
        self.win.destroy()
        main()


# -------------------- LAUNCHER --------------------
def main():
    root = tk.Tk()
    app = EMarkingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
