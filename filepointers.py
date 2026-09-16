# f=open("new.txt","w+")
# print(f.tell()) # returns the current position of the file pointer
# f.write("hello")
# print(f.tell())
# f.write("python")
# print(f.tell())
# f.close()

# f=open("new.txt","w")
# f.write("hello python")
# f.close()

# f=open("new.txt","r")
# print(f.tell()) # returns the current position of the file pointer
# print(f.read(5))
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.close()

# f=open("new.txt","w")
# f.write("hello python")
# f.close()

# f=open("new.txt","r")
# print(f.read())
# print(f.tell())
# f.seek(7) # moves the file pointer to the beginning of the file
# print(f.tell())
# print(f.read())
# f.close()

# f=open("new.txt","w+")
# f.write("hello python")
# print(f.tell())
# f.seek(7) # moves the file pointer to the beginning of the file
# print(f.tell())
# print(f.write("Pu"))
# f.seek(0)
# print(f.read())
# f.close()

try:
    f=open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    f.close()