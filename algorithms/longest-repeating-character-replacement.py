from typing import DefaultDict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # I: string, number
        # O: number
        # C: O(n)
        # E: empty string, invalid inputs, k > len

        count = DefaultDict(int)
        start = max_count = max_length = 0
        for end in range(len(s)):
            count[s[end]] += 1
            max_count = max(max_count, count[s[end]])
            window_size = end - start + 1
            num_not_max = window_size - max_count
            if num_not_max > k:
                count[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length

    def assert_equals(self, actual: int, expected: int, description: str = 'No description') -> None:
        if actual == expected:
            print('PASS [', description, ']')
        else:
            print('FAIL [', description, ']: expected', actual, 'to be', expected)

    def test(self) -> None:
        self.assert_equals(self.characterReplacement('AABAA', 1), 5, 'It should return the correct length')
        self.assert_equals(self.characterReplacement('ABAB', 2), 4, 'It should return the correct length')
        self.assert_equals(self.characterReplacement('AABABBA', 1), 4, 'It should return the correct length')

solution = Solution()
solution.test()