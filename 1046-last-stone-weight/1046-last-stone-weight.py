class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while(len(stones)> 1):
            x = (heapq.heappop(stones)) * -1
            y = heapq.heappop(stones) * -1 

            if x == y:
                continue
            else:
                x = x - y
                heapq.heappush(stones, -x)

        if len(stones) == 0:
            return 0
        return -stones[0]
