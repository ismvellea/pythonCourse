spam = 42 # global variable
realEggs = 42

def eggs():
    spam = 42 #local variable

def spam1():
    eggs = 99
    bacon()
    print(eggs)

def spam2():
    realEggs = 'Hello'
    print(realEggs)

def spam3():
    global realEggs
    realEggs = 'Hello'
    print(realEggs)

def bacon():
    ham = 101
    eggs = 0

spam1()
spam2()
print(realEggs)
spam3()
print(realEggs)
