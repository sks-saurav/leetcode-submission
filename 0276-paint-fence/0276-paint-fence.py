class Solution:
    def numWays(self, n: int, k: int) -> int:
        l = max(n+1, 3)
        dp = [0] * l
        dp[1], dp[2] = k, k*k

        for i in range(3, n+1):
            dp[i] = (k-1) * (dp[i-1] + dp[i-2])

        return dp[n]


'''
We know the values for totalWays(1) and totalWays(2), 
now we need a formula for totalWays(i), where 3 <= i <= n. 
Let's think about how many ways there are to paint the ith post. We have two options:

1. Use a different color than the previous post. If we use a different color, then there are k-1
   colors for us to use. 
   This means there are (k - 1) * totalWays(i - 1) ways to paint the i th post a different color than the (i−1) th post.

2. Use the same color as the previous post. There is only one color for us to use, so there are
   1 * totalWays(i - 1) ways to paint the i th post the same color as the (i−1) th
   post. However, we have the added restriction of not being allowed to paint three posts in a row the same color. Therefore, we can paint the i th post the same color as the (i−1) th
   post only if the (i−1) th
   post is a different color than the (i−2) th post.

3. So, how many ways are there to paint the (i−1) th
  post a different color than the (i−2) th
  post? Well, as stated in the first option, there are (k - 1) * totalWays(i - 1) ways to paint the i th  post a different color than the (i−1) th
  post, so that means there are 1 * (k - 1) * totalWays(i - 2) ways to paint the (i−1) th
  post a different color than the (i−2) th post.

Adding these two scenarios together gives totalWays(i) = (k - 1) * totalWays(i - 1) + (k - 1) * totalWays(i - 2), which can be simplified to:

totalWays(i) = (k - 1) * (totalWays(i - 1) + totalWays(i - 2))

'''