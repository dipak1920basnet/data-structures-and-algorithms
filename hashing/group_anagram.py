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
        if i in idx_track:
            continue
        groups = [strs[i]]
        idx_track.append(i)
        for j in range(i+1,len(strs)):
            if j in idx_track:
                continue
            second = strs[j]
            if helper(strs[i], second):
                groups.append(second)
                idx_track.append(j)
        grouped_anagram.append(groups)
    return grouped_anagram

strs = ["eat","tea","tan","ate","nat","bat"]
# # strs = [""]
# # strs = ["a"]
# print(groupAnagrams(strs))





# Alternate methods:
def group_ana(strs: list[str]) -> list[list[str]]:

    grouped_ana = dict()
    for i in strs:
        val = "".join(sorted(i))
        grouped_ana[val] = grouped_ana.get(val,[])
        grouped_ana[val].append(i)
    return [value for value in grouped_ana.values()]

print(group_ana(strs))