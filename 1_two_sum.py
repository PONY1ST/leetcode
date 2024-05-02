from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_sums = sorted(enumerate(nums), key=lambda x: x[1])
        
        left = 0
        right = len(sorted_sums) - 1
        while left < right:
            current_sum = sorted_sums[left][1] + sorted_sums[right][1]
            if current_sum == target:
                left_index = sorted_sums[left][0]
                right_index = sorted_sums[right][0]
                result = [left_index, right_index]
                return result
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        


print(Solution().twoSum(nums = [3,2,4], target = 6))