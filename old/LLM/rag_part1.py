from langchain_community.document_loaders import TextLoader #similarly for pdf use pdfloader
from langchain_text_splitters import RecursiveCharacterTextSplitter #used to divide data in chunks
from langchain_ollama.embeddings import OllamaEmbeddings #used to create embeddings
from langchain_ollama import ChatOllama #used to create output
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


raw_document = TextLoader("./information.txt").load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
documents = text_splitter.split_documents(raw_document)

embedd = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
db = Chroma.from_documents(documents, embedding=embedd)

template = """Answer based only on behalf of following context:

{context}

Question : {question}
"""
prompt = ChatPromptTemplate.from_template(template=template)

model = ChatOllama(
    model= "llama3.2",
    temperature=0
)

retriever = db.as_retriever()

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

chain = (
    {"context" : retriever | format_docs, "question" : RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print(chain.invoke("What is Jaipur?"))