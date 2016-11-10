fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
largest=None
d=dict()
for line in fh:
    word=line.split()
    if word==[]: continue
    if word[0]!=('From:'): continue
 
    #print (word)
    output=word[1:]
    #print (output[0])
    if line not in d:
         d[line]=1
    else:
        d[line]=d[line]+1
    mx=max(d, key=d.get)
    maksymalna=mx.strip()
    #print (maksymalna, d[mx])
print (maksymalna, d[mx])
