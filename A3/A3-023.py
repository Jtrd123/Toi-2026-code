import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    A, B = int(input_data[0]), int(input_data[1])
    
    # ผลรวมสูงสุดที่เป็นไปได้คือ B + B + B
    MAX_SUM = B * 3
    
    # 1. สร้างตะแกรงร่อนจำนวนเฉพาะ (Sieve of Eratosthenes)
    is_prime = [True] * (MAX_SUM + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(MAX_SUM**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, MAX_SUM + 1, p):
                is_prime[i] = False
                
    # 2. สร้าง Prefix Sum เพื่อจดว่าตั้งแต่ 0 ถึง i มีจำนวนเฉพาะกี่ตัวแล้ว
    pref = [0] * (MAX_SUM + 1)
    count = 0
    for i in range(MAX_SUM + 1):
        if is_prime[i]:
            count += 1
        pref[i] = count
        
    # 3. เริ่มวนลูปแค่ 2 ชั้น (หาค่า x และ y)
    total_sets = 0
    for x in range(A, B + 1):
        for y in range(x, B + 1):
            
            # ช่วงของจำนวนเฉพาะ (P) ที่จะทำให้ z อยู่ในขอบเขต [y, B] พอดี
            min_P = x + (2 * y)
            max_P = x + y + B
            
            if min_P <= max_P:
                # จำนวนของจำนวนเฉพาะในขอบเขตนี้ คือคำตอบของคู่นี้
                total_sets += pref[max_P] - pref[min_P - 1]
                
    print(total_sets)

if __name__ == '__main__':
    solve()