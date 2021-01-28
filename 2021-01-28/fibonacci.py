

# 1, 1, 2, 3, 5, 8...

def fibonacci_generator(num):
    """
    Write what the function does.
    Generates a series of fibonacci numbers without exceeding the nember num.
    """
    a = 1
    b = 1
    c = a + b
    fibo_list = [a, b, c]
    # adds items to the list
    while True:
        a, b = b, a + b
        c = a + b
        # checks if the c should NOT be added to the list
        if c > num:
            # exit the loop because c is now too big
            break
        fibo_list.append(c)
    return fibo_list

print(fibonacci_generator(50))