import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import os

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to caption a single image
def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Function to handle image selection
def select_images():
    file_paths = filedialog.askopenfilenames(title="Select Images",
                                             filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if not file_paths:
        return

    # Clear previous results
    text_output.delete('1.0', tk.END)

    # Caption each image
    for file_path in file_paths:
        try:
            caption = generate_caption(file_path)
            filename = os.path.basename(file_path)
            text_output.insert(tk.END, f"{filename}:\n{caption}\n\n")
        except Exception as e:
            text_output.insert(tk.END, f"Error with {file_path}:\n{str(e)}\n\n")

# GUI Setup
root = tk.Tk()
root.title("Image Captioning App - BLIP")

# Window size
root.geometry("600x500")
root.resizable(False, False)

# Title label
label = tk.Label(root, text="Click to Select Images for Captioning", font=("Helvetica", 14))
label.pack(pady=10)

# Select Button
button = tk.Button(root, text="Select Images", font=("Helvetica", 12), command=select_images)
button.pack(pady=10)

# Output Text Box
text_output = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 11))
text_output.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Run the GUI
root.mainloop()

input("\nPress Enter to exit...")  # Prevents auto-closing
