

r, c = map(int, input().split())

# 2. รับตำแหน่งบ้านของกระต่ายน้อย
rabbit_r, rabbit_c = map(int, input().split())

# 3. รับจำนวนผู้ติดเชื้อ
n = int(input())

# สร้างแผนที่เมืองขนาด R x C กำหนดความเสี่ยงเริ่มต้นเป็น 0 ทุกช่อง
grid = []
for _ in range(r):
    row = [0] * c
    grid.append(row)
# grid = [[0 for _ in range(r)] for _ in range(c)]

# 4. วนลูปตามจำนวนผู้ติดเชื้อ
for _ in range(n):
    ir, ic = map(int, input().split()) # ตำแหน่งคนติดเชื้อ
    
    # ตีกรอบรัศมี 2 ช่องรอบๆ ตัวคนติดเชื้อ (ขอบเขตคือ -2 ถึง +2)
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            nr = ir + dr  # แถวเป้าหมาย
            nc = ic + dc  # คอลัมน์เป้าหมาย
            
            # เช็คว่าช่องเป้าหมายไม่ได้ทะลุออกนอกแผนที่
            if 0 <= nr < r and 0 <= nc < c:
                # คำนวณระยะห่าง (ใช้ค่า max ของการกระจัดแนวแกน X หรือ Y)
                dist = max(abs(dr), abs(dc))
                
                # กำหนดความเสี่ยงตามระยะห่าง
                if dist == 0:
                    risk = 100
                elif dist == 1:
                    risk = 60
                elif dist == 2:
                    risk = 20
                else:
                    risk = 0
                
                # อัปเดตช่องนั้นๆ โดยยึดความเสี่ยงที่สูงที่สุด (เผื่อมีคนติดเชื้อทับซ้อนกัน)
                grid[nr][nc] = max(grid[nr][nc], risk)

# 5. นับจำนวนพื้นที่ปลอดภัย (ความเสี่ยงเป็น 0)
safe_count = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == 0:
            safe_count += 1

# 6. แสดงผลลัพธ์
print(safe_count)
print(f"{grid[rabbit_r][rabbit_c]}%")