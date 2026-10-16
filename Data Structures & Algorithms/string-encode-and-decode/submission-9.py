class Code:
    def __init__(self, s):
        self.string = s
        self.length = len(s)
    
    def __str__(self):
        return f"<{self.length}:::{self.string}>"
    


class Solution:

    # strs=[""] -> [""]
    # strs=[] -> []

    def encode(self, strs: List[str]) -> str:
        # Empty case: strs = []
        if len(strs) == 0:
            return ""
        
        # Case 0: "$<n0:STRING0><n1:STRING1>"
        # Case 1: "$<n0:STRING0>"
        # Case 2: "$"
        return "$" + "".join(str(Code(s)) for s in strs)
    
    def decode(self, s: str) -> List[str]:
        # Empty case: strs = []
        if s == "":
            return []

        # splits = [""] OR ["<n0:STRING0>"] OR [...]
        splits = s[1:].split("><")

        # CASE 2: [""] case
        if len(splits) == 1 and len(splits[0]) == 0:
            return [""]

        # Case 0: ["<n0:STRING0", "n1:STRING1>"]
        # Case 1: ["<n0:STRING0>"]
        strs = []
        for coded_string in splits:
            # coded_n = <n0 OR n1
            # coded_s = STRING0 OR STRING1>
            coded_n, coded_s = coded_string.split(":::")

            length = int(coded_n[(1 if coded_n[0] == "<" else 0):])
            strs.append(coded_s[:length])
        
        return strs

