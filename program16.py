file=open("marks.txt","w")
file.write("Rahul:85\n")
file.write("Anjali:90\n")
file.close()

file=open("marks.txt","r")
print(file.read())
file.close()
