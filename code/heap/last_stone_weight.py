'''
last stone weight
'''
import heapq
class solutions:
    def last_stone_weight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heap.heappop(stones)
            if -1*second < -1*first:
                 heapq.heappush(stones, first - second)
        stones.append(0)
        return -1*stones[0]