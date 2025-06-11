from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import ollama

ollama.pull('llama3.2')

llm = ChatOllama(
    model = 'llama3.2',
    temperature = 0
)

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', "you have to give two line definition of the word given by user"),
        ('human', 'the word is {user_input}')
    ]
)

message = chat_template.format_messages(user_input = 'backlog')
response_1 = llm.invoke(message)

chain = chat_template | llm | StrOutputParser()
response_2 = chain.invoke({'user_input' : 'backlog'})

print(message)
print("Response A: ", response_1)
print("Response B: ", response_2)
lo = input('')