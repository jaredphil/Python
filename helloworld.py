

#// Takes a file with 1 column of numbers and turns it into a new file with the numbers
#// in just one row separated by commas
# data = open("workfile.txt").readlines()
# file = open("newfile.txt", "w")
# for n, line in enumerate(data):
#     data[n] = line.rstrip()
# file.write(',\n'.join(data))

data = open("newfile.txt").readlines()
file = open("writefile.txt", "w")
for n, line in enumerate(data):
    data[n]= line.strip(',')

file.write(''.join(data))

# file = open("workfile.txt", "r")
# file2 = open("newfile.txt", "w")

# x = file.readline()
# print (str(x)+",")
# print(file.readline())

# data = open("workfile.txt", "r")
# file = open("newfile.txt", "w")
# count = 0
# for 
# for line in data:
#     print(line.strip())
#     count = count + 1

# print(count)
