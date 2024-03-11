class Solution(object):
    def getCommon(self, nums1, nums2):
        # initialize two pointers for nums1 and nums2
        x, y = 0, 0

        while x < len(nums1) and y < len(nums2):
            # if elements of pointer x and y are equal
            if nums1[x] == nums2[y]:
                # return common element
                return nums1[x]
            # if element in nums1 is smaller, move to next nums1 pointer
            elif nums1[x] < nums2[y]:
                x += 1
            # else move to nextnums2 pointer
            else:
                y += 1

        return -1
