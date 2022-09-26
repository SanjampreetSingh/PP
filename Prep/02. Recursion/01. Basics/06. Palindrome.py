class Solution:
    def palindrome(self, word: str, start: int, end: int)-> bool:
        if start >= end:
            return True
        return word[start] == word[end] and self.palindrome(word, start+1, end-1)

if __name__ == '__main__':
    s= Solution()
    print(s.palindrome("abcba", 0, 4))

# time complexity is O(n)
# space complexity is O(n)