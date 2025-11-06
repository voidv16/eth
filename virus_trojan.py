import ctypes
from pynput import mouse
import tkinter as tk
from tkinter import messagebox
import os

def on_click(x, y, button, pressed):
  if button == mouse.Button.right and pressed:
  # Create a simple popup dialog asking for shutdown
    root = tk.Tk()
    root.withdraw() # Hide main window
    answer = messagebox.askyesno("Shutdown?", "Do you want to shut down the computer?")
    root.destroy()
    if answer:
      # Shutdown command for Windows
      os.system("shutdown /s /t 10") # shutdown in 10 seconds
      print("Shutdown initiated in 10 seconds.")
      return False # stop listener after shutdown command

# Start listening to mouse clicks
with mouse.Listener(on_click=on_click) as listener:
  listener.join()