import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1 , 0

        for i in range(len(piles)):
            if right < piles[i]:
                right = piles[i]
        
        res = right

        while right >= left:
            mid = (left + right) // 2
            calHours = 0

            for p in piles:
                calHours += math.ceil(p/mid)
                
            if calHours <= h:
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1

        return res

                        