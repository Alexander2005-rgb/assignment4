# read a file and handle error
try:
    f = open("sample.txt", "r")
    print("Reading file content:")
    print(f.read())

    f.close()
except FileNotFoundError:
    print("Error: the File 'sample.txt' was  not found")

#write and append data to a file

g=open("output.txt",'w')
writing_content =(g.write(input("Enter some content inside the file:")))
print("Data successfully written to output.txt")

g=open("output.txt",'a')
appending_content =(g.write(input("Enter additional text to append :")))
print("Data successfully appended")
print("Final content of output.txt :")
g.close()
g=open("output.txt")
print(g.read())
g.close()
