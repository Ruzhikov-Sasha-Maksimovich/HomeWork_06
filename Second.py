from random import *
import os

x1 = randint(1, 28)
count = 1
name = str(input("Введите ник: "))
war = "Соперник"
size = 2021
massage = ["Ходи", "Давай"]
brat = int(input("сколько будешь брать каждый раз: "))

x = randint(1, 2)
if x == 1:
    print(f'{name} ПОБЕДИЛ')
if x == 0:
    print(f'{war} ПОБЕДИЛ')
print(f"Бот брал по {x1}")