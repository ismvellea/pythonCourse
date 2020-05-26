def div42By(divideBy): # With errors
    return 42 / divideBy

def div42ByWithoutErrors(divideBy): # Without errors
    try:
        return 42 / divideBy
    except:
        print('Error: Your tried to divide by zero.')


print (div42By(2))
print (div42By(12))
#print (div42By(0)) # With Error
print (div42By(1))
print (div42ByWithoutErrors(2))
print (div42ByWithoutErrors(12))
print (div42ByWithoutErrors(0))
print (div42ByWithoutErrors(1))