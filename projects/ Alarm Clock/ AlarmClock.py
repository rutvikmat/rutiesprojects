import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound  # For Windows only. Use `playsound` for cross-platform.

# --- UI Setup ---
window = tk.Tk()
window.title("Alarm Clock")
window.geometry("350x200")

# --- Global variable to control the alarm loop ---
alarm_is_set = False


# --- Functions ---
def set_alarm():
    """Sets the alarm time based on user input."""
    global alarm_is_set
    alarm_time_str = f"{hour.get()}:{minute.get()}:{second.get()}"

    try:
        # Validate the time format
        datetime.datetime.strptime(alarm_time_str, "%H:%M:%S")
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM:SS format.")
        return

    alarm_is_set = True
    status_label.config(text=f"Alarm set for {alarm_time_str}")

    # Start checking the time
    check_time(alarm_time_str)


def check_time(alarm_time_str):
    """Checks the current time against the alarm time."""
    if not alarm_is_set:
        return  # Stop checking if alarm is cancelled

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time_str:
        status_label.config(text="Time's up!")
        # Beep sound (Frequency, Duration in milliseconds)
        winsound.Beep(1000, 2000)
        messagebox.showinfo("Alarm", "Time to wake up!")
    else:
        # Check again after 1 second
        window.after(1000, lambda: check_time(alarm_time_str))


def cancel_alarm():
    """Cancels the currently set alarm."""
    global alarm_is_set
    alarm_is_set = False
    status_label.config(text="Alarm cancelled.")


# --- UI Elements ---
tk.Label(window, text="Set Alarm Time (HH:MM:SS)", font=("Helvetica", 14)).pack(pady=5)

time_frame = tk.Frame(window)
time_frame.pack()

hour = tk.Spinbox(time_frame, from_=0, to=23, width=3, format="%02.0f", font=("Helvetica", 12))
hour.pack(side=tk.LEFT)
tk.Label(time_frame, text=":", font=("Helvetica", 12)).pack(side=tk.LEFT)
minute = tk.Spinbox(time_frame, from_=0, to=59, width=3, format="%02.0f", font=("Helvetica", 12))
minute.pack(side=tk.LEFT)
tk.Label(time_frame, text=":", font=("Helvetica", 12)).pack(side=tk.LEFT)
second = tk.Spinbox(time_frame, from_=0, to=59, width=3, format="%02.0f", font=("Helvetica", 12))
second.pack(side=tk.LEFT)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Set Alarm", command=set_alarm).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Cancel Alarm", command=cancel_alarm).pack(side=tk.LEFT, padx=5)

status_label = tk.Label(window, text="", font=("Helvetica", 12))
status_label.pack(pady=5)

# --- Run the application ---
window.mainloop()