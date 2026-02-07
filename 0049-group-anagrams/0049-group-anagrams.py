class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            lis = [0] * 26

            for l in word:
                lis[ord(l) - ord('a')] += 1
    
            res[tuple(lis)].append(word)

        return list(res.values())
