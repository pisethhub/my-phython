# sub program
import random

# def is used to define the sub program and give it a name
def randomstudent():
    list = ["Piseth", "Ponleu", "sak", "Fish", "A doughnut", "Soup"]
    print(random.choice(list))
    
randomstudent()


def add(num1, num2):
    return num1 + num2
print(add(2, 3))
