import tkinter as tk
import webbrowser
import threading
import time
import pyautogui

def start_gesture_control():
    status_label.config(text="Launching YouTube & Starting Gesture Control...")

    # Run gesture code in background thread
    threading.Thread(target=launch_youtube_and_gesture).start()

def launch_youtube_and_gesture():
    webbrowser.open("https://www.youtube.com")
    time.sleep(5)  # Wait for YouTube to load

    # Focus the window (adjust coordinates as needed)
    pyautogui.hotkey("win", "d")
    time.sleep(1)
    pyautogui.hotkey("win", "d")
    time.sleep(1)
    pyautogui.moveTo(300, 300)
    pyautogui.click()
    
    # You can now call your gesture code here:
    # from your_script import run_gesture_control
    # run_gesture_control()

    status_label.config(text="Gesture Control Running...")

def quit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("YouTube Gesture Controller")
root.geometry("400x200")

title_label = tk.Label(root, text="🖐️ YouTube Gesture Controller", font=("Helvetica", 16))
title_label.pack(pady=10)

start_button = tk.Button(root, text="Start Gesture Control", font=("Helvetica", 12), command=start_gesture_control)
start_button.pack(pady=10)

status_label = tk.Label(root, text="Waiting to start...", font=("Helvetica", 12))
status_label.pack(pady=5)

quit_button = tk.Button(root, text="Quit", font=("Helvetica", 12), command=quit_app)
quit_button.pack(pady=10)

root.mainloop()
