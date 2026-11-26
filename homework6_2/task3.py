# Завдання 3
# Користувач вводить слова, поки не введе END. Виведіть в
# кінці ті слова, які починаються і закінчуються на одну і ту
# саму літеру(регістр не важливий).
result = ""

while True:
    word = input("Введіть слово: ")
    if word == "END":
        break
    else:
        if word[0].lower() == word[-1].lower():
            result += word + " "

print(result)
