class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        buckets=[[] for i in range(len(nums)+1)]
        for i,j in d.items():
            buckets[j].append(i)
        res=[]
        for i in range(len(buckets)-1,-1,-1):
          for num in buckets[i]:
            res.append(num)
            if len(res)==k:
                return res

