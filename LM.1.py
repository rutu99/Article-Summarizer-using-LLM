"""
Using FaceBook's Llama model to summarise and question an Research Articles(pdf's)

1. Agenda:
Libraries we need>>
Loading the pdf
Testing the API
Summarize funtion
Question Answering function
Putting it all together in a Streamlit app
># pip install groq pymupdf
># pip install streamlit 
># pip install streamlit pymupdf groq
># pip install groq

Putting it all together
generate the API key frmo Groq API
Code Begins from Here>>*

"""
import streamlit as st
import fitz  # PyMuPDF
from groq import Groq
from PIL import Image

# Initialize the Groq client
client = Groq(api_key='your API key here')

# Page Configuration
st.set_page_config(page_title="Article Summarizer", page_icon="📰", layout="wide")

# Display the image at the top
image_path = "./sum.jpg"  # Update with your image path
image = Image.open(image_path)
st.image(image, use_column_width=True, caption="Welcome to AI SUMMARIZER")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")  # Open PDF from file object
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def summarize_text(text):
    try:
        summary_response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text: {text}"}
            ],
            model="llama-3.1-8b-instant",
        )
        return summary_response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

def ask_question(context, question):
    try:
        answer_response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Context: {context} Question: {question}"}
            ],
            model="llama-3.1-8b-instant",
        )
        return answer_response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Header Section with Styling
st.markdown("""
    <style>
        .main-header { color: #FFF3E0; font-size: 50px; font-weight: bold; text-align: center; margin-bottom: 20px; }
        .subheader { color: #CE93D8; font-size: 24px; font-weight: 600; margin-top: 20px; }
        .custom-upload { border: 2px dashed #1F618D; padding: 10px; border-radius: 10px; background-color: #D1C4E9; }
        .summary-container, .qa-container { 
            background-color: #D1C4E9; padding: 15px; border-radius: 10px; 
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1); 
            color: black; /* Text color set to black */
        }
        .stButton > button { background-color: #3498DB; color: white; border: none; border-radius: 5px; padding: 8px 20px; font-size: 16px; }
        .stTextInput > div > input { padding: 10px; font-size: 16px; border: 2px solid #3498DB; border-radius: 5px; }
        .stTextArea > div > textarea { padding: 10px; font-size: 14px; border: 2px solid #1F618D; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)


st.markdown("<div class='main-header'>📄 Article Summarizer</div>", unsafe_allow_html=True)

# Upload Section
st.markdown("<div class='custom-upload'>Upload your PDF Article here to extract and summarize the content:</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type="pdf")

if uploaded_file is not None:
    # Extract Text
    pdf_text = extract_text_from_pdf(uploaded_file)
    
    # Display Extracted Text Section
    st.markdown("<div class='subheader'>Extracted Text</div>", unsafe_allow_html=True)
    st.markdown("<div class='summary-container'>Here's a preview of the extracted content from your PDF:</div>", unsafe_allow_html=True)
    st.text_area("Extracted Text", value=pdf_text[:500], height=200)  # Display a snippet of the text

    # Summarize Text Section
    summary_button = st.button("🔍 Summarize Text")
    if summary_button:
        with st.spinner("Generating summary..."):
            summary = summarize_text(pdf_text)
            st.markdown("<div class='subheader'>Summary</div>", unsafe_allow_html=True)
            st.markdown("<div class='qa-container'>" + summary + "</div>", unsafe_allow_html=True)

    # Question Section
    question = st.text_input("Ask a question about the PDF content:")
    if question:
        with st.spinner("Fetching answer..."):
            answer = ask_question(pdf_text, question)
            st.markdown("<div class='subheader'>Answer</div>", unsafe_allow_html=True)
            st.markdown("<div class='qa-container'>" + answer + "</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <style>
        footer { visibility: hidden; }
        .footer { font-size: 12px; color: #5D6D7E; text-align: center; margin-top: 50px; }
    </style>
    <div class="footer">Article Summarizer - Powered by Streamlit . Developed by RVP</div>
""", unsafe_allow_html=True)

