list=["PHP", "Exercises", "Backend"]
i=0
word_len=[]
for i in range(len(list)):
    newlist=[]
    newlist.insert(i,str(len(list[i])))
    newlist.insert(i+1,list[i])
    word_len.insert(i,newlist)
    print(newlist)
    i+=1
word_len.sort()
print("the longest one is:",word_len[-1])

