class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
    
        words = []

        for str in strs:
            words.append(f"{len(str)}#{str}")
        
        return "".join(words)


    def decode(self, s: str) -> List[str]:
        original_str = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            # after this, we'll start extracting our string
            length = int(s[i:j])
            start = j + 1
            end = start + length

            original_str.append(s[start:end])

            # moving the i index to the next string iteration
            i = end

        return original_str
