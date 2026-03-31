s = input().strip()
s_up = s.upper()

if all(c in 'IT' for c in s_up):
    print(f"unknown {len(s)}")
else:
    max_a = 0
    curr_a = 0
    is_valid = True
    err_idx = -1

    # 2. วนลูปเช็คทีละตัวอักษร
    for i in range(len(s_up)):
        c = s_up[i]
        
        # กฎข้อ 0: ตัวอักษรต้องอยู่ใน R, A, B, I, T เท่านั้น
        if c not in 'RABIT':
            is_valid = False
            err_idx = i
            break
            
        prev = s_up[i-1] if i > 0 else ''

        # กฎข้อ 2: หลัง R ต้องเป็น A
        if prev == 'R' and c != 'A':
            is_valid = False
            err_idx = i
            break
            
        # กฎข้อ 4: หลัง B ต้องเป็น I หรือ T
        if prev == 'B' and c not in 'IT':
            is_valid = False
            err_idx = i
            break
            
        # กฎข้อ 3: A ต้องตามหลัง R หรือ A เท่านั้น
        if c == 'A' and prev not in 'RA':
            is_valid = False
            err_idx = i
            break
            
        # กฎข้อ 5: ห้ามลงท้ายด้วย R หรือ B
        if i == len(s_up) - 1 and c in 'RB':
            is_valid = False
            err_idx = i
            break

        # 3. นับจำนวน A ที่ติดกัน
        if c == 'A':
            curr_a += 1
            max_a = max(max_a, curr_a)
        else:
            curr_a = 0 # รีเซ็ตเมื่อเจอตัวอื่น

    # 4. แสดงผลลัพธ์
    if is_valid:
        print(f"yes {max_a}")
    else:
        print(f"no {err_idx}")