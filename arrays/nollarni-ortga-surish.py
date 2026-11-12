# first try

# nums = [0,1,0,3,12]
#
# cash = 0
# for i in nums:
#     if i == 0:
#         cash += 1
#         nums.remove(i)
#         print(i)
#
# for i in range(cash):
#     nums.append(0)
#
# print(nums)

# second try

nums = [0,1,0,3,12]

# cash = []
# for i in nums:
#     if i == 0:
#         nums.remove(i)
#         nums.append(0)

# print(nums)

# last one

def moveZeroes(nums):
	l = 0
	for r in range(len(nums)):
		if nums[r] != 0:
			nums[l], nums[r] = nums[r], nums[l]
			l += 1
	return nums