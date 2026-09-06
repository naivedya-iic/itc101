"""
Alarm / Reminder App
----------------------
Schedule one-off reminders for specific times. The app runs in a loop,
checking every few seconds whether it's time to trigger a reminder,
and prints an alert (with a terminal beep) when the time arrives.

Usage: python 25_reminder_app.py
"""

import time
import threading
from datetime import datetime


reminders = []  # list of dicts: {"time": "HH:MM", "message": str, "triggered": bool}
lock = threading.Lock()


def add_reminder():
    time_str = input("Enter reminder time (24hr format, HH:MM): ").strip()
    try:
        datetime.strptime(time_str, "%H:%M")
    except ValueError:
        print("Invalid time format. Use HH:MM (e.g. 14:30).")
        return

    message = input("Enter reminder message: ").strip()
    if not message:
        message = "Reminder!"

    with lock:
        reminders.append({"time": time_str, "message": message, "triggered": False})
    print(f"Reminder set for {time_str}: \"{message}\"")


def list_reminders():
    with lock:
        if not reminders:
            print("No reminders set.")
            return
        print("\nActive reminders:")
        for r in reminders:
            status = "done" if r["triggered"] else "pending"
            print(f"  [{status}] {r['time']} - {r['message']}")


def checker_loop():
    while True:
        now = datetime.now().strftime("%H:%M")
        with lock:
            for r in reminders:
                if not r["triggered"] and r["time"] == now:
                    print(f"\n\a⏰ REMINDER: {r['message']} (at {r['time']})\n")
                    r["triggered"] = True
        time.sleep(20)  # check every 20 seconds


def main():
    print("=== ALARM / REMINDER APP ===")
    print("The checker runs in the background while you use the menu.\n")

    checker_thread = threading.Thread(target=checker_loop, daemon=True)
    checker_thread.start()

    menu = """
1. Add reminder
2. List reminders
3. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            add_reminder()
        elif choice == "2":
            list_reminders()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
