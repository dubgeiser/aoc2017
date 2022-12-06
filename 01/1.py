#!/usr/bin/env python3

with open("input") as data:
    numbers = [int(n) for n in data.read().strip()]

first = numbers.pop()
answer = 0
n = first
while len(numbers) > 0:
    if n == numbers[-1]:
        answer += n
    n = numbers.pop()
if n == first:
    answer += first

print()
print(answer)
