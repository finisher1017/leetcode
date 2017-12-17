class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        parts = []
        current = 0
        complete = False
        
        while complete == False:
            second = current + 1
            current_num = nums[current]
            r = range(second, len(nums))
            for i in r:
                if current_num + nums[i] == target:
                    parts.append(nums.index(current_num))
                    parts.append(second)
                    complete = True
                    break
                else:
                    second += 1
                    continue
            
            current += 1
        return parts

inst = Solution()
run = inst.twoSum([2, 5, 7, 15], 9)
print(run)