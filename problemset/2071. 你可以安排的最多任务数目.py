class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        # 二分答案法+贪心+双端队列
        from collections import deque
        def f(t_left, t_right, w_left, w_right, pills, strength):
            """当前的任务数能不能完成
            t_left,...,t_right：需要力量最小的任务数
            w_left,...,w_right：力量最大的工人数
            pills：药丸个数
            strength：药效
            """
            nonlocal workers, tasks
            # 已经使用了多少颗药
            cnt = 0
            dq = deque()
            j = t_left
            for i in range(w_left, w_right + 1):
                # 当前工人能够解锁的任务（不嗑药的情况下）
                while j <= t_right and tasks[j] <= workers[i]:
                    dq.append(j)
                    j += 1
                # 当前工人有任务做
                if dq and tasks[dq[0]] <= workers[i]:
                    # 当前工人选择当前能做的任务中最简单的一个
                    dq.popleft()
                else:
                    # 当前工人嗑药之后能够解锁的任务
                    while j <= t_right and tasks[j] <= workers[i] + strength:
                        dq.append(j)
                        j += 1
                    # 如果有任务可做
                    # 选择最难做的一个
                    if dq:
                        cnt += 1
                        dq.pop()
                    else:
                        return False
            return cnt <= pills

        tasks.sort()
        workers.sort()
        size_t, size_w = len(tasks), len(workers)
        # 能完成任务的上下边界
        # 有可能一个任务都完成不了
        # 也有可能任务全都完成了（工人的人数在多于任务的任务数的情况下）
        l, r = 0, min(size_t, size_w)
        ret = 0
        while l <= r:
            m = (l + r) // 2
            if f(0, m - 1, size_w - m, size_w - 1, pills, strength):
                ret = m
                l = m + 1
            else:
                r = m - 1
        return ret