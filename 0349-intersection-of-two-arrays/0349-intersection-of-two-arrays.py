class Solution(object):
    def intersection(self, nums1, nums2):
        # list to store result
        res = []

        # change lists to sets for preventing duplicated elements
        set1 = set(nums1)
        set2 = set(nums2)

        for char in set1:
            # check if char in set1 is in set2
            if char in set2:
                # append to list
                res.append(char)

        return res


        
        