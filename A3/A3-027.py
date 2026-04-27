def solve():
    try:
        n, m = map(int, input().split())
    except EOFError:
        return
        
    # 1. รับข้อมูลแผนที่ปัจจุบัน
    grid = []
    for _ in range(n):
        row = input().split()
        grid.append(row)
        
    # 2. สร้างแผนที่ใบใหม่สำหรับชั่วโมงถัดไป (จำลองให้แห้งทั้งหมดก่อน)
    next_grid = [['-' for _ in range(m)] for _ in range(n)]
    
    # 3. วนลูปเช็คแผนที่ใบเก่า
    for r in range(n):
        for c in range(m):
            # ถ้าน้ำท่วมตรงไหน
            if grid[r][c] == '*':
                # 3.1 ที่เดิมก็ยังต้องท่วมอยู่
                next_grid[r][c] = '*'
                
                # 3.2 ไหลลงไปข้างล่าง 1 ช่อง (ต้องเช็คว่าไม่ทะลุขอบล่างของแผนที่)
                if r + 1 < n:
                    next_grid[r + 1][c] = '*'
                    
    # 4. พิมพ์แผนที่ชั่วโมงถัดไป
    for r in range(n):
        print(" ".join(next_grid[r]))

if __name__ == '__main__':
    solve()