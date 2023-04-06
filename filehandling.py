
# open a file
f = open('myfile.txt','r')

# reading file
# content = f.read()

# reding line by line
# content1 = f.readline()


# it's another mehod to open file 
# the file is automatically close
with open('abc.txt','w') as f2:
  for data in f:
    f2.write(data)

# close the file
f.close()    