class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
<<<<<<< HEAD
        nums_dict = {}
        for index, num in enumerate(nums):
            remaining_target = target - num
            if remaining_target in nums_dict:
                return[index, nums_dict[remaining_target]]
                
                else:

                    nums_dict[num] = index
=======
        
>>>>>>> 24451d778b4f74500e09898c857fc0b866d86138
