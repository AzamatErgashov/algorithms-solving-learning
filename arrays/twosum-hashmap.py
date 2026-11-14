nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):

    difference = target - num

    if difference in seen:
        print([seen[difference], i])
        break

    seen[num] = i