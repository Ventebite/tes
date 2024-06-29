'''Реализуйте функцию, которая принимает в качестве первого аргумента строку,
а затем любое количество числовых аргументов и возвращает минимум,
максимум или среднее переданной последовательности аргументов.'''
nums = list(map(int, input().split()))
tmp = 0
if len(nums)%2!=0:
    tmp = nums.pop(len(nums)-1)
    
    
for i in range(0, len(nums), 2):
    if i == len(nums)-1:
        break
    nums[i], nums[i+1] = nums[i+1], nums[i]
    
if tmp:
    nums.append(tmp)
    
print(nums)