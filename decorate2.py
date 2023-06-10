def uppercase_decorator(function):

    def wrap():
        text = function()
        return text.upper()

    return wrap

def hello_world():
    return 'hello world'

# decorator = uppercase_decorator(hello_world)
# print(decorator())

@uppercase_decorator
def hello_world():
    return 'hello wordl'

print(hello_world())