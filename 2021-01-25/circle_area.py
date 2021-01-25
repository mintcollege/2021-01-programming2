
def circlecalc(r):
    pass


pi = 3.14
def circlearea(r):
    area = pi * r**2
    return area

def circlecirc(r):
    circ = 2 * pi * r
    return circ

def circledict(r):
    data = {
        'area': round(circlearea(r), 2),
        'circumference': round(circlecirc(r), 2)
    }
    return data

# message = circledict(3)
# print(message)
# message = circledict(12)
# print(message)
# message = circledict(89)
# print(message)


num1, num2 = 23, 24
# num1 = 23
# num2 = 24
print(num1)
print(num2)