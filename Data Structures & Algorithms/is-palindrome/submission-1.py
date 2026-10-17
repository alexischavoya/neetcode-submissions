
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean string
        ascii_lower = set("abcdefghijklmnopqrstuvwxya0987654321")
        s = "".join(filter(lambda c : c in ascii_lower, s.replace(" ","").lower()))

        # Solve
        for i in range(len(s)):
            j = len(s) - 1 - i
            if (s[i] != s[j]):
                return False
        return True