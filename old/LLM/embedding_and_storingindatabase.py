from langchain_community.document_loaders import TextLoader #similarly for pdf use pdfloader
from langchain_text_splitters import RecursiveCharacterTextSplitter #used to divide data in chunks
from langchain_ollama.embeddings import OllamaEmbeddings #used to create embeddings
from langchain_ollama import ChatOllama #used to create output
from langchain_chroma import Chroma


raw_document = TextLoader("./information.txt").load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
documents = text_splitter.split_documents(raw_document)

embedd = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
database = Chroma.from_documents(documents, embedding=embedd)

query = "Jaipur"
result = database.similarity_search(query)

print(len(result))
for i in result:
    print(i)