A = ["abcdefgh", "abcghijk", "abcefgh"]
B=["anand","kumar"]
commons = [i for i in zip(*A)]
print(commons)
res=""
for i  in commons:
    if(len(set(i))==1):
        res+=i[0]
    else:
        break

print(res)

print(ord('A'))
