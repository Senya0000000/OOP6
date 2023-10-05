punctuation = {".", ",", ";", ":", "!", "?"}
string = input("Введите строку: ")
count = 0
for char in string:
 if char in punctuation:
  count += 1
print("Количество знаков пунктуации:", count)