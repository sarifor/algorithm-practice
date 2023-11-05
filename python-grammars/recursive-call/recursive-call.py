def hello(count):
    if count == 0:
        return
    
    print('Hello, world!', count)
    
    count -= 1
    hello(count)

hello(5)
'''
Hello, world! 5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1
'''