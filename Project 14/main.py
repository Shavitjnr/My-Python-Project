import tkinter as tk
from tkinter import messagebox
import datetime
import threading
import time
import sys
import os

try:
    from playsound import playsound
    PLAYSOUND_AVAILABLE = True
except ImportError:
    PLAYSOUND_AVAILABLE = False

try:
    import winsound  # For Windows
except ImportError:
    winsound = None

AUDIO_FILE = os.path.join(os.path.dirname(__file__), 'FAIRY - TALE RINGTONE BGM ✨.mp3')

def play_alarm_sound():
    if PLAYSOUND_AVAILABLE and os.path.exists(AUDIO_FILE):
        try:
            playsound(AUDIO_FILE)
            return
        except Exception as e:
            print(f"Error playing sound: {e}")
    if winsound:
        for _ in range(3):
            winsound.Beep(1000, 500)
            time.sleep(0.5)
    else:
        for _ in range(3):
            print('\a')
            sys.stdout.flush()
            time.sleep(0.5)

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.create_widgets()
        self.alarm_thread = None
        self.alarm_set = False

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Set Alarm (HH:MM, 24-hour)").pack()
        self.time_entry = tk.Entry(frame, width=10, justify='center')
        self.time_entry.pack(pady=5)

        self.set_button = tk.Button(frame, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=5)

        self.status_label = tk.Label(frame, text="No alarm set.")
        self.status_label.pack(pady=5)

    def set_alarm(self):
        alarm_time = self.time_entry.get().strip()
        try:
            alarm_dt = datetime.datetime.strptime(alarm_time, "%H:%M")
            now = datetime.datetime.now()
            alarm_dt = now.replace(hour=alarm_dt.hour, minute=alarm_dt.minute, second=0, microsecond=0)
            if alarm_dt < now:
                alarm_dt += datetime.timedelta(days=1)
            self.status_label.config(text=f"Alarm set for {alarm_dt.strftime('%H:%M')}")
            self.alarm_set = True
            if self.alarm_thread and self.alarm_thread.is_alive():
                # Only one alarm at a time
                return
            self.alarm_thread = threading.Thread(target=self.wait_for_alarm, args=(alarm_dt,), daemon=True)
            self.alarm_thread.start()
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM format (24-hour).")

    def wait_for_alarm(self, alarm_dt):
        while self.alarm_set:
            now = datetime.datetime.now()
            if now >= alarm_dt:
                self.status_label.config(text="Alarm ringing!")
                play_alarm_sound()
                messagebox.showinfo("Alarm", "Time's up!")
                self.status_label.config(text="No alarm set.")
                self.alarm_set = False
                break
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
