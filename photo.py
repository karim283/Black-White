import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

Image.MAX_IMAGE_PIXELS = None

def convert(path):
    img = Image.open(path)
    img = img.resize((img.width, img.height), Image.Resampling.LANCZOS)
    blackwhite = img.convert('L')
    return img, blackwhite

def compares(original, blackwhite):
    original_data = np.array(original)
    blackwhite_data = np.array(blackwhite)

    if len(original_data.shape) == 3:
        blackwhite_data = np.stack((blackwhite_data,) * 3, axis=-1)

    diff = np.abs(original_data - blackwhite_data)
    diff_count = np.sum(np.any(diff > 0, axis=-1))

    return diff, diff_count

def show(original, blackwhite, diff):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].imshow(original)
    axes[0].set_title('Original', fontsize=14, fontweight='bold')
    axes[0].axis('off')

    axes[1].imshow(blackwhite, cmap='gray')
    axes[1].set_title('Black & White', fontsize=14, fontweight='bold')
    axes[1].axis('off')

    axes[2].imshow(diff, cmap='hot')
    axes[2].set_title('Difference', fontsize=14, fontweight='bold')
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()

def process(path):
    try:
        original_img, blackwhite_img = convert(path)
        difference, count = compares(original_img, blackwhite_img)
        show(original_img, blackwhite_img, difference)
        messagebox.showinfo("Result", f"Number of differing pixels: {count}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def upload():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
        path_label.config(text=file_path, fg="green")
        process(file_path)

root = tk.Tk()
root.title("Image Compare Tool")
root.geometry("600x400")
root.configure(bg="#000000")

header = tk.Label(root, text="Image Black & White ", font=("Arial", 20, "bold"), bg="#000000", fg="#f5f5f5")
header.pack(pady=20)

frame = tk.Frame(root, bg="#000000")
frame.pack(expand=True)

upload_button = tk.Button(
    frame,
    text="Upload Image",
    command=upload,
    font=("Arial", 14, "bold"),
    bg="#3333ff",
    fg="white",
    relief="raised",
    width=20,
    height=2
)
upload_button.pack(pady=10)

path_label = tk.Label(frame, text="No file selected", font=("Arial", 12), bg="#000000", fg="red")
path_label.pack(pady=10)

def on_enter(e):
    upload_button.config(bg="#00b300")

def on_leave(e):
    upload_button.config(bg="#3333ff")

upload_button.bind("<Enter>", on_enter)
upload_button.bind("<Leave>", on_leave)


root.mainloop()
