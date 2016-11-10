name = input("Enter file name:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

d = dict()

for line in fh :
	words = line.rstrip()
	if words == "": continue
	words = line.split()
	if words[0] != "From" : continue
	time = words[5].split(":")
	d[time[0]] = d.get(time[0], 0) + 1

lst = list()

for key,value in d.items() :
	lst.append((key,value))
lst.sort()

for hour,count in lst :
	print (hour, count)
