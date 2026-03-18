n = int(input())
vowels = 'aeiouAEIOU'
count = 0

for i in range(n):
    text = input()
    if text in vowels:
        count += 1

print(count)