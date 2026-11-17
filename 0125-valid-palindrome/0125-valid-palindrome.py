class Solution:
    def isPalindrome(self, s: str) -> bool:
        right=len(s)-1
        left=0

        while left < right:
            while left<right and not s[left].isalnum():
                left=left+1
            while right>left and not s[right].isalnum():
                right=right-1

            if s[left].lower() != s[right].lower():
                return False
            
            left+=1
            right-=1

        return True

        