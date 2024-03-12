class Solution(object):
    def maxFrequencyElements(self, nums):
        # count freq of each element
        char_count = Counter(nums)
        
        # initialize result
        res = 0
        
        # find the max freq
        max_freq = max(char_count.values())
        
        # loop through every freq        
        for count in char_count.values():
            # if current freq equals to max freq
            if count == max_freq:
                # add to result
                res += count
        
        return res
        