class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, num in enumerate(nums):
            remaining_target = target - num
            if remaining_target in nums_dict:
                return[index, nums_dict[remaining_target]]
                
                else:

                    nums_dict[num] = index