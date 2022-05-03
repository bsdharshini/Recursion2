#c_Replace_pi_with_3.14.py
#copying string

def replace_pi(s):
    l = len(s)
    if l ==0 or l ==1:
        return s
    if s[0]+s[1] == 'pi':
        return '3.14'+replace_pi(s[2:])
    else:
        return s[0]+replace_pi(s[1:])
print(replace_pi("abcpide"))

#without copying
def replace_pi1(s,i):
    l = len(s)
    if l-1 == i or l-2 == i:
        return s[i]+s[i+1]
    if s[i]+s[i+1] == 'pi':
        return '3.14'+replace_pi1(s,i+2)
    else:
        return s[i]+replace_pi1(s,i+1)
print(replace_pi1("abcpide",0))