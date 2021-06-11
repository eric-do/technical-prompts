class Solution:
    def exchange_money_for_chocolate(self, ppc, wpc, wallet) -> int:
        if ppc <= 0:
            return 0

        wrappers = self.exchange_currency_for_chocolate(ppc, wallet)
        total = wrappers
        while wrappers >= wpc:
            exchanged_chocolates = self.exchange_currency_for_chocolate(wpc, wrappers)
            total += exchanged_chocolates
            wrappers = wrappers - exchanged_chocolates * wpc + exchanged_chocolates
        return total

    def exchange_currency_for_chocolate(self, units_per_chocolate: int,  total_units: int) -> int:
        if total_units < units_per_chocolate:
            return 0

        return 1 + self.exchange_currency_for_chocolate(units_per_chocolate, total_units - units_per_chocolate)

    def assert_equals(self, actual: int, expected: int, description='No description') -> None:
        if actual == expected:
            print('PASS [', description, ']')
        else:
            print('FAIL [', description, ']: expected', expected, ' but got ', actual)

    def test(self) -> None:
        self.assert_equals(self.exchange_money_for_chocolate(3, 5, 20), 7, "It should return the correct amount")
        self.assert_equals(self.exchange_money_for_chocolate(2, 2, 16), 15, "It should return the correct amount")
        self.assert_equals(self.exchange_money_for_chocolate(1, 3, 15), 22, "It should return the correct amount when there are leftover chocolates")
        self.assert_equals(self.exchange_money_for_chocolate(-3, 5, 10), 0, "It should return 0 if negative price entered")
        self.assert_equals(self.exchange_money_for_chocolate(2, 5, 1), 0, "It should return 0 user does not have enough money")
        self.assert_equals(self.exchange_money_for_chocolate(0, 5, 1), 0, "It should return 0 if $0/chocolate")
        self.assert_equals(self.exchange_currency_for_chocolate(3, 15), 5, "It should return the correct amount")


solution = Solution()
solution.test()
