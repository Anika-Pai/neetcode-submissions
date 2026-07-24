class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cFreqs = {}
        for c in chars:
            cFreqs[c] = cFreqs.get(c, 0) + 1
        
        total = 0
        
        for word in words:
            word_count = {}
            valid = True

            for c in word:
                word_count[c] = word_count.get(c, 0) + 1
                if word_count.get(c, 0) > cFreqs.get(c, 0):
                    valid = False
                    break
            
            if valid:
                total += len(word)

        return total