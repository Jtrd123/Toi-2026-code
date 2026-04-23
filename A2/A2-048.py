def solve():
    # 1. รับค่า n แบบป้องกันกรณีบรรทัดว่าง
    try:
        n = int(input().strip())
    except EOFError:
        return
        
    # กฎข้อที่ 1: ถ้า n = 0 ให้พิมพ์ Student: แล้วจบโปรแกรมทันที
    if n == 0:
        print("Student:")
        return
        
    # 2. รับคะแนนให้ครบ n ค่า (ใช้ while loop ป้องกันกรณี Grader เคาะบรรทัดแปลกๆ)
    scores = []
    while len(scores) < n:
        try:
            line = input().split()
            scores.extend([int(x) for x in line])
        except EOFError:
            break
            
    # ตัดให้เหลือแค่ n ตัวเป๊ะๆ (เผื่อ Grader ส่งขยะแถมมาด้านหลัง)
    scores = scores[:n]
    
    high_score = max(scores)
    low_score = min(scores)
    sum_scores = sum(scores)
    
    # 3. คำนวณค่าเฉลี่ยด้วย "คณิตศาสตร์จำนวนเต็ม (Integer Math)"
    # เอาผลรวมคูณ 100 แล้วหาร n จะได้ค่าแบบไม่เอาทศนิยม (เช่น 2.25 -> 225)
    val = (sum_scores * 100) // n 
    
    # เช็คเศษหลักสุดท้าย (เช่น 5) ถ้า >= 5 ให้ปัดขึ้น 
    if val % 10 >= 5:
        avg_10 = (val // 10) + 1
    else:
        avg_10 = val // 10
        
    # จับแยกประกอบร่างกลับเป็น String แบบ 1 ตำแหน่ง
    avg_str = f"{avg_10 // 10}.{avg_10 % 10}"
    
    # 4. สร้าง List รายชื่อ
    members = [f"Student{i}" for i in range(1, n + 1)]
    
    # 5. พิมพ์ผลลัพธ์
    print("Student: " + " ".join(members))
    print(f"Highest score: {high_score}")
    print(f"Lowest score: {low_score}")
    print(f"Average score: {avg_str}")
    print("Students who scored above average:")
    
    # 6. หาคนที่คะแนนสูงกว่าเฉลี่ย (ใช้ Integer Math ย้ายข้างสมการ ป้องกันบั๊ก)
    # scores[i] > (sum / n)  -->  ย้าย n ไปคูณ จะได้ scores[i] * n > sum
    for i in range(n):
        if scores[i] * n > sum_scores:
            print(members[i])

if __name__ == '__main__':
    solve()