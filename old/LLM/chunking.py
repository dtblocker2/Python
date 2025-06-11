from langchain_community.document_loaders import TextLoader #similarly for pdf use pdfloader
from langchain_text_splitters import RecursiveCharacterTextSplitter #used to divide data in chunks

raw_document = TextLoader("./information.txt").load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
documents = text_splitter.split_documents(raw_document)

print(len(documents))
for i in documents:
    print(i)