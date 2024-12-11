s="hello"

mp={}

n=len(s)

for i in range(n):
    if s[i] in mp:
        mp[s[i]]+=1
    else :
        mp[s[i]]=1

print(mp)