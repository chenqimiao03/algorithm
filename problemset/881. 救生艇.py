class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ret = 0
        l, r = 0, len(people) - 1
        while l <= r:
            k = people[l] if l == r else people[l] + people[r]
            if k > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            ret += 1
        return ret