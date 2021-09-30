

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        text = ''
        for i in range(len(s)):
            #this is for odd ones for example like "dad"
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if len(text) < len(s[left+1:right]): text = s[left+1:right]
            #this is for even ones for example like "daad" where there is aa in the string
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if len(text) < len(s[left+1:right]): text = s[left+1:right]
        return text

s = ["babad", "cbbd", "a", "ac"]
for i in s:
    print(Solution.longest_palindromic(i))

