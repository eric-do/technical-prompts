class Solution:
    def exchange_money_for_chocolate(self, ppc, wpc, wallet) -> int:
        if ppc <= 0:
            return 0

        total_chocolates = self.exchange_currency_for_chocolate(ppc, wallet)
        remaining_chocolates = chocolates_from_wrappers = total_chocolates

        while chocolates_from_wrappers > 0:
            chocolates_from_wrappers = self.exchange_currency_for_chocolate(wpc, remaining_chocolates)
            remaining_chocolates -= chocolates_from_wrappers * wpc
            remaining_chocolates += chocolates_from_wrappers
            total_chocolates += chocolates_from_wrappers

        return total_chocolates

    def exchange_currency_for_chocolate(self, units_per_chocolate: int,  total_units: int) -> int:
        if total_units < units_per_chocolate:
            return 0

        return 1 + self.exchange_currency_for_chocolate(units_per_chocolate, total_units - units_per_chocolate)


    def assert_equals(self, actual: int, expected: int, description='No description') -> None:
        if actual == expected:
            print('PASS [', description, ']')
        else:
            print('PASS [', description, ']: expected', actual, ' to equal ', expected)

    def test(self) -> None:
        self.assert_equals(self.exchange_money_for_chocolate(3, 5, 15), 6, "It should return the correct amount when % 0")
        self.assert_equals(self.exchange_money_for_chocolate(1, 3, 15), 22, "It should return the correct amount when % 0")
        self.assert_equals(self.exchange_money_for_chocolate(3, 2, 10), 5, "It should return the correct amount when % > 0")
        self.assert_equals(self.exchange_money_for_chocolate(-3, 5, 10), 0, "It should return 0 if negative price entered")
        self.assert_equals(self.exchange_money_for_chocolate(2, 5, 1), 0, "It should return 0 user does not have enough money")
        self.assert_equals(self.exchange_money_for_chocolate(0, 5, 1), 0, "It should return 0 if $0/chocolate")
        self.assert_equals(self.exchange_currency_for_chocolate(3, 15), 5, "It should return the correct amount")


solution = Solution()
solution.test()
