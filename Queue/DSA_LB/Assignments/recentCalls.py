'''
LC 933. Number of Recent Calls
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]
'''
import collections
class RecentCounter:
        
    def ping(t):
        queue = collections.deque()
        print('t:',t)
        start = t - 3000
        queue.append(t)

        while (queue and queue[0] < start):
            queue.popleft()
        return len(queue)
        
# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
t = [[], [1], [100], [3001], [3002]]
print(obj.ping(t[i]) for i in range(len(t)))