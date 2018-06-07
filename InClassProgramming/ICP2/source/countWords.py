
with open('sample.txt','r') as f:
    for line in f.readlines():
        words = len(line.split(' '))
        print(line,words)

