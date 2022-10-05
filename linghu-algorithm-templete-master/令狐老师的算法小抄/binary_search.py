# Binary Search
# 排序数组(30-40%是二分)
# 当面试官要求你找一个比O(n) 更小的时间复杂度算法的时候(99%)
# 找到数组中的一个分割位置，使得左半部分满足某个条件，右半部分不满足(100%)
# 找到一个最大/最小的值使得某个条件被满足(90%)
# 时间复杂度：O(logn)
# 空间复杂度：O(1)

def binary_search(self, nums, target):

    # corner case
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1

    # 用start + 1 < end 而不是start < end 的目的是为了避免死循环
    # 在first position of target 的情况下不会出现死循环
    # 但是在last position of target 的情况下会出现死循环
    # 样例：nums=[1，1] target = 1
    # 为了统一模板，我们就都采用start + 1 < end，就保证不会出现死循环
    while start+1 < end:
        # mid = start + (end - start) // 2
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid
        elif nums[mid] > target:
            end = mid
        elif nums[mid] == target:
            end = mid

    # 因为上面的循环退出条件是start + 1 < end
    # 因此这里循环结束的时候，start 和end 的关系是相邻关系（1 和2，3 和4 这种）
    # 因此需要再单独判断start 和end 这两个数谁是我们要的答案
    # 如果是找first position of target 就先看start，否则就先看end
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1