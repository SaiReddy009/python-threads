import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Tkinter Example")

# Set the window size
root.geometry("300x150")

# Create a label
label = tk.Label(root, text="Click the button to change this text.")
label.pack(pady=20)