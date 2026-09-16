# f=open("sample.txt","w")
# creates a file where python file exists
# f=open(r"C:\Users\pawan\OneDrive\Desktop\python\sample.txt","w")
# f.write("Hello World")
# f=open("sample.txt","r")
# print(f.read())
# print(f.readline()) #reads first line of the file
# print(f.readline()) #reads second line of the file
# print(f.readline()) #reads third line of the file
# print(f.readlines()) #reads all lines of the file and returns a list
# f=open("sample.txt","a")
# f.write("learn c\n")
# f.close()
# print(f.read())

# f=open("sample1.txt","x") # creates a new file, if file exists it will raise an error (exclusive creation)
# f=open("images1.jpg","rb")
# print(f.read(20)) # reads first 20 bytes of the file
# f.close()
# p=open("sample.txt","r+") # write and read, but file must be present
# print(p.read())
# p.write("goodbye!\n")
# print(p.read()) 
# p.close()

# p=open("sample2.txt","w+") # write and read, but existing content will be deleted. if file doesn't exist, it will create a new file
# print(p.read())
# # p.write("goodbye!\n")
# # print(p.read()) 
# # p.close()

# p=open("sample3.txt","r+") # file will be created if it doesn't exist, and you can read and write to the file. The file pointer is at the end of the file after writing.
# print(p.read())
# p.write("goodbye!\n")
# print(p.read()) 
# p.close()

# p=open("sample3.txt","r") # file will be created if it doesn't exist, and you can read and write to the file. The file pointer is at the end of the file after writing.
# print(p.read())
# p.close()

# f=open("sample4.txt","w")
# f.write("welcome to python")
# print(f.name) #returns the name of the file
# print(f.mode) #returns the mode of the file
# print(f.closed) #returns true if the file is closed
# f.close()
# print(f.closed)

# with open("sample5.txt","w") as f:
#     f.write("python is a programming language")

# f=open("sample3.txt","w")
# f.writelines(['Hello World\n', 'learn python\n', 'learn java\n', 'learn javascript\n', 'learn c\n', 'goodbye!\n', 'goodbye!\n'])
# f.close()