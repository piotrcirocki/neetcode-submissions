class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct_words = {}
        for i, word in enumerate(strs):
            word_sorted = "".join(sorted(word))
            if word_sorted in dct_words:
                dct_words[word_sorted].append(word)
            else:
                dct_words[word_sorted] = [word]
        result = list(dct_words.values())
        return result
        