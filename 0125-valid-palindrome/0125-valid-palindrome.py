class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for char in s:
            if char.isalnum():
                ans.append(char.lower())
        while len(ans)>1:
            if ans.pop(0)!=ans.pop():
                return False
        return True
    