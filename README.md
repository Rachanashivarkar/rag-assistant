RAG Assistant (Local AI Document Chatbot)
📘 Overview

RAG Assistant is a Retrieval-Augmented Generation (RAG) based chatbot built using LangChain.
It allows users to upload and query their own text documents.
Unlike typical implementations that require an OpenAI API key, this project uses Hugging Face local embeddings (all-MiniLM-L6-v2) — making it completely free and offline.

🚀 Features

✅ Load and process any text document (.txt)
✅ Use local Sentence-BERT embeddings for semantic search
✅ Ask natural language questions about document content
✅ Works offline — no API keys or internet required
✅ Lightweight, clean, and beginner-friendly Python setup

🏗️ Tech Stack
Component	Technology Used
Programming Language	Python 3.10+
Framework	LangChain
Embeddings	HuggingFace Sentence-BERT (all-MiniLM-L6-v2)
Vector Database	ChromaDB
Model	Local Retrieval QA Chain
Interface	Command-Line Interface (CLI)
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/rag-assistant.git
cd rag-assistant

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate # On Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt


(If you don’t have a requirements.txt, you can manually install them)

pip install langchain langchain-community langchain-core langchain-openai chromadb sentence-transformers

🧩 Project Structure
rag-assistant/
│
├── app.py                # Main Python file (RAG chatbot logic)
├── documents/            # Folder containing your text files
├── requirements.txt       # Dependencies list
└── README.md              # Project description

🧠 How It Works

The program loads your .txt documents using LangChain TextLoader.

It converts the text into embeddings using Sentence-BERT from HuggingFace.

These embeddings are stored in a Chroma vector database for similarity search.

When you ask a question, it retrieves the most relevant chunks and generates a contextual answer.

▶️ Running the Project

Run this command in your terminal:

python app.py


You’ll see:

🤖 AI Assistant is ready (free local mode)! Type 'exit' to quit.

You:


Type your questions, for example:

You: What is this document about?


The assistant will respond based on your document content.

👩‍💻 Author

Rachana Shivarkar
🎓 Computer Engineering Student
💡 Passionate about AI, Machine Learning, and Software Development

📜 License

This project is licensed under the MIT License — free to use and modify.