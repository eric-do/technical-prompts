from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = [1] * len(nums)
        max_length = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    res[i] = max(res[i], res[j] + 1)
            max_length = max(max_length, res[i])

        return max_length

    def assert_equals(self, actual: int, expected: int, description: str) -> None:
        if actual == expected:
            print('PASS [', description, ']')
        else:
            print('FAIL [', description, '] expected: ', expected, 'but got', actual)

    def test(self) -> None:
        self.assert_equals(self.lengthOfLIS([10,1,2]), 2, 'It should return the correct length')
        self.assert_equals(self.lengthOfLIS([10,1,2,1,2,3]), 3, 'It should return the correct length for multiple increasing sequences')
        self.assert_equals(self.lengthOfLIS([10]), 1, 'It should return the correct length for a single element')
        self.assert_equals(self.lengthOfLIS([]), 0, 'It should return 0 for an empty list')

solution = Solution()
solution.test()