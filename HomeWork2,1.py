num = int(input("Введіть 4-х значне число:  "))
number1 = (num // 1000)
number2 = (num // 100) % 10
number3 = (num // 10) % 10
number4 = (num % 10)

print(number1)
print(number2)
print(number3)
print(number4)
