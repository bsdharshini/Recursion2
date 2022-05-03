#d_remove_adjacent_duplicate_elements.py
#copying string multiple times
def remove_adj(s):
    l = len(s)
    if l ==0 or l ==1:
        return s 
    if s[0] == s[1]:
        return remove_adj(s[1:])
    else:
        return s[0]+remove_adj(s[1:])
print(remove_adj('abcdddefccc'))

#without copying string

def remove_adj1(s,i):
    l = len(s)
    if l-1== i or l-2 == i:
        return s[i]+s[i+1]
    if s[i] == s[i+1]:
        return remove_adj1(s,i+1)
    else:
        return s[i]+remove_adj1(s,i+1)
print(remove_adj1('abcdddefccc',0))