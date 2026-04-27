inventory = {}
output_log = []

while True :
    parts = input().split()

    cmd = parts[0]

    if cmd == 'END' :
        break
    
    elif cmd == 'ADD' :
        name = parts[1]
        qty = int(parts[2])

        if name in inventory :
            inventory[name] += qty
        else :
            inventory[name] = qty
        
    elif cmd == 'REMOVE' :
        name = parts[1]
        qty = int(parts[2])

        curr_qty = inventory.get(name, 0)

        if qty > curr_qty :
            output_log.append(f'Not enough stock for {name}')
            inventory[name] = 0
        else :
            inventory[name] -= qty

        if inventory[name] == 0:
            del inventory[name]

    elif cmd == 'CHECK' :
        low_stock = []
        for name, qty in inventory.items() :
            if qty < 5 :
                low_stock.append(name)
        
        if len(low_stock) > 0 :
            low_stock.sort()
            for name in low_stock :
                output_log.append(name)
        else :
            output_log.append('All stocks are sufficient')

    elif cmd == 'REPORT' :
        sorted_items = sorted(inventory.keys())

        for name in sorted_items :
            output_log.append(f'{name}: {inventory[name]}')

for line in output_log :
    print(line)
            