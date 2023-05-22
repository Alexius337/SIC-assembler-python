import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def parse_file(file_path):
    # Parse the SIC assembler file
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def Pass1(lines):
    return '\n'.join(lines)

def Pass2(lines):
    output_lines = ["Object Code: " + line for line in lines]
    return '\n'.join(output_lines)

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File",
                                          filetypes = (("Assembly files", "*.asm*"), ("all files", "*.*")))
    entry_path.delete(0, 'end')
    entry_path.insert(0, filename)

def openPass1():
    file_path = entry_path.get()
    lines = parse_file(file_path)
    output = Pass1(lines)
    text_box.delete(1.0, 'end')
    text_box.insert('end', output)

def openPass2():
    file_path = entry_path.get()
    lines = parse_file(file_path)
    output = Pass2(lines)
    text_box.delete(1.0, 'end')
    text_box.insert('end', output)

root = tk.Tk()
root.title('SIC Assembler')
root.geometry('800x600')

# Load the background image
bg_image = Image.open("background.jpg") # replace with your image path
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(root, text="Assembler SIC", font=("Helvetica", 24), bg='white')
title_label.pack(pady=10)

entry_path = tk.Entry(root, width=100)
entry_path.pack(pady=20)

btn_browse = tk.Button(root, text="Browse Files", command=browseFiles)
btn_browse.pack(pady=10)

btn_pass1 = tk.Button(root, text="Run Pass1", command=openPass1)
btn_pass1.pack(pady=10)

btn_pass2 = tk.Button(root, text="Run Pass2", command=openPass2)
btn_pass2.pack(pady=10)

text_box = tk.Text(root, height=10, width=40)
text_box.pack(pady=10)

root.mainloop()
