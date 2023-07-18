A='   a ci f ved pu vkfzbu bnbvlvgkua imjd hrrnx nopp p kso iejgcd wyalgcxie yfslfzzw lygatpbv wr budfobxsm'
split=[]
res=""
start=0
print(len(A))
for i in range(len(A)):
    if A[i] != " " and start == 0:
        split.append(i - 1)
        start = 1
        continue

    if A[i]==" " and start==1:
        split.append(i)
    if i==len(A)-1:
        split.append((i+1))
print(split)

for i in range(len(split)-1,0,-1):
    res+=A[split[i-1]+1:split[i]]
    if i!=1:
        res+=" "

print(res)
print(len(res))



