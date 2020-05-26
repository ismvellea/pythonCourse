# While Example with jump

spam = 0
while spam < 5:
    spam += 1
    if spam == 3: 
        continue #jmp to the next while iteration
    print('spam is ' + str(spam))
