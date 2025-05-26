with open('9_14250 (1).txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(nums):
    return len(nums) == len(set(nums))

def f2(nums):
    return (max(nums) - min(nums))**3 >= (sum(nums) - max(nums) - min(nums))**2

summ = 0
cnt = 0
for i in data:
    cnt += 1
    if f1(i) and f2(i):
        summ += cnt
print(summ)

