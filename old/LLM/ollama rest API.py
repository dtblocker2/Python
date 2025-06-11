#generating offline responses:
from ollama import Client

Client = Client(host='http://localhost:11434')

response = Client.chat(model='llama3.2',messages=[
    {
        'role' : 'system',
        'content' : 'you are sherlock holmes',
    },
    {
        'role' : 'user',
        'content' : 'explain schrodinger wave equation in very concise',
    }
])

print(response['message']['content'])