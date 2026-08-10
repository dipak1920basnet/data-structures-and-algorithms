def groupAnagrams(strs: list[str]) -> list[list[str]]:
    def helper(first:str, second:str)->bool:
        if len(first)!= len(second):
            return False

        for i in set(first):
            if first.count(i) != second.count(i):
                return False
        return True

    grouped_anagram = []
    idx_track = []
    for i in range(len(strs)):
        groups = []
        if i not in idx_track:
            first = strs[i]
            idx_track.append(i)
            groups.append(first)
            for j in range(i+1,len(strs)):
                if j not in idx_track:
                    second = strs[j]
                    if helper(first, second):
                        groups.append(second)
                        idx_track.append(j)
        if len(groups) > 0:
            grouped_anagram.append(groups)
    return grouped_anagram

strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]
strs = ["a"]
print(groupAnagrams(strs))