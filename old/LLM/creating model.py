import ollama

ollama.pull('llama3.2')
#creating model
model_file = '''
FROM llama3.2
SYSTEM You are JARVIS and user is iron man'''
ollama.create(model='JARVIS',modelfile=model_file)

#list of all models
print(ollama.list())

ollama.delete(model='JARVIS')