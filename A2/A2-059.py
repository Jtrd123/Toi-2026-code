hashtags = {
        1: "TechTrends", 
        2: "EcoLife", 
        3: "FoodieHeaven", 
        4: "FashionWeek", 
        5: "HealthyLiving"
    }

n, d = map(int, input().split())

max_total = -1
top_performer = ""

for _ in range(n):
    row_data = list(map(int, input().split()))
    
    h_id = row_data[0]
    name = hashtags[h_id]

    counts = row_data[1:]

    total = sum(counts)
    avg = total / d

    if counts[-1] > counts[0]:
        trend = "GROWING"
    elif counts[-1] < counts[0]:
        trend = "DECLINING"
    else: 
        trend = "STABLE"

    print(f'{name}: {total} total, {avg:.2f} avg, {trend}')

    if total > max_total :
        max_total = total
        top_performer = name


print(f"Top performer: {top_performer}")