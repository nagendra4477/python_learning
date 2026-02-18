A= [5,3,8,5,2,9,0,0,1,2,5,6]
B=[]
for i in A:
    if i not in B:
        B.append(i)
print(B)
for i in range(len(B)):   
  for i in range(len(B)-1):
      if B[i] > B[i+1]:
          B[i],B[i+1] = B[i+1],B[i]
print(B)