class Solution(object):
    def twoSum(self, nums, target):
        # stores elements and indices
        value = {}
        for i, num in enumerate(nums):
            # calculate the value to reach target
            remainder = target - num
            # check if remainder exists in value
            if remainder in value:
                # return the indices of two numbers that equals to target
                return [value[remainder], i]
            # else add the current number and index to value
            value[num] = i
        # if not found return empty list    
        return []