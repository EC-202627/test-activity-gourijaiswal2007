t = int(input())

for _ in range(t):
    x = int(input())

    if x <= 1000:
        print("No")
    elif x >= 10000:
        print("It's too much")
    else:
        print("Yes")
