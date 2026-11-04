class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre, post = [], []
        cur = 1

        for num in nums:
            pre.append(cur)
            cur *=  num
        

        cur = 1

        for num in reversed(nums):
            post.append(cur)
            cur *= num
        
        post.reverse()

        for i in range(len(pre)):
            res.append(pre[i] * post[i])

        return res

        