class Solution:

    def checkAnagram(self, freq1: list, freq2: list) -> bool:
        if freq1 != freq2:
            return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        freq1 = 26*[0]
        freq2 = 26*[0]
        a = ord("a")

        if m < n:
            return False

        for i in s1[:n]:
            freq1[ord(i) - a] += 1

        for i in s2[:n]:
            freq2[ord(i) - a] += 1

        if self.checkAnagram(freq1, freq2):
            return True

        window_size = n
        while(window_size < m):
            freq2[ord(s2[window_size]) - a] += 1
            freq2[ord(s2[window_size - n]) - a] -= 1

            if self.checkAnagram(freq1, freq2):
                return True

            window_size += 1

        return False
