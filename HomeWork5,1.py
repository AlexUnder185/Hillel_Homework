import string
import keyword

name = input("Ведіть ім'я змінної: ")

# 1. Ім’я не може починатися з цифри
if name and name[0].isdigit():
    print(False)

# 2. Не можна використовувати зареєстровані слова
elif name in keyword.kwlist:
    print(False)

# 3. Не повинно містити великі літери
elif any(ch.isupper() for ch in name):
    print(False)

# 4. Не повинно містити пробіли або заборонені знаки пунктуації (окрім "_")
elif any(ch in string.punctuation.replace("_", "") for ch in name):
    print(False)

# 5. Повне ім’я змінної може містити не більше одного "_"
elif name.count("_") > 1:
    print(False)

# Якщо все гаразд
else:
    print(True)