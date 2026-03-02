class Solution(object):
    def twoSum(self, nums, target):

            self.nums = nums
            self.target = target
            seen = {}
            for i,num in enumerate(nums):
                needed = target - num
                if needed in seen:
                 return   seen[needed],i
                else:
                    seen[num] = i


solu =    Solution()
nums = [2,7,11,15]
target = 9
result = solu.twoSum(nums,target)
print(result)

# ------------------------------------
class Solution(object):
    def minimumPairRemoval(self, nums):
        ops = 0
        self.nums = nums
        
        """
        :type nums: List[int]
        :rtype: int
        """
        class Solution(object):
    def minimumPairRemoval(self, nums):

        self.nums = nums
        
        """
        :type nums: List[int]
        :rtype: int
        """
        class Solution(object):
    def minimumPairRemoval(self, nums):

        self.nums = nums
        
        """
        :type nums: List[int]
        :rtype: int
        """
class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            s = 0
            while n > 0:
                digit = n % 10
                s += digit * digit
                n //= 10

            n = s

        return True
