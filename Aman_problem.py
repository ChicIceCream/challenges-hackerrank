N, H, x = map(int, input().split())

print(N, H, x)

total_time = N + x

if total_time >= H:
    print(1)
else:
    print(0)