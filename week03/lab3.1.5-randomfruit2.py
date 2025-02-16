# This program prints out a random fruit
import random
fruits = ('Apple', 'Guava', 'Banana', 'Watermelon')
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))