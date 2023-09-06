import tkinter as tk

root = tk.Tk()
root.title("Tkinter World")

# Set the window size
root.geometry("300x150")

# label = tk.Label(root, text="Hello, Studytonight!")  Step 1
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()

entry = tk.Entry(root)
entry.pack()