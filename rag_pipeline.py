from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
import pandas as pd

# Load Mistral from Ollama
llm = Ollama(model="mistral")

# Load hospital data
df = pd.read_csv("data/patients.csv")
docs = [Document(page_content=row.to_json()) for _, row in df.iterrows()]

# Embed and index
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = FAISS.from_documents(docs, embedding)

# QA Chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(),
    chain_type="stuff"
)

def ask_question(query):
    return qa.run(query)
