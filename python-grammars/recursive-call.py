def hello():
    print('Hello, world!')
    hello()
hello()
'''
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
(중략)
RecursionError: maximum recursion depth exceeded while calling a Python object
'''