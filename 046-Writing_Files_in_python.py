#####Read File
file=open("doc.txt" , "r")
print(file.read())

#####Over-write the text in file 
file=open("doc.txt" , "w")
file.write("I'm A Good Boy")

#####File closing
file.close()

#####Append data into files
file=open("doc.txt" ,  "a")
file.write("\nNo I'm Not a Good Boy")
