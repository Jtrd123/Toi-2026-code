def solve():
    n = int(input())

    shells = []
    for _ in range(n):
        x, y, d = map(int,input().split())
        shells.append((x, y, d))

    for Tx in range(1001):
        for Ty in range(1001):

            is_target = True

            for x, y, d in shells:
                if (Tx - x)**2 + (Ty - y)**2 != d**2:
                    is_target = False
                    break

            if is_target:
                print(f'{Tx} {Ty}')
                return
                
if __name__ == "__main__":
    solve()