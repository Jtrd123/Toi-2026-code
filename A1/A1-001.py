fname = input().strip()
lname = input().strip()
print(f"Hello {fname} {lname}")
alias = f"{fname[:2]}{lname[:2]}"
print(alias)