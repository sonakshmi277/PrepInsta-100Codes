class Solution:
    def permute(self, nums):
        self.per = []

        def back(path, used):
            if len(nums) == len(path):
                self.per.append(path[:])  # ✅ appending a copy
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    back(path, used)
                    path.pop()            # ✅ backtracking
                    used[i] = False

        back([], [False] * len(nums))     # ✅ initial call
        return self.per
