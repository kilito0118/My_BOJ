a=input()
s=[]
cnt=0
for i in a:
    s.append(i)
    cnt+=1
    if cnt<4:
        continue
    if "PPAP" == "".join(s[-4:]):
        s.pop()
        s.pop()
        s.pop()
        cnt-=3
an = "".join(s)
if an=="PPAP" or an=="P":
    print("PPAP")
else:
    print("NP")
