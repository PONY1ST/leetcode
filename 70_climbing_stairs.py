class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dynamic_programming = [0]*(n+1)
        dynamic_programming[1] = 1
        dynamic_programming[2] = 2

        for i in range(3, n+1):
            dynamic_programming[i] = dynamic_programming[i-1] + dynamic_programming[i-2]
        
        return dynamic_programming[n]

climbStairs = Solution().climbStairs(3)
print(climbStairs)