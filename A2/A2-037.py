n = int(input())
e_queue = []
n_queue = []

for _ in range(n) :
    cmd = input().split()

    if cmd[0] == 'ARRIVE' :
        name = cmd[1]
        type_case = cmd[2]

        if type_case == 'emergency' :
            e_queue.append(name)
        elif type_case == 'normal' :
            n_queue.append(name)

    elif cmd[0] == 'TREAT' :
        if len(e_queue) > 0 :
            e_queue.pop(0)
        elif len(n_queue) > 0 :
            n_queue.pop(0)

    elif cmd[0] == 'SHOW' :
        if not e_queue and not n_queue :
            print("EMPTY")
        else:
            curr_queue = e_queue + n_queue
            print(*curr_queue)