class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")


        if len(pattern) != len(words):
            return False

        char_to_word = {}
        seen_words = set ()

        for c, w in zip(pattern,words):
            if c in char_to_word:
                if char_to_word[c] !=w:
                    return False
            else:

                if w in seen_words:
                    return False
                char_to_word[c] = w
                seen_words.add(w)

        return True                        