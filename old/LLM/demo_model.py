import ollama

ollama.pull('llama3.2')

#there can be 2 ways to generate answers in this
#1. generating result ie answer to given question

question = "who is Rahul gandhi and answer in 2 lines"#input('sentence completion method: ')
result = ollama.generate(model='llama3.2',
                        prompt = question)

#2. in this we interact with chat model like a whatsapp chat
question_2 = "who is PM of India and answer in 2 lines?"#input('chat method: ')
response = ollama.chat(model='llama3.2',
                       messages=[{
                           'role' : 'user',
                           'content' : question_2,
                       }])

print(f'result:{result} \nresponse {response}\n\nto show only response use: {response['message']['content']}')
lol = input('')