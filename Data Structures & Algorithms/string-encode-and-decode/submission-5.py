class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += s + "_||_"

        return output
    def decode(self, s: str) -> List[str]:
        output = s.split("_||_")
        output.pop()
        return output
