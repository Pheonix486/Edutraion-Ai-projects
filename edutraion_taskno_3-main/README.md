# 🧠 Task 3: Image Captioning AI with GUI (BLIP-based)

This project is part of Task 3 in the AI Mini Projects series.This is a simple Image Captioning desktop app using the BLIP model.  
It combines **Computer Vision** and **Natural Language Processing (NLP)** to **generate meaningful captions for images** using a **Graphical User Interface (GUI)**.

---

### 🧩 Project Description

This image captioning application uses the **BLIP (Bootstrapped Language Image Pretraining)** model developed by Salesforce.  
It uses a **Transformer-based model** to understand and describe images in natural language.

We’ve wrapped this functionality in a **Python GUI** built with Tkinter, so users can easily:
- Select **one or multiple images** from their system
- Get **descriptive captions** generated automatically

---

### ✅ Features

- 🖼️ Accepts multiple image files in one click
- 🧠 Uses pretrained **BLIP model** for accurate image understanding
- 🪟 Clean GUI interface (no need for command line)
- 📝 Displays only the final caption (no logs or extra info)
- 📂 Supports images from **any folder** with **any filename**
- Caption **multiple images at once**
- Clean and simple **Graphical User Interface (GUI)**
- Uses the powerful **Salesforce BLIP model** for high-quality captions

---

### 💻 Requirements

Before running the project, make sure the following Python libraries are installed:

pip install transformers torch pillow

🔹 transformers: Hugging Face library for NLP + Vision models
🔹 torch: Required for model inference
🔹 pillow: For image handling

🚀 How to Run
Download or Clone this repository and go to the Task3-Image-Captioning folder.

Make sure you have Python installed and available in Command Prompt.

Run the following command:

bash

python image caption.py(filename.py)

The GUI window will open.

Click on the “Select Images” button, and choose one or more images from your computer.

The app will generate captions and display them in a scrollable text box.


🛠️ Model Details
This app uses the following model:

🤖 BLIP (base model)
🔗 Model link: https://huggingface.co/Salesforce/blip-image-captioning-base

The model is downloaded automatically and cached the first time you run the app (internet required only once).

📌 Notes
You do not need to rename images or keep them in the same folder.

Caption generation may take a few seconds per image (depending on your computer).

Internet is required only on first run to download the model weights.

---

