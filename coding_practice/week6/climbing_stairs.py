
"""
Climbing Stairs - LeetCode #70
DP relation: f(n)=f(n-1)+f(n-2)
"""
def climbStairs(n):
    if n<=2: return n
    a,b=1,2
    for _ in range(3,n+1):
        a,b=b,a+b
    return b

print(climbStairs(5))  # 8

