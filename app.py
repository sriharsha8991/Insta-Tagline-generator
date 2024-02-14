from dotenv import load_dotenv

load_dotenv() # load all the variables from .env 

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = "AIzaSyBIPucZCQr14TZm9DKfA0ACl0DXLRq2JeE")

#function to load Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_respose(input,image,prompt):

    response = model.generate_content([input,image[0],prompt])
    return response.text


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


#Sreamlit Setup

st.set_page_config(page_title = "Tagline Generator for instagram posts")

st.header("Tagline Generator for instagram posts")

input = st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image of your choice..",type=['jpg','jpeg','png'])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded Image",use_column_width=True)

submit = st.button("Generate Tag line")

input_prompt = """
Generate creative and engaging taglines suitable for Instagram posts. 
The taglines should be concise, catchy, and relevant to the details of the image
 Incorporate popular and contextually appropriate emojis to enhance the emotional appeal and visual interest of each tagline.
 Ensure the language is positive, inclusive, and resonates with a diverse, global audience. 
  reflecting a range of tones from the given images

"""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_respose(input_prompt,image_data,input)
    st.subheader("The Response is : ")
    st.write(response)


