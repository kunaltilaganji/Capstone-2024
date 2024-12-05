import streamlit as st

def main():
    st.title("Capstone Project: Stable Diffusion Inpainting")
    st.write("Hello and welcome to our Capstone Project.")
    st.write("Title: Stable Diffusion Inpainting")
    st.write("BY:")
    st.write("Kunal Tilaganji")
    st.write("Prajwal Rawoorkar")
    st.write("Siddhant Singh")

    st.write("---")  # Adding a horizontal line for separation

    st.subheader("Generate Images")

    # Input prompt for text
    text_input = st.text_input("Enter text prompt:", "Enter your prompt here")

    # Input prompt for number of images
    num_images = st.number_input("Number of images:", min_value=1, max_value=10, value=1, step=1)

    # Button to trigger image generation
    if st.button("Generate Images"):
        # Call your function to generate images based on the input
        generate_images(text_input, num_images)

def generate_images(text, num_images):
    # Your image generation logic here
    # This is where you would use the Stable Diffusion model to generate images
    # You can display the generated images or save them to a directory
    
    st.write(f"Generating {num_images} images based on the prompt: {text}")

if __name__ == "__main__":
    main()
