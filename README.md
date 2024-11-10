# Article-Summarizer-using-LLM
This tool extracts text from PDF articles, summarizes content, and answers questions based on the text. It's powered by Streamlit and leverages Groq's Llama model API for natural language understanding and summarization.


It's an interactive web application for summarizing PDF documents and answering questions based on the extracted content using Llama's language model API. This app leverages Streamlit for the user interface, PyMuPDF for PDF text extraction, and custom CSS for an aesthetically pleasing UI.

## Features

- **Upload PDF Files**: Upload and process PDF documents to extract text content.
- **Summarization**: Summarizes the content of uploaded articles or documents.
- **Question-Answering**: Enables users to ask questions based on the content for quick insights.

## Tech Stack

- **Streamlit**: For creating an interactive user interface.
- **PyMuPDF (fitz)**: For extracting text from PDF files.
- **Groq API**: For leveraging Llama's summarization and question-answering capabilities.
- **CSS**: For custom styling to enhance UI aesthetics.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Article-Summarizer-using-LLM.git
   cd Article-Summarizer-using-LLM

   pip install streamlit fitz groq Pillow
   streamlit run app.py
   
Usage
Upload a PDF document.
Click "Summarize Text" to get a concise summary of the content.
Use the "Ask a Question" feature to inquire further about specific details within the PDF content.

