class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        maxn = nums[0]

        for n in nums:
            hash[n] = hash.get(n, 0) + 1
            if hash[maxn] < hash[n]:
                maxn = n
        return maxn
