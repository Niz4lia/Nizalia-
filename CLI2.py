# pomodoro_timer_sound.py

import time
import os
import platform

def beep():
    """Plays a sound alert depending on the OS."""
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)  # frequency=1000Hz, duration=500ms
    else:
        # Works on macOS and Linux (uses the system bell)
        print("\a", end="", flush=True)

def countdown(seconds, label):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{label}: {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"\n✅ {label} finished!")
    beep()  # play alert sound

def pomodoro_timer(work_time=25, break_time=5):
    print(f"🍅 Pomodoro started! Work for {work_time} minutes.")
    countdown(work_time * 60, "Work session")

    print(f"\n⏳ Time for a {break_time}-minute break!")
    countdown(break_time * 60, "Break time")

while True:
    print("\n⏰ POMODORO TIMER")
    print("1. Start 25/5 Pomodoro")
    print("2. Custom time")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        pomodoro_timer()
    elif choice == "2":
        work = int(input("Enter work minutes: "))
        brk = int(input("Enter break minutes: "))
        pomodoro_timer(work, brk)
    elif choice == "3":
        print("Goodbye! Stay productive!")
        break
    else:
        print("Invalid choice.")
