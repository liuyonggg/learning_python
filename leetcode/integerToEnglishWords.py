'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''
class Solution():
    def __init__(self):
        self.less_twenty = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FORTEEN ", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN", "TWENTY"]
        self.tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NIGHTY"]
        self.hundred = "HUNDRED"
        self.thousand = "THOUSAND"

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        n = num
        while n > 0:
            n_mod_1000 = n % 1000
            n_hundreds = n_mod_1000 / 100
            n_tens = n_mod_1000 % 100 / 10
            n_ones = n_mod_1000 % 10
            if n_tens > 1:
                a = " " + res if res else ""
                b = self.less_twenty[n_ones] + a
                res = self.tens[n_tens] + " " + b if b else self.tens[n_tens]
            elif n_tens == 1:
                a = " " + res if res else ""
                res = self.less_twenty[n_tens*10 + n_ones] + a
            else:
                assert (n_tens == 0)
                a = " " + res if res else ""
                b = " " + res if res else ""
                res = self.less_twenty[n_ones] + b if n_ones else res
            a = " " + res if res else ""
            res = self.less_twenty[n_hundreds] + " " + self.hundred + a if n_hundreds else res
            n = n / 1000
            res = (self.thousand + " " + res if res else self.thousand ) if n else res
        return res

if __name__ == "__main__":
    assert Solution().numberToWords(123) == "ONE HUNDRED TWENTY THREE"
    assert Solution().numberToWords(113) == "ONE HUNDRED THIRTEEN"
    assert Solution().numberToWords(103) == "ONE HUNDRED THREE"
    assert Solution().numberToWords(100) == "ONE HUNDRED"
    assert Solution().numberToWords(1123) == "ONE THOUSAND ONE HUNDRED TWENTY THREE"
    assert Solution().numberToWords(1000) == "ONE THOUSAND"
            
            
                
