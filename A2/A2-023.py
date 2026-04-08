r = input().strip()
r_up = r.upper()

if all(c in 'TI' for c in r_up):
    print(f'unknown {len(r)}')
else :
    curr_a = 0
    max_a = 0
    is_valid = True
    err_idx = -1

    for i in range(len(r_up)):
        pres = r_up[i]

        if pres not in 'RABIT':
            is_valid = False
            err_idx = i
            break

        prev = r_up[i-1] if i > 0 else None

        if prev == 'R' and pres != 'A':
            is_valid = False
            err_idx = i
            break

        if prev == 'B' and pres not in 'IT':
            is_valid = False
            err_idx = i
            break

        if pres == 'A' and prev not in 'RA':
            is_valid = False
            err_idx = i
            break

        if i == len(r_up) - 1 and pres in 'RB':
            is_valid = False
            err_idx = i
            break

        if pres == 'A':
            curr_a += 1
            max_a = max(max_a, curr_a)
        else:
            curr_a = 0

    if is_valid:
        print(f'yes {max_a}')
    else:
        print(f'no {err_idx}')