def loud(text):
    return text.upper()

def quite(text):
    return text.lower()

def hello(func):
    text = func("hello")
    print(text)

hello(loud)
hello(quite)