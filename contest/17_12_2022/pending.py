class Solution:
    def smallestValue(self, n: int) -> int:
        def get_sum(n):
            sum_things = 0
            c = 2
            while (n > 1):
                if n % c == 0:
                    sum_things += c
                    n = n / c
                else:
                    c = c + 1
            return sum_things

        while True:
            next_n = get_sum(n)

            if next_n == n:
                return n
            n = next_n

        return 2


sol = Solution()
sol.smallestValue(15)
