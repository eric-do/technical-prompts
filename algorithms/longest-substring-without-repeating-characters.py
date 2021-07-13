class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I: string
        # O: length of longest non-repeating substring
        # C: < O(n^2) -> O(n)
        # E: empty string, invalid input, upper/lowercase?
        #   L R L R R R
        # a b c a d c b
        # 1 2 3 3 4 3
        # max: 4
        # a:0  b:1  c:5  d:4

        # Set L/R to 0
        # set max length to 0
        # Loop string with R
        #   Check if dictionary contains character and character appears before L
        #     If yes:
        #       update position of L to position in front of L
        #   Add character:position to dictionary
        #   Update max length = R - L + 1

        l = 0
        max_length = 0
        pos = {}

        for r in range(len(s)):
            if s[r] in pos and pos[s[r]] >= l:
                l += 1
            pos[s[r]] = r
            max_length = r - l + 1
        return max_length

    def assert_equals(self, actual: int, expected: int, description: str) -> None:
        if actual == expected:
            print('PASS [', description, ']')
        else:
            print('FAIL [', description, ']: expected', expected, 'but got', actual)

    def test(self) -> None:
        self.assert_equals(self.lengthOfLongestSubstring('abc'), 3, 'It returns correct longest substring length for abc')
        self.assert_equals(self.lengthOfLongestSubstring('bbbb'), 1, 'It returns correct longest substring length for bbbb')
        self.assert_equals(self.lengthOfLongestSubstring('a'), 1, 'It returns correct longest substring for 1 char string')
        self.assert_equals(self.lengthOfLongestSubstring(''), 0, 'It returns 0 for an empty string')

solution = Solution()
solution.test()