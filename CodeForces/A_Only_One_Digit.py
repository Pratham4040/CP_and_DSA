t = int(input())
for _ in range(t):
    n = str(input())
    digits = [int(char) for char in n if char.isdigit()]
    if digits:
        print(min(digits))
    