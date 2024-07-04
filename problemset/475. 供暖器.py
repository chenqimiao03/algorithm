class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def best(houses, heaters, i, j):
            # 如果是最后一个供暖器，那必定是最优的
            # j 号供暖器到 i 号房子的半径小于 j + 1 号供暖器到 i 号房子
            return j == len(heaters) - 1 or abs(heaters[j] - houses[i]) < abs(heaters[j + 1] - houses[i])
        houses.sort()
        heaters.sort()
        ret = 0
        j = 0
        for i in range(len(houses)):
            # 如果 i 号房子选择 j 号供暖器不是最优
            while not best(houses, heaters, i, j):
                j += 1
            ret = max(ret, abs(heaters[j] - houses[i]))
        return ret