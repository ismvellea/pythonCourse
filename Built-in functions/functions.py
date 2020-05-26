def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

def hello2(name):
    print('Hello ' + name)

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

hello()
hello2('Alice')

print('Hello' , end='')
print('Cat' , 'Dog', 'Mouse')
print('Cat' , 'Dog', 'Mouse', sep=',')
