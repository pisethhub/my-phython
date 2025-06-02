#Chatbot
import random
import time
chatPlaces = ["the beach", "anywhere with snow", "any big city", "walking in the hills"]
print("Welcome to Chatbot")
name = input("What is your name? ")
print("Hi there", name, "it's great to meet you!")
place = input("Where is your favourite place to be? ")
time.sleep(2)
print("That sounds great, I really love", random.choice(chatPlaces))
day = input("Have you had a good day? ")
day = day.lower()
if day == "yes":
    print("Good to hear that, me too")
else:
    print("Well I hope tomorrow is better")
print("Really enjoyed the chat, speak to you again soon. ")
