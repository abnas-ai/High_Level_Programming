


class AbnasFileError(Exception):
    def  file_not_found(self):
        return "File not found"
    def file_name_correct(self):
        return "File name is correct"

try:
    f = open("abnasfile.txt")
    if f.name == "abnasfile.txt":
        raise  Exception
    
    
except Exception as e:
    print(f"Error! ") 
