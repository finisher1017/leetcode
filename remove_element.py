def remove_element(nums, val):
	done = False
	while done == False:
		if val in nums:
			nums.remove(val)
			continue
		else:
			done = True

	return len(nums)

print(remove_element([3,2,2,3,2], 3))