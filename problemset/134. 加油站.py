class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # # 油余量数组
        # for i in range(n):
        #     gas[i] -= cost[i]
        # # 时间复杂度：O(N^2)
        # for start in range(n):
        #     if gas[start] < 0:
        #         continue
        #     total = 0
        #     for j in range(start, start + n):
        #         total += gas[j % n]
        #         if total < 0:
        #             break
        #     else:
        #         return start
        # return -1

        n = len(gas)
        # 油余量数组
        for i in range(n):
            gas[i] -= cost[i]
        l, r, total, length = 0, 0, 0, 0
        # 尝试从 l 位置出发看能不能走一圈
        # r: 窗口即将进来数字的位置
        # length： 窗口的大小
        # total：窗口累加和
        while l < n:
            # 扩展窗口
            while total >= 0:
                if length == n:
                    return l
                r = (l + length) % n
                length += 1
                total += gas[r]
            # 缩减窗口
            length -= 1
            total -= gas[l]
            l += 1
        return -1