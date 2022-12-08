# reads from the list of name until finds the name in the list. if not in the list, reads entire list of names
def read_names(fh,name):
    x=fh.readline()
    while (x!=name+"\n" and x!=""):
        print(x)
        x=fh.readline()
    return

# reads each element of each list within a 2d list
def read_every_element(twoDList):
    for element in twoDList:
        for item in element:
            print(item)
    return

# checks if all elements in 2d list are equal length
def determine_length_equality(twoDList):
    equality = True
    if len(twoDList)>1:
        length = len(twoDList[0])
        for element in twoDList:
            if len(element)!=length:
                equality = False
    return equality

# loops through a string and prints each character
def loop_thru_str(string):
    for char in string:
        print(char)
    return

# makes a staircase of desired bottom level length and symbol
def staircase(symbol,length):
    for i in range(1,length+1):
        print(symbol*i)
    return

# performs both types of division and determines the equality of the results
def both_divisions(a,b):
    return a/b, a//b, a/b == a//b
def twoDToOneD(twoDList):
    new_list = []
    for element in twoDList:
        for i in element:
            new_list.append(i)
    return new_list
