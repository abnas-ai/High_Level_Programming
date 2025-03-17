#*******************string slicing**********
# my_string = "Hello, World"
# print(my_string[1:4])
# greeting = "Hello"
# name = "John Doe"
# x = greeting + " " + name[0:4]
# print(x)

#**************concatenation*************
# greeting = "Hello "
# name = "Jane Doe"

# x = "Hello " + name
# print(x)
# name = "Jane Doe"

# 1 Capitalize() method

# name = "jane Doe"
# cap_name = name.capitalize()
# print(cap_name)

#2 upper() method
# name = "jane Doe"
# cap_name = name.upper()
# print(cap_name)

# name = "jane Doe"

#3 Lower Method
# new_name = "DOE"
# new_name = new_name.lower()
# print(new_name)

# 4 count method
# print(new_name.count("o"))

# 5 split method
# name = "jane Doe"
# new_list = name.split()
# print(new_list)

# phone = "0727-870-721"
# print(phone.split('-'))

# my_name = "Kipngeno Abednego Abnas"
# new_li = my_name.split()
# middle_name = new_li[2]
# print(middle_name)

# 6 ******join() method*********

# phone = "0727" "870" "721"
# joined_phone =  ''.join(phone)
# print(joined_phone)

# # print(type(phone))
# # print(type(joined_phone))

# text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# # join elements of text with space
# print(' '.join(text))

# 7*******isalnum()********
# name = "python3"
# print(name.isalnum())

# # 8****isalpha()********
# name = "python3"
# print(name.isalpha())

# 9*****isdecimal()********

# num = "1234"
# print(num.isdecimal())
# num = "qwe"
# print(num.isdecimal())
# num = "1234.456"
# print(num.isdecimal())
# num = "12/34"
# print(num.isdecimal())

# 10********isdigit********


# num = "12/34"
# print(num.isdigit())
# num = "1234"
# print(num.isdigit())
# num = "qwe"
# print(num.isdigit())

# num = "1234.456"
# print(num.isdigit())

# #s = '²3455'
# s = '\u00B23455'
# print(s.isdigit())


# s = '½'
# s = '\u00BD'
# print(s.isdigit())

# text = "python123"
# text2 = "123"
# print(text2.isdigit())



# 11********islower********
# let = "Saxophone"
# print(let.islower())
# let = "saxophone"
# print(let.islower())

#12*****isupper()*********

# let = "Saxophone"
# print(let.isupper())
# let = "saxophone"
# print(let.isupper())

#13*******isidentifier()************
# let = "Saxophone"
# print(let.isidentifier())
# let = "22saxophone"
# print(let.isidentifier())

#14*******isprintable*******

# text1 = 'python programming'

# # checks if text1 is printable 
# result1 = text1.isprintable()
# print(result1)

# text2 = 'python programming\n'

# # checks if text2 is printable 
# result2 = text2.isprintable() 
# print(result2)

# # defining string using ASCII value 
# text = chr(27) + chr(97)

# # checks if text is printable 
# if text.isprintable():
#   print('Printable')
# else:
#   print('Not Printable')



# checks if text1 is printable 
# text1 = "a\n"

# print(text1.isprintable())
# text1 = "a/n"

# print(text1.isprintable())

#*************isspace()************
# s = '   \t'
# print(s.isspace())

# s = ' a '
# print(s.isspace())

# s = ''
# print(s.isspace())
# s = '      t'
# print(s.isspace())
# text = "  "
# print(text.isspace())

#15 *********startswith()*******
# python = "python3"
# print(python.startswith("p"))

# #16******endswith*********
# python = "python3"
# print(python.endswith("3"))

#*********17 f-strings******
#old way of formatting strings
# string = "John"
# age = "23"
# height = "5.6"

# print(f"Hello, {string.upper()} you are {age} years old and {height} tall")

# my_string = "I love Python"
# new_string = my_string.replace ("Python", "Javascript")
# print(new_string)

#18****strips*****
# text = " python "
# print(text)
# text = " python "
# new_text = text.strip()
# print(new_text)


