nums = [1, 1, 2]
mem = nums[0]
for i in nums:
	if i == mem:
		nums.remove(i)

print(len(nums))

