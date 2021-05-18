class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = 0
        count = 0
        vowels = "aeiou"
        n = len(s)

        for i in s[:k]:
            if i in vowels:
                count += 1

        max_vowel = count

        for i in range(k, n):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            if count > max_vowel:
                max_vowel = count

        return max_vowel
