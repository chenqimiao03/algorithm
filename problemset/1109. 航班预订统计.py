class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0 for i in range(n + 2)]
        for book in bookings:
            arr[book[0]] += book[2]
            arr[book[1] + 1] -= book[2]
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        ret = [arr[i + 1] for i in range(n)]
        return ret
