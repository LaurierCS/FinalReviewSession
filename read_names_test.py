from functions import read_names
fh = open("names.txt","r")
name = input("Enter a name")
read_names(fh,name)
fh.close()
#reads from the list of name until finds the name in the list. if not in the list, reads entire list of names
