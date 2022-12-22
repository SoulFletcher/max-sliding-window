import collections


def max_sliding_window(nums, k):
    """
    returns all maximum values from all positions of sliding window with size k
    using deque (because pop is O(n) and popLeft is O(n)
    """
    result = []
    deq = collections.deque()  # indices
    i, j = 0, 0
    while j < len(nums):
        while deq and nums[deq[-1]] < nums[j]:  # removing elements from end of deque if smaller than nums[j]
            deq.pop()
        deq.append(j)  # then append j
        if i > deq[0]:  # delete left value from deque if out of bounce
            deq.popleft()
        if (j + 1) >= k:  # append left one when size of deque window is k or more
            result.append(nums[deq[0]])
            i += 1
        j += 1
    return result
