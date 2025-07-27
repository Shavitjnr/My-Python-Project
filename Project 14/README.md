# Alarm Clock

A modern, GUI-based Alarm Clock application written in Python. Set alarms easily and get notified with a custom MP3 ringtone when the time is reached.

---

## ⏰ Features
- **Intuitive GUI:** Built with Tkinter for a simple and clean interface.
- **Set Alarms:** Enter the desired time (24-hour format) to set an alarm.
- **Custom Ringtone:** Plays the included `FAIRY - TALE RINGTONE BGM ✨.mp3` when the alarm rings.
- **Cross-Platform:** Works on Windows, Linux, and macOS (with Python and playsound).
- **Fallback Beep:** If the MP3 cannot be played, falls back to a system beep.

---

## 🛠️ Requirements
- **Python:** 3.6 or higher
- **Libraries:**
  - `tkinter` (standard with Python)
  - `playsound` (for MP3 playback)

Install dependencies with:
```bash
pip install playsound
```

---

## 🚀 Installation & Usage
1. **Clone or Download this Project Folder**
2. **Install Dependencies:**
   ```bash
   pip install playsound
   ```
3. **Run the Application:**
   ```bash
   python3 main.py
   ```
4. **Set an Alarm:**
   - Enter the alarm time in HH:MM (24-hour) format.
   - Click "Set Alarm".
   - When the time is reached, the ringtone will play and a popup will appear.

---

## 📁 File Structure
```
Project 14/
├── main.py      # Main alarm clock script (Tkinter GUI)
├── requirements.txt  # Python dependencies
├── FAIRY - TALE RINGTONE BGM ✨.mp3  # Alarm ringtone
└── README.md    # Project documentation
```

---

## 📝 About This Project
This Alarm Clock was created to provide a simple, customizable, and visually appealing way to manage alarms on your desktop. It is ideal for students, professionals, or anyone who needs reliable reminders.

Feel free to use, modify, or extend this project for your own needs!
