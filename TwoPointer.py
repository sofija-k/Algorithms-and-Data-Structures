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
        