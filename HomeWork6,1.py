import string

user_letters = input("Введіть дві літери через дефіс: ")

start, end = user_letters.split("-")

liters = string.ascii_letters
first_litter = liters.index(start)
second_litter = liters.index(end)

print(liters[first_litter:second_litter + 1])



