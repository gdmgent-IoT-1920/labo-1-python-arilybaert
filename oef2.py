# Open the txt
f = open('namen.txt')

# unique names array
uniqueNames = []
diffNames = {}

# use readline() to read the first line 
line = f.readline()
# loop through txt file
while line:

    #print(line)


    # add new name if unique
    if line not in uniqueNames:
        uniqueNames.append(line)
        diffNames[line] = 1
    else:
        diffNames[line] = diffNames[line] +1
    # use realine() to read next line
    line = f.readline()
f.close()


print(diffNames)