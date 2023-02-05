from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float("inf")
        sum = 0

        leftpoint = 0

        for num in range(len(nums)):
            sum += nums[num]
            while sum >= s:
                sum -= nums[leftpoint]
                res = min( res, num - leftpoint + 1)
                leftpoint += 1
            
        return -1 if res == float("inf") else res

if __name__ == "__main__":
    exam=Solution()
    print(exam.minSubArrayLen(7,[2,3,1,2,4,3]))

