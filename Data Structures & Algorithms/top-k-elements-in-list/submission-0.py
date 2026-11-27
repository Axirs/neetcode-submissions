class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = {}
        ary = []
        res = []
        for num in nums:
            lst[num]= 1 + lst.get(num, 0)
        for num, i in lst.items():
            ary.append([i, num])
        ary.sort()
        while len(res) < k:
            res.append(ary.pop()[1])
        return res