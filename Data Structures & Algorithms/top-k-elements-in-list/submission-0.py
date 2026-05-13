from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: count frequencies
        count = Counter(nums)   # e.g. {1:1, 2:2, 3:3}

        # Step 2: create buckets where index = frequency
        # largest possible frequency is len(nums)
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            freq_buckets[freq].append(num)

        # Step 3: collect k most frequent by scanning buckets from high freq to low
        result = []
        for freq in range(len(freq_buckets) - 1, 0, -1):  # high to low
            for num in freq_buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        