class Solution:
    def permuteUnique(self, nums):
        self.per = []
        nums.sort()  # Sort the list first to bring duplicates together

        def back(path, used):
            if len(path) == len(nums):
                self.per.append(path[:])
                return
            
            used_in_this_layer = set()  # Track duplicates at this recursion level
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                if nums[i] in used_in_this_layer:
                    continue  # Skip duplicate number at this level
                
                used_in_this_layer.add(nums[i])
                used[i] = True
                path.append(nums[i])
                
                back(path, used)
                
                path.pop()
                used[i] = False

        back([], [False] * len(nums))
        return self.per
