# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:24:39 2024

@author: User
"""

import google.generativeai as genai
from IPython.display import Markdown, display
import textwrap

# Configure the API key
GOOGLE_API_KEY = 'AIzaSyDaZQujJc-ejLkRD11Vvx6_Sc7FbTEwvn8'
genai.configure(api_key=GOOGLE_API_KEY)

# List available models and select the appropriate one
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Function to convert text to Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Prompt to be passed to the generate_content method
prompt = (
    "you are a writing assistant helping writers in writers block writers will be providing the last content they were written, the writer will provide the last paragraph he has written and the summary of the book or article "
    "YOUR JOB IS TO GIVE 10 CONITNUATION OF TWO PARAGRAPH EACH OF THE WRITING FROM THE LAST WRITTEN PARAGRAPH SO THE WRITER WILL HAVE IDEAS TO CONTINUE WRITING"
    "starting from here last written "
    "last written paragraph=(Nearly ten years had passed since the Dursleys had woken up to find their nephew on the front step, "
    "but Privet Drive had hardly changed at all. The sun rose on the same tidy front gardens and lit up the "
    "brass number four on the Dursleys' front door; it crept into their living room, "
    "which was almost exactly the same as it had been on the night when Mr. Dursley had seen that fateful news report about the owls. "
    "Only the photographs on the mantelpiece really showed how much time had passed. Ten years ago, there had been lots of pictures of what looked like a large pink beach ball wearing different-colored bonnets - but Dudley Dursley was no longer a baby, and now the photographs showed a large blond boy riding his first bicycle, on a carousel at the fair, playing a computer game with his father, being hugged and kissed by his mother. The room held no sign at all that another boy lived in the house, too.) "
    "overall summary of book starting from here" 
    "summary = (The book is about 11 year old Harry Potter, who receives a letter saying that he is invited to attend Hogwarts, school of witchcraft and wizardry. He then learns that a powerful wizard and his minions are after the sorcerer's stone that will make this evil wizard immortal and undefeatable.) "

)

# Generate content
response = model.generate_content(prompt)

# Convert the response text to Markdown and display it
markdown_output = to_markdown(response.text)
display(markdown_output)
