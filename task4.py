# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.



s = input()

s = s.upper()
s = s.replace(' ','_')
file = open ('n4', 'a+', encoding="utf-8", )
file.write(s)
print(s)