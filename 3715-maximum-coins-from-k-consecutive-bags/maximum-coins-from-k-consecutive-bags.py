class Solution:
    def maximumCoins(self, A: List[List[int]], k: int) -> int:
        def slide(A):
            A.sort()
            cur = best = j = 0

            for i in range(len(A)):
                right = A[i][0] + k - 1

                while j < len(A) and A[j][0] <= right:
                    cur += (A[j][1] - A[j][0] + 1) * A[j][2]
                    j += 1

                # j is the next interval, so j - 1 is the last added
                extra = max(0, A[j - 1][1] - right) * A[j - 1][2]
                best = max(best, cur - extra)

                # next iteration starts at the next interval
                cur -= (A[i][1] - A[i][0] + 1) * A[i][2]

            return best

        mirrored = [[-r, -l, coins] for l, r, coins in A]
        return max(slide(A), slide(mirrored))