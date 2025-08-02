num = int(input("Введіть 5-ти значне число: "))
print(num % 10,(num // 10) % 10,(num // 100) % 10,(num // 1000) % 10,(num // 10000) % 10)

number = int(input("Введіть 5-ти значне число: "))
num1 = number % 10
num2 = (number // 10) % 10
num3 = (number // 100) % 10
num4 = (number // 1000) % 10
num5 = (number // 10000)

reversed_number = num1 * 10000 + num2 *1000 + num3 *100 + num4 *10 + num5
print(reversed_number)
