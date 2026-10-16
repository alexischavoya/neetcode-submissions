class Solution:

    # strs=[""] -> [""]
    # strs=[] -> []
    KEY = "<#>"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return Solution.KEY + Solution.KEY.join(strs)
    
    def decode(self, s: str) -> List[str]:
        if s is "":
            return []
        return s[len(Solution.KEY):].split(Solution.KEY)
