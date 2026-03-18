even_count = 0
odd_count = 0

for i in range(3):
    num = int(input())
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"even {even_count}")
print(f"odd {odd_count}")
    

