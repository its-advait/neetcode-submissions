class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}

        for l in s1:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1

        window = {}

        for r in range(len(s2)):
            if s2[r] in window:
                window[s2[r]] += 1
            else:
                window[s2[r]] = 1

            if r >= len(s1):
                left = s2[r - len(s1)]
                window[left] -= 1

                if window[left] == 0:
                    del window[left]

            if window == d:
                return True

        return False