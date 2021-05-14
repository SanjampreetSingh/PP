class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = 0
        count = 0
        vowels = ["a", "e", "i", "o", "u"]
        n = len(s)

        for i in range(0, k):
            if s[i] in vowels:
                max_vowel += 1
                count += 1

        for i in range(k, n):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            if count > max_vowel:
                max_vowel = count

        return max_vowel
