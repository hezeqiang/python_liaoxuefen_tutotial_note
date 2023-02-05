from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fastP=slowP=0

        for number in nums:
            
            if number == val:
                fastP=fastP+1

            else:
                nums[slowP]=nums[fastP]
                fastP=fastP+1
                slowP=slowP+1
        return nums[:slowP]
            

if __name__ == "__main__":
    exam=Solution()
    print(exam.removeElement([1,2,3,4,5,6],3))

