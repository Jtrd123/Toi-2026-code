text = input()
count = 0

for i in range(len(text)) :
    if text[i] in "aeiou":
        count += 1

print(count)