class Solution:
    def encode(self, strs: List[str]) -> str:
        # strs = [(example_string, length),  (example_2, length2) ...]
        if not strs:
            return "empty_fucking_list"
        elif strs == [""]:
            return "list_with_empty_str"
        delimeter = 'Ω'
        return delimeter.join(strs)


    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "empty_fucking_list":
            return []
        elif s == "list_with_empty_str":
            return [""]
        else:
            return s.split('Ω')