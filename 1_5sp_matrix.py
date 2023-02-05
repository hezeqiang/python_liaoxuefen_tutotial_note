from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = [[0]* n for _ in range(n) ]
        loop_num = int((n-1)/2)
        startx, starty = 0, 0
        count = 1 

        for loop in range(loop_num):
            length=n-2*loop
            for i in range(length-1):
              num[starty][i+startx]=count
              count += 1
            for i in range(0,length-1):
              num[i+starty][startx+length-1]=count
              count += 1
            for i in range(0,length-1):
              num[startx+length-1][startx+length-1-i]=count
              count += 1
            for i in range(0,length-1):
              num[startx+length-1-i][startx]=count
              count += 1
            
            startx += 1
            startx += 1
            loop_num += 1

        if n % 2 == 1:
            num[int(n/2)][int(n/2)]=count

        return num

if __name__ == "__main__":
    exam=Solution()
    print(exam.generateMatrix(3))

