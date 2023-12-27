'''LC 2327. Number of People Aware of a Secret'''

from collections import deque

def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    mod = 10 ** 9 + 7

    # day 1
    q = deque([1] + [0] * (forget-1))
    sharing = 0
    pre = delay - 1

    for _ in range(1,n):
        sharing += q[pre] - q.pop()
        q.appendleft(sharing % mod)

    return sum(q) % mod

# DRIVER CODE
n = 6
delay = 2
forget = 4
print(peopleAwareOfSecret(n, delay, forget)) 


