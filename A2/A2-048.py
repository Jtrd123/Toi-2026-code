# n = int(input())

# if n == 0:
#     print("Student:")
# else:
#     scores = list(map(int, input().split()))

#     high_score = max(scores)
#     low_score = min(scores)
#     avg_score = ( sum(scores) / n ) + 1e-9

#     members = [f"Student{i}" for i in range(1, n + 1)]
    
#     print("Student: " + " ".join(members))
    
#     print(f"Highest score: {high_score}")
#     print(f"Lowest score: {low_score}")
#     print(f"Average score: {avg_score:.1f}")
#     print("Students who scored above average:")

#     for j in range(n):
#         if scores[j] > avg_score:
#             print(members[j])

import sys

def solve():
    # ดูดข้อมูลทั้งหมดทีเดียว หั่นด้วยช่องว่าง (ไม่แคร์ว่าจะขึ้นบรรทัดใหม่หรือไม่)
    data = sys.stdin.read().split()
    
    # ดักกรณีไม่มีข้อมูลเข้ามาเลย ป้องกันโปรแกรมพัง
    if not data:
        return
        
    n = int(data[0])
    
    # กฎข้อที่ 1: ถ้า n = 0 ให้พิมพ์แค่ Student: แล้วจบโปรแกรมทันที
    if n == 0:
        print("Student:")
        return
        
    # ดึงคะแนนจำนวน n ตัวถัดมา
    scores = [int(x) for x in data[1:n+1]]
    
    high_score = max(scores)
    low_score = min(scores)
    
    # คำนวณค่าเฉลี่ยแบบเป๊ะๆ เพื่อเอาไว้เทียบว่าใครมากกว่า
    exact_avg = sum(scores) / n
    
    # กฎข้อที่ 2: แก้ปัญหาปัดเศษของ Python โดยบวก 1e-9 (0.000000001) เข้าไป
    # ถ้าค่าเป็น 2.25 จะกลายเป็น 2.250000001 พอสั่ง :.1f มันจะปัดเป็น 2.3 ให้เป๊ะๆ!
    print_avg = exact_avg + 1e-9
    
    # สร้างรายชื่อนักเรียน
    members = [f"Student{i}" for i in range(1, n + 1)]
    
    # พิมพ์ผลลัพธ์
    print("Student: " + " ".join(members))
    print(f"Highest score: {high_score}")
    print(f"Lowest score: {low_score}")
    print(f"Average score: {print_avg:.1f}")
    print("Students who scored above average:")
    
    # วนลูปหาคนที่คะแนน "มากกว่า" ค่าเฉลี่ย (strictly greater)
    for i in range(n):
        if scores[i] > exact_avg:
            print(members[i])

if __name__ == '__main__':
    solve()