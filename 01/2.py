#!/usr/bin/env python3

with open("input") as data:
    numbers = [int(n) for n in data.read().strip()]

size = len(numbers)
step = int(size / 2)
answer = 0

for i, n in enumerate(numbers):
    if n == numbers[(i + step) % size]:
        answer += n

print()
print(answer)
