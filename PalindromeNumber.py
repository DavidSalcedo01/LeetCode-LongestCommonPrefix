class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        for i in range(0, len(text)//2, 1):
            first = text[i:i+1]
            last = text[len(text)-(i+1):len(text)-i]
            if(first != last):
                return False
        return True