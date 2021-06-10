class Solution:
    # I:
    #  - ppc: integer
    #  - wallet: integer
    # O:
    #  - total choclates: integer
    # C:
    #  - none
    # E:
    #  - invalid inputs? characters instead of numbers
    def exchange_money_for_chocolate(self, ppc, wpc, wallet) -> int:
        if ppc < 0:
            raise Exception('Price per chocolate cannot be negative')

        total_chocolates = self.get_chocolates_based_on_wallet(ppc, wallet)
        remaining_chocolates = total_chocolates
        while True:
            chocolates_from_wrappers = self.get_chocolates_based_on_wrappers(wpc, remaining_chocolates)
            remaining_chocolates -= chocolates_from_wrappers * wpc
            remaining_chocolates += + chocolates_from_wrappers
            total_chocolates += chocolates_from_wrappers
            if chocolates_from_wrappers == 0:
                break

        return total_chocolates

    def get_chocolates_based_on_wallet(self, ppc: int,  wallet: int) -> int:
        if wallet < ppc:
            return 0

        return 1 + self.get_chocolates_based_on_wallet(ppc, wallet - ppc)

    def get_chocolates_based_on_wrappers(self, wpc, chocolates) -> int:
        if chocolates < wpc:
            return 0
        return 1 + self.get_chocolates_based_on_wrappers(wpc, chocolates - wpc)

    def assert_equals(self, actual: int, expected: int) -> None:
        if actual == expected:
            print('PASS')
        else:
            print('FAIL: expected ', actual, ' to equal ', expected)

    def assert_throws_error(self, func, ppc, wpc, wallet) -> None:
        try:
            func(ppc, wpc, wallet)
            print('FAIL: did not raise exception for invalid input')
        except Exception:
            print('PASS')

    def test(self) -> None:
        self.assert_equals(self.exchange_money_for_chocolate(3, 5, 15), 6)
        self.assert_equals(self.exchange_money_for_chocolate(3, 2, 10), 5)
        self.assert_equals(self.exchange_money_for_chocolate(1, 3, 15), 22)
        self.assert_throws_error(self.exchange_money_for_chocolate, -3, 5, 10)
        self.assert_equals(self.get_chocolates_based_on_wrappers(3, 15), 5)


solution = Solution()
solution.test()
