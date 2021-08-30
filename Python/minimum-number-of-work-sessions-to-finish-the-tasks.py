# Time:  O(n * 2^n)
# Space: O(2^n)

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        # dp[mask][0]: min number of sessions by choosing tasks in mask bitset
        # dp[mask][1]: min used time of last session by choosing tasks in mask bitset
        dp = [[float("inf")]*2 for _ in xrange(1<<len(tasks))]
        dp[0] = [1, 0]
        for mask in xrange(len(dp)):
            basis = 1
            for task in tasks:
                new_mask = mask|basis
                basis <<= 1
                if new_mask == mask:
                    continue
                if dp[mask][1]+task <= sessionTime:
                    dp[new_mask] = min(dp[new_mask], [dp[mask][0], dp[mask][1]+task])
                else:
                    dp[new_mask] = min(dp[new_mask], [dp[mask][0]+1, task])
        return dp[-1][0]
