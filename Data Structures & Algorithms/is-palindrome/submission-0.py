class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for i in s:
            if i.isalnum():
                new+=i.lower()
        rev=new[::-1]
        if new==rev:
            return True
        else:
            return False
                