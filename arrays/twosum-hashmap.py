nums = [1, 7, 8, 15]
target = 9

seen = {}

for i, num in enumerate(nums):

    difference = target - num
    print(target)
    print(num)

    if difference in seen:
        print(difference)
        print([seen[difference], i])
        break

    seen[num] = i