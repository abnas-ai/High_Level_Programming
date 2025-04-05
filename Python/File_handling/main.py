
#File input and output

#open() function
#read, write , append
#close() function


#syntax
# open("filename", "mode")

#MODES
# r - read - reads the contents inside that file
# w - write - Creates a file if not existing or ovewrites the content if it exists
# a - append - create a file if it do not exist or add content to the end of the file
# r+ - read and write
# b - binary - read or write a file in binary mode

# read mode

# f = open("test.txt", "r")

# print(f.readline().strip())

# f.close()


#Write

# f = open("output.txt", "w")

# f.write("This is a test file/content.")
# f.write("This content will ovewrite the existing one.")
# f.close()

#******append*******
# f = open("output.txt", "a")
# f.write("this is the content that will bea added to the end of the file.")
# f.close()

# binary
# f = open("img.jpg", "rb")
# print(f.read())

#copy image
# Copy the binary content to another file
# Copy the binary content from the source image to "copied_img.jpg"
# with open("img.jpg", "rb") as source:
#     with open("copied_img.jpg", "wb") as destination:
#         for data in source:
#             destination.write(data)

# Read from "copied_img.jpg" and copy its content to "cop_img.jpg"
with open("img.jpg", "rb") as b:
       for data in b:
         with open("cop_img.jpg", "wb") as f:
     
            f.write(data)