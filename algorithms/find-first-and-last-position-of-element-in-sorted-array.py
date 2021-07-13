from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # I: list of numbers, target number
        # O: position of start/end
        # C: O(log n)
        # E: empty list, not found

        # what do we know
        # - BST
        # - When element is found, any other elements MUST be next to found element
        # [1,8,N,N,N,N,N,N,N,8,8,9]
        #  - - - M R R L M R L M R
        #  [1, 10]
        # BS looking for element:
        #  Set left/right
        #  Find mid
        #  if mid is element
        #    if on an edge, update edge
        #    else mark as traveled
        #      Go left
        #      Go right
        #  else
        #    if mid is traveled, return
        #    if mid is less than element, go right
        #    if mid is greater than element, go left

        pass

    def findFirstAndLastPosition(self, target: int, l: int, r: int, nums: List[int], solution: List[int]) -> List[int]:
        if l == r:
            if nums[l] == target:
                if l == 0 or nums[l-1] < target:
                    solution[0] = l
                elif r == len(nums) - 1 or nums[r + 1] > target:
                    solution[1] = r
            return solution

    def binarySearchElement(self, target, l: int, r: int, nums: List[int]) -> int:
        if l == r:
            return l if nums[l] == target else -1

        mid = (l + r) // 2
        if target == nums[mid]:
            if mid == 0 or (nums[mid-1] != '*' and nums[mid-1] < target):
                solution[0] = l
            elif mid == len(nums) - 1 or (nums[mid + 1] != '*' and nums[mid + 1] > target):
                solution[1] = r
            nums[mid] = '*'
            self.binarySearchElement(target, l, mid, nums)
            self.binarySearchElement(target, mid + 1, r, nums)
        elif target < nums[mid]:
            return self.binarySearchElement(target, l, mid, nums)
        else:
            return self.binarySearchElement(target, mid + 1, r, nums)

    def assert_equals(self, actual: List[int], expected: List[int], description: str) -> None:
        if actual == expected:
            print('PASS [', description, ']')
        else:
            print('FAIL [', description, ']: expected', expected, 'but got', actual)

    def test(self) -> None:
        self.assert_equals(self.searchRange([5,7,7,8,8,10], 8), [3,4], 'It should return the correct first and last position when 2 elements')
        self.assert_equals(self.searchRange([5,7,7,8,10], 8), [3,3], 'It should return the correct first and last position when 1 element')
        self.assert_equals(self.searchRange([7,8,8,8,8,8,8,10], 8), [1,5], 'It should return the correct first and last position when more than 2 elements')
        self.assert_equals(self.searchRange([5,7,7,10], 8), [-1,-1], 'It should return [-1,-1] if element not found')
        self.assert_equals(self.searchRange([], 8), [-1,-1], 'It should return [-1,-1] if list is empty')
        self.assert_equals(self.binarySearchElement(1, 0, 2, [1,2,3]), 0, 'Binary search should work')
        self.assert_equals(self.binarySearchElement(2, 0, 2, [1,2,3]), 1, 'Binary search should work')
        self.assert_equals(self.binarySearchElement(3, 0, 2, [1,2,3]), 2, 'Binary search should work')
        self.assert_equals(self.findFirstAndLastPosition(8, 0, 7, [7,8,8,8,8,8,8,10], []), [1,6], 'It should return the correct first and last position when more than 2 elements')

solution = Solution()
solution.test()