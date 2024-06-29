class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # 某个前缀和最早出现的位置
        # 0 这个前缀和最早出现在 -1，表示一个属也没有的时候
        HashMap = {0: -1}
        total, ret = 0, 0
        for i in range(len(hours)):
            # 把数组元素转化成 1 和 -1
            total += 1 if hours[i] > 8 else -1
            # 当前的累加和大于零时，最长子数组的长度是 i + 1
            if total > 0:
                ret = i + 1
            else:
                # total <= 0
                if HashMap.get(total - 1, None) is not None:
                    ret = max(ret, i - HashMap.get(total - 1))
            if HashMap.get(total, None) is None:
                HashMap[total] = i
        return ret
