#a_Replace_character.py using recursion

#string copying
def replace_s(s,c1,c2):
    l = len(s)
    if l == 0:
        return s
    smallList = replace_s(s[1:],c1,c2)
    if s[0] == c1:
        return c2+smallList
    else:
        s[0]+smallList
t = input()
c1 = input()
c2 = input()
print(replace_s(t,c1,c2))

#without string copying
def replace_char(t,c1,c2,s):
    l = len(t)
    if l == s:
        return t[s]
    smallList = replace_char(t,c1,c2,s+1)
    if t[s] == c1:
        return c2+smallList
    else:
        return t[s]+smallList
    
t = input()
c1 = input()
c2 = input()
print(replace_char(t,c1,c2,0))
