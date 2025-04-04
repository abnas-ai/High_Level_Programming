
#How to open files in python
#  1) open() function
#here we only input filename and mode i.e file = open("filename.txt", "mode")

# a)read files
# f = open("MyData.txt", "r")
# print(f.readline().strip())#strip() function is used to remove an extra  empty line
# f.close()

# b)Write files
# f = open('MyData.txt', 'w')
# f.write("This will override the existing file")
# f.close()

# c) Append files
# f = open('MyData.txt', 'a')
# f.write("This content is added at the end of the existing file")
# f.close()

# d) create a new file
# f = open('MyOtherData.txt', 'x') #if the file do not exist it will be created else a FileExists error will appear
# f.write("This content is new")
# f.close()

# e) copy an image or a binary file

# f = open("deck.jpeg", "rb") #opens the source file in binary read mode

# f1 = open("mypic.jpg", "wb")#creates and opens a  new destination file with a new file name in binary write mode

# for i in f: #iterates through the file object
#     f1.write(i) #writes the original file to the destination file
# f.close() #closes the source file
 

# 2)content manager method

# In this method we use with and as
# Generally 'with' opens and closes the file while 'as' gives a temporary variable name to the file

# a)read files

# with open('MyData.txt', 'r') as f:
#     contents = f.read()
#     print(contents)
#     f.close()
    
# b) write files

# with open("MyGuy.txt", "w") as f: #file is overwritten if it exists
#   f.write("Hello guys")

# f.close()

# c)append files

# with open("MyGuy.txt", "a") as f:
#   f.write(" Hello guys another text at the end")

# f.close()

# d) create a  new file

# with open("youguymyguy.txt", "x") as f:
#   f.write("Hello guys here again with another file")
# f.close()

# e) copy an image or a binary file

# ****method 1****

# with open("deck.jpeg", "rb") as f: #opens the original file in read mode
#     with open("djdeck.jpg", "wb") as f2: #creates a new file with new file name in write mode
#         f2.write(f.read())#f.read reads contents of the originl file while f2.write writes the contents to the destination file

# *****method 2****

with open("deck.jpeg", "rb") as f: #opens the original file in read mode
       for data in f: #Iterating through the source file contents
         with open("copied_img.jpg", "wb") as f2: #creates a new file with new file name in write mode
     
            f2.write(data) #writes the contents to the destination file

