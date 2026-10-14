#Задание 1

word = 'подземелье'

# print(word[0])
# print(word[1])
# print(word[-1])
# print(word[-2])

#Задание 2

print(word[0:3])
print(word[3:5])

#Задание 3

print(len(word))

#Задание 4

text = "  Ты ЗАШЁЛ в тёмный ЛЕС  "

lowerText = text.lower().lstrip().rstrip()
print(lowerText)


#Задание 5

print(text.replace("тёмный", "светлый"))

#Задание 6

text2 = "гоблин гоблин дракон гоблин"
print(text2.find("гоблин"))

#Задание 7

command = "взять меч"

part = command.split()
print(part[1])
print(part[2])

#Задание 8

usersInput = input("Введите текст").lower().strip()
newUser = usersInput.split()
if newUser == '':
    print("Ты ничего не сказал.")
elif newUser == 'взять':
    print("Ты берёшь предмет.")
elif newUser == "идти":
    print("Ты идёшь.")
elif newUser == "осмотреть":
    print("Ты осматриваешься.")
else:
    print("Я не понял.")

#Задание 9

text = "Hello World from Python"

words = text.split()

reversed_words = words[::-1]

result = " ".join(reversed_words)

print(result)