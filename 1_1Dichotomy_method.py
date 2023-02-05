from typing import List

class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right=len(nums)-1
       
        while left<=right:
            middle=int((left+right)/2)
            
            if nums[middle]>target:
                right=middle-1

            elif nums[middle]<target:
                left=middle+1

            else:
                return middle

        return -1

if __name__ == "__main__":
    exam=Solution()
    print(exam.search([1,2,3,4,5,6],0))




        