class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        def f(n, frm, to, o):
            if n == 1:
                to.append(frm.pop())
            else:
                f(n - 1, frm, o, to)
                to.append(frm.pop())
                f(n - 1, o, to, frm)
        f(n, A, C, B)
        