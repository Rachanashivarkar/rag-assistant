import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOpenAI 
from langchain.chains import RetrievalQA


load_dotenv()


loader = TextLoader("data.txt")
documents = loader.load()


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


db = Chroma.from_documents(documents, embeddings)


retriever = db.as_retriever()


class SimpleResponder:
    def __init__(self, retriever):
        self.retriever = retriever

    def run(self, query):
        docs = self.retriever.get_relevant_documents(query)
        if not docs:
            return "I couldn’t find any relevant information."
        return "Based on your question, here's what I found:\n\n" + docs[0].page_content

qa_chain = SimpleResponder(retriever)


print("🤖 AI Assistant is ready (free local mode)! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break
    response = qa_chain.run(user_input)
    print("Assistant:", response, "\n")
