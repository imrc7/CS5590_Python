# sample input
webStudents=["Revanth","Swathi","Sravya","Vineet","Rakul"]
pythonStudents=["Revanth","Vineet","Samanta","Bunny","Swathi","Rakul"]

# sort both the lists
pythonStudents.sort()
webStudents.sort()

# Calculate length of both lists
wLen=len(webStudents) # 5
pLen=len(pythonStudents) # 6

# initialize the output variables
pIndex,wIndex=0,0
commonStudents=[]
uncommonStudent=[]

# logic to find common and different students
if wLen>0 and pLen>0:
    if wLen>pLen: # 5>6 false so go to else
        while (pIndex < pLen):
            if webStudents[wIndex] == pythonStudents[pIndex]:
                commonStudents.append(pythonStudents[pIndex])
                wIndex += 1
                pIndex += 1
            elif webStudents[wIndex] > pythonStudents[pIndex]:
                uncommonStudent.append(pythonStudents[pIndex])
                pIndex+=1
            else:
                uncommonStudent.append(webStudents[wIndex])
                wIndex += 1
        for i in range(wIndex,wLen):
            uncommonStudent.append(webStudents[i])
    else:
        while (wIndex < wLen): # 0 < 5 true case
            if webStudents[wIndex] == pythonStudents[pIndex]:
                commonStudents.append(pythonStudents[pIndex])
                wIndex += 1
                pIndex += 1
            elif webStudents[wIndex] > pythonStudents[pIndex]:
                uncommonStudent.append(pythonStudents[pIndex])
                pIndex+=1
            else:
                uncommonStudent.append(webStudents[wIndex])
                wIndex += 1
        for i in range(pIndex,pLen):
            uncommonStudent.append(webStudents[i])


elif wLen>0 and pLen<=0:
    uncommonStudent=webStudents
elif  pLen>0 and wLen<=0:
    uncommonStudent=pythonStudents
else:
    print("List should not be empty") # Also validating whether the provided lists are empty or not

# print the result

print("Students enrolled in Web class")
print(webStudents)

print("Students enrolled in python class")
print(pythonStudents)

print("Common Students")
print(commonStudents)

print("Uncommon Students")
print(uncommonStudent)

