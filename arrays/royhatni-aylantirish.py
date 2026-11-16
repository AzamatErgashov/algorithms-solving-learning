nums = [1,2,3,4,5,6,7]
k = 4

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# 1 2 3 4 5 -> 5 4 3 2 1

def rotate(nums, k):
    left = 0
    right = len(nums) - 1
    reverse(nums, left, right)
    reverse(nums, left, k - 1)
    reverse(nums, k, right)

    return nums


print(rotate(nums, k))



# while k > 0:
#     element = nums.pop()
#     nums.insert(0, element)
#     # print(element)
#     k -= 1
#
# print(nums)
