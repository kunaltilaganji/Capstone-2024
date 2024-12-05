import tkinter as tk
import customtkinter as ctk 
import os
from datetime import datetime

from PIL import Image, ImageTk
from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline 

# Create the app
app = tk.Tk()
app.title("Stable Bud") 
ctk.set_appearance_mode("dark") 

# Function to create directory if it doesn't exist
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to generate and save images
def generate(): 
    # Get prompt and count input
    prompt_text = prompt.get()
    count_value = int(count.get())
    
    # Get current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create directory structure
    dataset_folder = "dataset"
    prompt_folder = os.path.join(dataset_folder, f"{prompt_text}_{date_time}")
    create_directory_if_not_exists(dataset_folder)
    create_directory_if_not_exists(prompt_folder)
    
    # Initialize variables to keep track of maximum image size
    max_width = 0
    max_height = 0
    
    # Generate and save images
    for i in range(count_value):
        with autocast(device): 
            image = pipe(prompt_text, guidance_scale=9.5)["images"][0]
        
        image_path = os.path.join(prompt_folder, f'generatedimage_{i}.png')
        image.save(image_path)
        
        # Get the dimensions of the generated image
        width, height = image.size
        
        # Update maximum image size if necessary
        max_width = max(max_width, width)
        max_height = max(max_height, height)
        
        # Display the generated image
        img = ImageTk.PhotoImage(image)
        image_labels[i].configure(image=img)
        image_labels[i].image = img  # Keep a reference to avoid garbage collection
    
    # Resize the window according to the maximum image size
    app.geometry(f"{max_width + 20}x{max_height * count_value + 200}")

# Create entry widgets for prompt and count
prompt = ctk.CTkEntry(app, placeholder_text="Enter prompt", height=40, width=512, text_color="black", fg_color="white")
prompt.configure(font=("Arial", 20)) 
prompt.pack()

count = ctk.CTkEntry(app, placeholder_text="Enter dataset images", height=40, width=512, text_color="black", fg_color="white")
count.configure(font=("Arial", 20)) 
count.pack()

# Create labels to display generated images
image_labels = []
for i in range(6):  # Assuming maximum of 10 images for display
    label = ctk.CTkLabel(app, height=512, width=512)
    label.pack()
    image_labels.append(label)

# Initialize Stable Diffusion Pipeline
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token) 
pipe.to(device) 

# Create button for generating images
trigger = ctk.CTkButton(app, height=40, width=120, text_color="white", fg_color="blue", command=generate) 
trigger.configure(font=("Arial", 20)) 
trigger.configure(text="Generate") 
trigger.pack() 

app.mainloop()
