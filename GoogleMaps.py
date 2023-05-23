import cv2
import numpy as np
import pyautogui
import os
import time
import threading
import tkinter as tk

class ScreenRecorder:
    def __init__(self):
        self.recording = False
        self.save_path = os.path.join(os.path.expanduser("~"), "Desktop", "screen_recording.mp4")
        self.screen_size = pyautogui.size()
        self.fps = 20
        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.out = cv2.VideoWriter(self.save_path, self.fourcc, self.fps, self.screen_size)

        # create a thread to run the recording process
        self.thread = threading.Thread(target=self._record)

        # create the GUI
        self.root = tk.Tk()
        self.root.title("Screen Recorder")
        self.root.geometry("250x100")

        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack(side="top", pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording, state="disabled")
        self.stop_button.pack(side="bottom", pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self._exit)
        self.root.mainloop()

    def _exit(self):
        self.stop_recording()
        self.root.destroy()

    def _record(self):
        while self.recording:
            # capture the current screen frame
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # click the up arrow key
            pyautogui.press("up")

            # write the frame to the video file
            self.out.write(frame)

            # pause for 2 seconds
            time.sleep(2)

        # release the VideoWriter object and close the video file
        self.out.release()

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

            if not self.out.isOpened():
                self.out = cv2.VideoWriter(self.save_path, self.fourcc, self.fps, self.screen_size)

            self.thread.start()

    def stop_recording(self):
        if self.recording:
            self.recording = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

    def __del__(self):
        if self.recording:
            self.stop_recording()

recorder = ScreenRecorder()
