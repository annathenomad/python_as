
#fhand=open('mbox-short.txt')
#for line in fhand:
#    line=line.rstrip()
#    if not line.startswith('From'): continue
#    words=line.split()
#    print (words[2])        


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    nbr=line[20:]
    nbr=float(nbr)
    #print (nbr)
    total=total+nbr

#print (count)
#print (total)
average=total/count
print ('Average spam confidence: ', average)


    
        
    






#to tworzy osobne listy z tymi numerami, każdy osobna lista
    #nbr=line.split()

    #nbr=nbr[1:]
    #print (nbr)
  
    
   
   
