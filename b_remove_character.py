#b_remove_character.py

#string copying
def remove_char(s,c):
    l = len(s)
    if l == 0:
        return s
    smallList = remove_char(s[1:],c)
    if s[0] == c:
        return ''+smallList
    else:
        return s[0]+smallList
print(remove_char('abcdef','d'))

#without string copying
def remove_char1(s,c,i):
    l = len(s)
    if l-1 == i:
        return s[i]
    smallList = remove_char1(s,c,i+1)
    if s[i] == c:
        return ''+smallList
    else:
        return s[i]+smallList
print(remove_char1('abcdef','d',0)) 
