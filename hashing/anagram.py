def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    
    s_hash_table = dict()
    t_hash_table = dict()
    for i in s:
        s_hash_table[i] = s_hash_table.get(i,0)+1
    for j in t:
        t_hash_table[j] = t_hash_table.get(j,0)+1

    for key, value in t_hash_table.items():
        try:
            if t_hash_table[key] == s_hash_table[key]:
                continue
            else:
                print("number of value not equal")
                return False
        except KeyError:
            print("key not found")
            return False
    return True

s = "anagram"
t = "nagaram"


s = "rat"
t = "car"
print(isAnagram(s,t))
     