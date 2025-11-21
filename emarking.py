import difflib
import json
import datetime
import os
import time

# =========================
# FAIR SEMANTIC COMPARISON
# =========================
STOPWORDS = {"the", "is", "a", "an", "and", "or", "in", "of", "to"}

def fair_similarity(answer, model):
    # Normalize and split
    a_words = [w.lower().replace('.', '').replace(',', '') for w in answer.split() if w.lower() not in STOPWORDS]
    m_words = [w.lower().replace('.', '').replace(',', '') for w in model.split() if w.lower() not in STOPWORDS]

    if not m_words:
        return 0.0

    # Count key model words in student's answer
    overlap = sum(1 for w in m_words if w in a_words)
    word_score = overlap / len(m_words)

    # Sequence bonus (small, just for order)
    seq_score = difflib.SequenceMatcher(None, " ".join(a_words), " ".join(m_words)).ratio()
    
    # Weighted: mostly word coverage, small order bonus
    final_score = (word_score * 0.8 + seq_score * 0.2) * 100
    final_score = min(final_score, 100)
    return round(final_score, 2)

# =========================
# DATABASE SIMULATION
# =========================
db_file = "emarking_db.json"

def load_db():
    if not os.path.exists(db_file):
        return {}
    with open(db_file, "r") as f:
        return json.load(f)

def save_db(data):
    with open(db_file, "w") as f:
        json.dump(data, f, indent=4)

# =========================
# USERS
# =========================
users = {
    "teacher": {"password": "123", "role": "Teacher"},
    "level": {"password": "123", "role": "Level Head"},
    "parent": {"password": "123", "role": "Parent"},
}

# =========================
# LOGIN
# =========================
def login():
    print("\n=== E-MARKING & SCRUTINY SYSTEM ===")
    user = input("Username: ").lower()
    pwd = input("Password: ")
    if user in users and users[user]["password"] == pwd:
        print(f"\nWelcome, {users[user]['role']}!\n")
        return users[user]["role"], user
    else:
        print("❌ Invalid credentials.")
        return None, None

# =========================
# TEACHER PANEL
# =========================
def teacher_panel(db):
    while True:
        print("\n--- TEACHER DASHBOARD ---")
        print("1. Evaluate Answers")
        print("2. Submit Marks to Level Head")
        print("3. Check Recheck Requests")
        print("4. View Mark History")
        print("5. Logout")
        choice = input("Choose: ")

        if choice == "1":
            student_name = input("Enter Student Name: ").strip().lower()
            model = input("Enter Model Answer:\n> ")
            student = input("Enter Student Answer:\n> ")
            print("\nEvaluating...", end="")
            for _ in range(3):
                time.sleep(0.4)
                print(".", end="")
            print()
            score = fair_similarity(student, model)
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")

            # Create student record if not exists
            if student_name not in db:
                db[student_name] = {"student_answer": "", "marks": 0, "approved": False, "recheck_requested": False, "mark_history": []}

            db[student_name]["student_answer"] = student
            db[student_name]["marks"] = score
            db[student_name]["mark_history"].append(f"{score} ({timestamp})")
            db[student_name]["model_answer"] = model
            save_db(db)
            print(f"✅ AI Suggested Marks for {student_name}: {score}\n")

        elif choice == "2":
            for s in db:
                db[s]["approved"] = False
                db[s]["recheck_requested"] = False
            save_db(db)
            print("📨 Marks sent to Level Head for review.\n")

        elif choice == "3":
            for s in db:
                if db[s]["recheck_requested"]:
                    print(f"⚠️ {s} requested a recheck!")
            print("Check completed.\n")

        elif choice == "4":
            print("\nMark History:")
            for s, data in db.items():
                print(f"\nStudent: {s}")
                for m in data["mark_history"]:
                    print(" -", m)
            print()

        elif choice == "5":
            print("Logging out...\n")
            break

        else:
            print("Invalid choice.\n")

# =========================
# LEVEL HEAD PANEL
# =========================
def level_panel(db):
    while True:
        print("\n--- LEVEL HEAD DASHBOARD ---")
        print("1. Load Submission")
        print("2. Edit Marks")
        print("3. Approve Marks")
        print("4. Logout")
        choice = input("Choose: ")

        if choice == "1":
            student_name = input("Enter Student Name: ").strip().lower()
            if student_name not in db:
                print("No submission found.\n")
            else:
                data = db[student_name]
                print("\nStudent Answer:")
                print(data["student_answer"])
                print(f"\nMarks: {data['marks']}")
                print(f"Approved: {data['approved']}\n")

        elif choice == "2":
            student_name = input("Enter Student Name: ").strip().lower()
            if student_name not in db:
                print("No submission found.\n")
            else:
                try:
                    new = float(input("Enter new marks: "))
                    db[student_name]["marks"] = new
                    save_db(db)
                    print(f"✅ Marks updated to {new}.")
                except:
                    print("Invalid number.\n")

        elif choice == "3":
            student_name = input("Enter Student Name: ").strip().lower()
            if student_name not in db:
                print("No submission found.\n")
            else:
                db[student_name]["approved"] = True
                save_db(db)
                print(f"✅ Marks approved for {student_name}.\n")

        elif choice == "4":
            print("Logging out...\n")
            break

        else:
            print("Invalid choice.\n")

# =========================
# PARENT PANEL
# =========================
def parent_panel(db, username):
    while True:
        print("\n--- PARENT DASHBOARD ---")
        print("1. View Result")
        print("2. Request Recheck")
        print("3. Logout")
        choice = input("Choose: ")

        if choice == "1":
            if username not in db or not db[username]["approved"]:
                print("📢 Results not yet published.\n")
            else:
                data = db[username]
                print(f"\nFinal Marks: {data['marks']}")
                print(f"Student Answer: {data['student_answer']}")
                print(f"Mark History: {data['mark_history']}\n")

        elif choice == "2":
            if username not in db or not db[username]["approved"]:
                print("Marks not approved yet, wait for publication.\n")
            else:
                db[username]["recheck_requested"] = True
                db[username]["approved"] = False
                save_db(db)
                print("✅ Recheck request sent.\n")

        elif choice == "3":
            print("Logging out...\n")
            break

        else:
            print("Invalid choice.\n")

# =========================
# MAIN PROGRAM LOOP
# =========================
db = load_db()
while True:
    role, username = login()
    if role == "Teacher":
        teacher_panel(db)
    elif role == "Level Head":
        level_panel(db)
    elif role == "Parent":
        parent_panel(db, username)
    else:
        again = input("Try again? (y/n): ")
        if again.lower() != "y":
            break

