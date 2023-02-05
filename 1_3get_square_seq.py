from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)

        left = 0
        right = n-1
        squ_list = [-1] * n


        for i in range(n):
            print(i)

            if abs(nums[left]) >= abs(nums[right]):
                squ_list[n-1-i] = nums[left] ** 2
                left += 1
            else:
                squ_list[n-1-i] = nums[right] ** 2
                right -= 1

        return squ_list


if __name__ == "__main__":
    exam=Solution()
    print(exam.sortedSquares([-5,-1,0,4,6]))
