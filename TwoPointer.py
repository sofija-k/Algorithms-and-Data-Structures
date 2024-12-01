'''
Valid Palindrome
link: https://leetcode.com/problems/valid-palindrome/description/
'''
from ast import List


def isPalindrome(self, s: str) -> bool:
        # use two pointer method
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


'''
Two Integer Sum II - Input Array is Sorted
link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointer method to find two indices whoese elements add up to target
        # remember list is sorted in ascending order, when incrementing l and r
        l, r = 0 , len(numbers)-1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1 
                
'''
Three Sum
link: https://leetcode.com/problems/3sum/description/
'''
def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums)-1

            while l < r:
                if nums[l] + nums[r] + val < 0:
                    l += 1
                elif nums[l] + nums[r] + val > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res


'''
Container With Most Water
link: https://leetcode.com/problems/container-with-most-water/description/
'''
def maxArea(self, heights: List[int]) -> int:
    l, r = 0, len(heights) - 1
    maxVol = 0
    
    while l < r:
        x = r - l 
        y = min(heights[l], heights[r])
        vol = x * y
        maxVol = max(maxVol, vol)
        
        # try another height by incrementing the pointer with the lower height
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    
    return maxVol